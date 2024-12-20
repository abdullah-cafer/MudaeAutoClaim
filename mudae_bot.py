import asyncio
import datetime
import json
import random
import re
import sys
import threading
import time
from collections import deque

import discord
import inquirer
import keyboard
from discord.ext import commands
from rich.console import Console
from rich.live import Live
from rich.table import Table

# Load presets
try:
    presets = json.load(open("presets.json", "r"))
except FileNotFoundError:
    print("presets.json not found.")
    sys.exit(1)

TARGET_BOT_ID = 432610292342587392
preset_statuses = {}
preset_statuses_lock = threading.Lock()
console = Console()
running_presets = {}
preset_logs = {}
MAX_LOG_LINES = 5
current_page = 0
presets_per_page = 5

def update_status(name, char=None, status=None, reset=None):
    with preset_statuses_lock:
        if name not in preset_statuses:
            preset_statuses[name] = {"last_character": "-", "status": "", "reset_time": ""}
        if char:
            preset_statuses[name]["last_character"] = char
        if status:
            preset_statuses[name]["status"] = status
        if reset:
            preset_statuses[name]["reset_time"] = reset

def log_msg(msg, name, is_err=False):
    ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_msg = f"[{ts}] [{name}] {msg}"
    with open("logs.txt", "a") as f:
        f.write(log_msg + "\n")
    if is_err:
        console.log(log_msg)
    with preset_statuses_lock:
        if name not in preset_logs:
            preset_logs[name] = deque(maxlen=MAX_LOG_LINES)
        preset_logs[name].append(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {msg}")

async def run_bot(preset_name):
    preset = presets[preset_name]
    client = commands.Bot(command_prefix=preset["prefix"])
    client.min_kakera = preset["min_kakera"]
    running_presets[preset_name] = True
    key_mode = preset.get("key_mode", False)
    delay = preset["delay_seconds"]
    mudae_prefix = preset["mudae_prefix"]
    target_channel_id = preset["channel_id"]
    roll_command = preset["roll_command"]

    @client.event
    async def on_ready():
        log_msg(f"Bot ready, delay: {delay}s, Key Mode: {'On' if key_mode else 'Off'}", preset_name)
        update_status(preset_name, status="Ready")
        await asyncio.sleep(delay)
        ch = client.get_channel(target_channel_id)
        try:
            for cmd in [f"{mudae_prefix}limroul 1 1 1 1", f"{mudae_prefix}dk", f"{mudae_prefix}daily"]:
                await ch.send(cmd)
                await asyncio.sleep(0.5)
            await check_claim(client, ch)
        except discord.errors.Forbidden as e:
            log_msg(f"[bold red]Discord Error:[/bold red] Cannot send: {e}", preset_name, is_err=True)
            update_status(preset_name, status="[bold red]Error:[/bold red] No Send Perms")
            await client.close()
        except Exception as e:
            log_msg(f"[bold red]Error:[/bold red] Unexpected: {e}", preset_name, is_err=True)
            update_status(preset_name, status=f"[bold red]Error:[/bold red] {e}")
            await client.close()
        finally:
            running_presets.pop(preset_name, None)

    async def check_claim(client, ch):
        update_status(preset_name, status="Checking Claim")
        for attempt in range(5):
            await ch.send(f"{mudae_prefix}mu")
            await asyncio.sleep(1)
            try:
                async for msg in ch.history(limit=1):
                    if msg.author.id == TARGET_BOT_ID:
                        content = msg.content.lower()
                        if "right now" in content:
                            match = re.search(r"in \*\*(\d+h)?\s*(\d+)\*\* min", content)
                            if match:
                                h = int(match.group(1)[:-1]) if match.group(1) else 0
                                m = int(match.group(2))
                                secs = (h * 60 + m) * 60
                                update_status(preset_name, status="Claim Ready", reset=f"{h}h {m}m" if secs <= 3600 else f"{h}h {m}m")
                                await check_rolls(client, ch)
                                return
                            raise ValueError("No time info")
                        elif "you can't claim" in content:
                            match = re.search(r"another \*\*(\d+h)?\s*(\d+)\*\* min", content)
                            if match:
                                h = int(match.group(1)[:-1]) if match.group(1) else 0
                                m = int(match.group(2))
                                total_secs = (h * 60 + m) * 60
                                update_status(preset_name, reset=f"{h}h {m}m")
                                if key_mode:
                                    update_status(preset_name, status="Key Mode - Rolling Kakera")
                                    await check_rolls(client, ch, True, True)
                                    return
                                else:
                                    update_status(preset_name, status=f"Waiting {h}h {m}m")
                                    await wait(total_secs, delay, preset_name)
                                    await check_claim(client, ch)
                                    return
                            raise ValueError("No wait time")
                        raise ValueError("Mudae msg not found")
            except ValueError as e:
                log_msg(f"[bold red]Error:[/bold red] {e}", preset_name, is_err=True)
                update_status(preset_name, status=f"[bold red]Error:[/bold red] Checking claim ({attempt+1}/5)")
                await asyncio.sleep(5)
            except discord.errors.HTTPException as e:
                log_msg(f"[bold red]Discord Error:[/bold red] HTTP claim check: {e}", preset_name, is_err=True)
                update_status(preset_name, status=f"[bold red]Error:[/bold red] Checking claim ({attempt+1}/5)")
                await asyncio.sleep(5)
        log_msg(f"Max retries for claim. Retrying in 30 min.", preset_name, is_err=True)
        update_status(preset_name, status="Retrying claim in 30m")
        await asyncio.sleep(1800)
        await check_claim(client, ch)

    async def check_rolls(client, ch, ignore_limit=False, key_mode_only_kakera=False):
        update_status(preset_name, status="Checking Rolls")
        for attempt in range(5):
            await ch.send(f"{mudae_prefix}ru")
            await asyncio.sleep(1)
            try:
                async for msg in ch.history(limit=5):
                    if msg.author.id == TARGET_BOT_ID and "roll" in msg.content.lower():
                        match = re.search(r"You have \*\*(\d+)\*\* roll(?:s)?(?: \+\*\*(\d+)\*\* \$mk)? left", msg.content)
                        if not match:
                            match = re.search(r"You have (\d+) rolls? left", msg.content)
                        if match:
                            rolls = int(match.group(1))
                            reset_match = re.search(r"Next rolls? reset in \*\*(\d+)\*\* (min|h)", msg.content)
                            if reset_match:
                                reset_time = int(reset_match.group(1)) * (60 if reset_match.group(2) == "h" else 1)
                                update_status(preset_name, reset=f"{reset_time}m (Rolls)", status=f"Rolls: {rolls}")
                            else:
                                update_status(preset_name, reset="Unknown (Rolls)", status=f"Rolls: {rolls}")

                            if rolls == 0:
                                update_status(preset_name, status=f"No Rolls - Waiting {reset_time}m")
                                await wait_rolls(reset_time, delay, preset_name)
                                await check_claim(client, ch)
                                return
                            await start_rolls(client, ch, rolls, ignore_limit, key_mode_only_kakera)
                            return
                        raise ValueError(f"No roll info: {msg.content}")
                raise ValueError("No Mudae roll response")
            except ValueError as e:
                log_msg(f"[bold red]Error:[/bold red] {e}", preset_name, is_err=True)
                update_status(preset_name, status=f"[bold red]Error:[/bold red] Checking rolls ({attempt+1}/5)")
                await asyncio.sleep(5)
            except discord.errors.HTTPException as e:
                log_msg(f"[bold red]Discord Error:[/bold red] HTTP roll check: {e}", preset_name, is_err=True)
                update_status(preset_name, status=f"[bold red]Error:[/bold red] Checking rolls ({attempt+1}/5)")
                await asyncio.sleep(5)
        log_msg(f"Max roll retries. Retrying in 30 min.", preset_name, is_err=True)
        update_status(preset_name, status="Retrying rolls in 30m")
        await asyncio.sleep(1800)
        await check_claim(client, ch)

    async def start_rolls(client, ch, rolls, ignore_limit, key_mode_only_kakera):
        update_status(preset_name, status="Rolling")
        for _ in range(rolls):
            await ch.send(f"{mudae_prefix}{roll_command}")
            await asyncio.sleep(0.3)
        await asyncio.sleep(4)
        mudae_msgs = [msg async for msg in ch.history(limit=rolls * 2, oldest_first=False) if msg.author.id == TARGET_BOT_ID]
        await handle_rolls(client, ch, mudae_msgs, ignore_limit, key_mode_only_kakera)
        await asyncio.sleep(2)
        await check_claim(client, ch)

    async def handle_rolls(client, ch, msgs, ignore_limit, key_mode_only_kakera):
        claims = sorted([msg for msg in msgs if msg.embeds and msg.embeds[0].color.value in [16751916, 1360437]],
                      key=lambda m: int(re.search(r"\*\*(\d+)\*\*<:kakera:", m.embeds[0].description).group(1)) if re.search(r"\*\*(\d+)\*\*<:kakera:", m.embeds[0].description) else 0, reverse=True)
        other_claims = sorted([msg for msg in msgs if msg.embeds and msg.embeds[0].color.value not in [16751916, 1360437]],
                             key=lambda m: int(re.search(r"\*\*(\d+)\*\*", m.embeds[0].description).group(1)) if m.embeds and re.search(r"\*\*(\d+)\*\*", m.embeds[0].description) else 0)

        async def claim(msg, rt=False):
            log_msg(f"{'Claimed Kakera' if 'kakera' in msg.embeds[0].description.lower() else ('Claimed with $rt' if rt else 'Claimed')}: {msg.embeds[0].author.name}", preset_name)
            update_status(preset_name, char=msg.embeds[0].author.name)
            for comp in msg.components:
                for btn in comp.children:
                    if btn.emoji and btn.emoji.name in ['💖', '💗', '💘', '❤️', '💓', '💕', '♥️', '🪐']:
                        try:
                            await btn.click()
                            await asyncio.sleep(3)
                            return
                        except discord.errors.HTTPException as e:
                            log_msg(f"[bold red]Discord Error:[/bold red] Claim error: {e}", preset_name, is_err=True)
            try:
                await msg.add_reaction("✅")
                await asyncio.sleep(3)
            except discord.errors.HTTPException as e:
                log_msg(f"[bold red]Discord Error:[/bold red] Reaction error: {e}", preset_name, is_err=True)

        for msg in msgs:
            if msg.components:
                for comp in msg.components:
                    for btn in comp.children:
                        if btn.emoji and btn.emoji.name in ['kakeraY', 'kakeraO', 'kakeraR', 'kakeraW', 'kakeraL']:
                            try:
                                await btn.click()
                                log_msg(f"Claimed Kakera: {msg.embeds[0].author.name}", preset_name)
                                await asyncio.sleep(3)
                            except discord.errors.HTTPException as e:
                                log_msg(f"[bold red]Discord Error:[/bold red] Kakera claim error: {e}", preset_name, is_err=True)

        if not key_mode_only_kakera:
            if claims and (ignore_limit or int(re.search(r"\*\*(\d+)\*\*<:kakera:", claims[0].embeds[0].description).group(1)) > client.min_kakera):
                await claim(claims[0])
                if len(claims) > 1 and int(re.search(r"\*\*(\d+)\*\*<:kakera:", claims[1].embeds[0].description).group(1)) > client.min_kakera:
                    await ch.send(f"{mudae_prefix}rt")
                    await asyncio.sleep(0.5)
                    await claim(claims[1], True)
        elif key_mode_only_kakera and claims and int(re.search(r"\*\*(\d+)\*\*<:kakera:", claims[0].embeds[0].description).group(1)) > client.min_kakera:
            await ch.send(f"{mudae_prefix}rt")
            await asyncio.sleep(0.5)
            await claim(claims[0], True)

        if other_claims:
            await claim(other_claims[0])

    async def wait(secs, delay, name):
        target_time = (datetime.datetime.now() + datetime.timedelta(seconds=secs)).replace(second=0, microsecond=0)
        update_status(name, status="Waiting for reset", reset=target_time.strftime('%H:%M:%S'))
        log_msg(f"Waiting for reset. Target: {target_time.strftime('%H:%M:%S')}, delay: {delay}s", name)
        await asyncio.sleep(secs + delay)

    async def wait_rolls(minutes, delay, name):
        now = datetime.datetime.now()
        target_minute = (now.minute + minutes) % 60
        target_time = now.replace(minute=target_minute, second=0, microsecond=0)
        if target_time < now:
            target_time += datetime.timedelta(hours=1)
        wait_seconds = (target_time - now).total_seconds() + delay
        update_status(name, status="Waiting for rolls", reset=target_time.strftime('%H:%M:%S'))
        log_msg(f"Waiting for rolls reset. Target: {target_time.strftime('%H:%M:%S')}, delay: {delay}s", name)
        await asyncio.sleep(wait_seconds)

    await client.start(preset["token"])

def display_menu():
    def change_page(key):
        global current_page
        max_page = (len(running_presets) - 1) // presets_per_page
        current_page = max(0, current_page - 1) if key == 'k' else min(max_page, current_page + 1)

    keyboard.add_hotkey('k', change_page, args=('k',))
    keyboard.add_hotkey('l', change_page, args=('l',))

    with Live(console=console, screen=True, refresh_per_second=4) as live:
        while running_presets:
            table = Table(title=f"Running Presets - Page {current_page + 1}")
            table.add_column("Preset", style="cyan")
            table.add_column("Last Char", style="magenta")
            table.add_column("Status", style="green")
            table.add_column("Refresh", style="yellow")
            table.add_column("Logs", style="dim")

            with preset_statuses_lock:
                start = current_page * presets_per_page
                end = start + presets_per_page
                for name, status in list(preset_statuses.items())[start:end]:
                    log_text = "\n".join(preset_logs.get(name, []))
                    table.add_row(name, status["last_character"], status["status"], status["reset_time"], log_text)
            live.update(table)
            time.sleep(0.25)

def main_menu():
    while True:
        actions = {
            'Run Preset': select_and_run,
            'Run Multiple Presets': select_and_run_multiple,
            'Exit': sys.exit
        }
        questions = [inquirer.List('action', message="Select an option:", choices=actions.keys())]
        answer = inquirer.prompt(questions)
        actions[answer['action']]()

def select_and_run():
    presets_list = list(presets.keys())
    if not presets_list:
        print("No presets found.")
        return
    questions = [inquirer.List('preset', message="Select a preset to run:", choices=presets_list)]
    answer = inquirer.prompt(questions)
    preset_name = answer['preset']
    threading.Thread(target=asyncio.run, args=(run_bot(preset_name),)).start()
    if not any(t.name == "display_thread" for t in threading.enumerate()):
        threading.Thread(target=display_menu, name="display_thread", daemon=True).start()

def select_and_run_multiple():
    presets_list = list(presets.keys())
    if not presets_list:
        print("No presets found.")
        return
    questions = [inquirer.Checkbox('presets', message="Select presets to run:", choices=presets_list)]
    answers = inquirer.prompt(questions)
    for preset_name in answers['presets']:
        threading.Thread(target=asyncio.run, args=(run_bot(preset_name),)).start()
    if not any(t.name == "display_thread" for t in threading.enumerate()):
        threading.Thread(target=display_menu, name="display_thread", daemon=True).start()

if __name__ == "__main__":
    main_menu()
