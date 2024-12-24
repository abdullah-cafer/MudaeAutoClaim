import sys
import asyncio
import discord
from discord.ext import commands
import random
import re
import json
import os
import threading
import time
import subprocess
import datetime
import inquirer

# Load presets from JSON file
presets = {}
try:
    with open("presets.json", "r") as f:
        presets = json.load(f)
except FileNotFoundError:
    print("presets.json dosyası bulunamadı. Lütfen oluşturun ve gerekli bilgileri girin.")
    sys.exit(1)

# Dictionary to store bots
bots = {}

# Target bot ID (Mudae's ID)
TARGET_BOT_ID = 432610292342587392

# Log list
log_list = []

# Preset logs
preset_logs = {}


def run_bot(token, prefix, target_channel_id, roll_command, min_kakera, delay_seconds, mudae_prefix, log_function, preset_name, key_mode):
    client = commands.Bot(command_prefix=prefix)
    client.min_kakera = min_kakera

    @client.event
    async def on_ready():
        log_function(f"[{client.user}] Bot is ready.", preset_name)
        log_function(f"[{client.user}] Delay: {delay_seconds} seconds", preset_name)
        log_function(f"[{client.user}] Key Mode: {'Enabled' if key_mode else 'Disabled'}", preset_name)
        await asyncio.sleep(delay_seconds)

        channel = client.get_channel(target_channel_id)
        try:
            await channel.send(f"{mudae_prefix}limroul 1 1 1 1")
            await asyncio.sleep(0.5)
            await channel.send(f"{mudae_prefix}dk")
            await asyncio.sleep(0.5)
            await channel.send(f"{mudae_prefix}daily")
            await asyncio.sleep(0.5)
            await check_claim_rights(client, channel)
        except discord.errors.Forbidden as e:
            log_function(f"[{client.user}] Hata: Kanala mesaj göndereme iznim yok. {e}", preset_name)
            await client.close()

    async def check_claim_rights(client, channel):
        log_function(f"[{client.user}] Checking claim rights...", preset_name)
        error_count = 0
        max_retries = 5
        while True:
            await channel.send(f"{mudae_prefix}mu")
            await asyncio.sleep(1)
            try:
                async for msg in channel.history(limit=5):
                    if msg.author.id == TARGET_BOT_ID:
                        if "right now" in msg.content.lower():
                            match = re.search(r"The next claim reset is in \*\*(\d+h)?\s*(\d+)\*\* min\.", msg.content)
                            if match:
                                hours = int(match.group(1)[:-1]) if match.group(1) else 0
                                minutes = int(match.group(2))
                                remaining_seconds = (hours * 60 + minutes) * 60

                                if remaining_seconds <= 3600:
                                    log_function(f"[{client.user}] Claim right available and less than 1 hour remaining.", preset_name)
                                    await check_rolls_left(client, channel, ignore_limit=True)
                                else:
                                    log_function(f"[{client.user}] Claim right available. Applying claim limit.", preset_name)
                                    await check_rolls_left(client, channel)
                                return
                            else:
                                raise ValueError("Time information could not be parsed.")
                        elif "you can't claim" in msg.content.lower():
                            match = re.search(r"you can't claim for another \*\*(\d+h)?\s*(\d+)\*\* min\.", msg.content)
                            if match:
                                hours = int(match.group(1)[:-1]) if match.group(1) else 0
                                minutes = int(match.group(2))
                                total_seconds = (hours * 60 + minutes) * 60
                                if key_mode:
                                    log_function(f"[{client.user}] Claim right not available, but Key Mode is enabled. Rolling for kakera only.", preset_name)
                                    await check_rolls_left(client, channel, ignore_limit=True, key_mode_only_kakera=True)
                                    return
                                else:
                                    log_function(f"[{client.user}] Claim right not available. Will retry in {hours}h {minutes}min.", preset_name)
                                    await wait_for_reset(total_seconds, delay_seconds, log_function, preset_name)
                                    await check_claim_rights(client, channel)
                                    return
                            else:
                                raise ValueError("Waiting time not found.")
                        else:
                            raise ValueError("Mudae message not found.")
                    else:
                        raise ValueError("Mudae message not found.")

            except ValueError as e:
                error_count += 1
                log_function(f"[{client.user}] Error: {e}", preset_name)
                if error_count >= max_retries:
                    log_function(f"[{client.user}] Max retries reached for claim rights. Retrying in 30 minutes.", preset_name)
                    await asyncio.sleep(1800)
                    error_count = 0
                else:
                    log_function(f"[{client.user}] Claim right check failed. Retrying in 5 seconds.", preset_name)
                    await asyncio.sleep(5)
                continue

            except Exception as e:
                error_count += 1
                log_function(f"[{client.user}] Error: {e}", preset_name)
                if error_count >= max_retries:
                    log_function(f"[{client.user}] Max retries reached for claim rights. Retrying in 30 minutes.", preset_name)
                    await asyncio.sleep(1800)
                    error_count = 0
                else:
                    log_function(f"[{client.user}] Claim right check failed. Retrying in 5 seconds.", preset_name)
                    await asyncio.sleep(5)
                continue


    async def check_rolls_left(client, channel, ignore_limit=False, key_mode_only_kakera=False):
        error_count = 0
        max_retries = 5
        while True:
            await channel.send(f"{mudae_prefix}ru")
            await asyncio.sleep(1)
            try:
                async for msg in channel.history(limit=5):
                    if msg.author.id == TARGET_BOT_ID and "roll" in msg.content.lower():
                        match = re.search(r"You have \*\*(\d+)\*\* roll(?:s)?(?: \+\*\*(\d+)\*\* \$mk)? left\.", msg.content)
                        if not match:
                            match = re.search(r"You have (\d+) rolls? left\.", msg.content)

                        if match:
                            rolls_left = int(match.group(1))
                            reset_match = re.search(r"Next rolls? reset in \*\*(\d+)\*\* (min|h)", msg.content)
                            if reset_match:
                                reset_time = int(reset_match.group(1))
                                reset_unit = reset_match.group(2)
                                if reset_unit == "h":
                                    reset_time *= 60
                            else:
                                reset_time = 0
                                log_function(f"[{client.user}] Warning: Could not parse roll reset time.", preset_name)

                            if rolls_left == 0:
                                log_function(f"[{client.user}] No rolls left. Reset in {reset_time} min.", preset_name)
                                await wait_for_rolls_reset(reset_time, delay_seconds, log_function, preset_name)
                                await check_claim_rights(client, channel)
                                return
                            else:
                                log_function(f"[{client.user}] Rolls left: {rolls_left}", preset_name)
                                await start_roll_commands(client, channel, rolls_left, ignore_limit, key_mode_only_kakera)
                                return
                        else:
                            log_function(f"[{client.user}] Could not parse roll information: {msg.content}", preset_name)
                            raise ValueError(f"Could not parse roll information. Mudae's response was: {msg.content}")

                raise ValueError("Mudae did not respond with roll information within the time limit.")

            except ValueError as e:
                error_count += 1
                log_function(f"[{client.user}] Error ({error_count}/{max_retries}): {e}", preset_name)
                if error_count >= max_retries:
                    log_function(f"[{client.user}] Max retries reached. Giving up on roll check. Retrying in 30 minutes.", preset_name)
                    await asyncio.sleep(1800)
                    error_count = 0
                else:
                    await asyncio.sleep(5)
            except Exception as e:
                error_count += 1
                log_function(f"[{client.user}] Unexpected error ({error_count}/{max_retries}): {e}", preset_name)
                if error_count >= max_retries:
                    log_function(f"[{client.user}] Max retries reached. Giving up on roll check. Retrying in 30 minutes.", preset_name)
                    await asyncio.sleep(1800)
                    error_count = 0
                else:
                    await asyncio.sleep(5)



    async def start_roll_commands(client, channel, rolls_left, ignore_limit=False, key_mode_only_kakera=False):
        for _ in range(rolls_left):
            await channel.send(f"{mudae_prefix}{roll_command}")
            await asyncio.sleep(0.3)

        await asyncio.sleep(4)

        await check_new_characters(client, channel)

        mudae_messages = []
        async for msg in channel.history(limit=rolls_left * 2, oldest_first=False):
            if msg.author.id == TARGET_BOT_ID:
                mudae_messages.append(msg)

        await handle_mudae_messages(client, channel, mudae_messages, ignore_limit, key_mode_only_kakera)

        await asyncio.sleep(2)
        await check_claim_rights(client, channel)


    async def handle_mudae_messages(client, channel, mudae_messages, ignore_limit=False, key_mode_only_kakera=False):
        highest_claim_character = None
        highest_claim_character_message = None
        second_highest_claim_character = None
        second_highest_claim_character_message = None
        lowest_claim_kakera = None
        lowest_claim_kakera_message = None
        
        for msg in mudae_messages:
            if msg.embeds:
                embed = msg.embeds[0]

                if msg.components:
                    for component in msg.components:
                        for button in component.children:
                            if button.emoji and button.emoji.name in ['kakeraY', 'kakeraO', 'kakeraR', 'kakeraW', 'kakeraL']:
                                try:
                                    await button.click()
                                    log_function(f"[{client.user}] Claimed Kakera: {msg.embeds[0].author.name}", preset_name)
                                    log_list.append(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Claimed Kakera: {msg.embeds[0].author.name}")
                                    await asyncio.sleep(3)
                                except discord.errors.HTTPException as e:
                                    log_function(f"[{client.user}] Kakera claim hatası: {e}", preset_name)

                if embed.color.value in [16751916, 1360437]:
                    match = re.search(r"\*\*(\d+)\*\*<:kakera:", embed.description)
                    if match:
                        kakera_value = int(match.group(1))
                        
                        if (not highest_claim_character or kakera_value > highest_claim_character) and (ignore_limit or kakera_value > client.min_kakera):
                            second_highest_claim_character = highest_claim_character
                            second_highest_claim_character_message = highest_claim_character_message
                            highest_claim_character = kakera_value
                            highest_claim_character_message = msg
                        elif (not second_highest_claim_character or kakera_value > second_highest_claim_character) and (ignore_limit or kakera_value > client.min_kakera):
                             second_highest_claim_character = kakera_value
                             second_highest_claim_character_message = msg

                else:
                    match = re.search(r"\*\*(\d+)\*\*", embed.description)
                    if match:
                        kakera_value = int(match.group(1))
                        if (not lowest_claim_kakera or kakera_value < lowest_claim_kakera):
                            lowest_claim_kakera = kakera_value
                            lowest_claim_kakera_message = msg

        if not key_mode_only_kakera:
            if highest_claim_character_message:
                await claim_character(client, channel, highest_claim_character_message)

                if second_highest_claim_character_message:
                   if second_highest_claim_character > client.min_kakera:
                       await channel.send(f"{mudae_prefix}rt")
                       await asyncio.sleep(0.5)
                       await claim_character(client, channel, second_highest_claim_character_message, is_rt_claim=True)
                   else:
                       log_function(f"[{client.user}] $rt ile alınacak karakter limiti karşılamıyor.", preset_name)
        elif key_mode_only_kakera:
            if highest_claim_character_message:
                if highest_claim_character > client.min_kakera:
                    await channel.send(f"{mudae_prefix}rt")
                    await asyncio.sleep(0.5)
                    await claim_character(client, channel, highest_claim_character_message, is_rt_claim=True)
                else:
                    log_function(f"[{client.user}] $rt ile alınacak karakter limiti karşılamıyor.", preset_name)


        if lowest_claim_kakera_message:
            await claim_character(client, channel, lowest_claim_kakera_message, is_kakera=True)


    async def claim_character(client, channel, msg, is_kakera=False, is_rt_claim=False):
        log_message = "Claimed Kakera" if is_kakera else "Claimed Character"
        if is_rt_claim:
            log_message = "Claimed Character with $rt"


        if msg.components:
            for component in msg.components:
                for button in component.children:
                    if button.emoji and button.emoji.name in ['💖', '💗', '💘', '❤️', '💓', '💕', '♥️', '🪐']:
                        try:
                            await button.click()
                            log_function(f"[{client.user}] {log_message}: {msg.embeds[0].author.name}", preset_name)
                            log_list.append(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {log_message}: {msg.embeds[0].author.name}")
                            await asyncio.sleep(3)
                            return
                        except discord.errors.HTTPException as e:
                            log_function(f"[{client.user}] Karakter claim hatası: {e}", preset_name)
        else:
            try:
                await msg.add_reaction("✅")
                log_function(f"[{client.user}] {log_message}: {msg.embeds[0].author.name}", preset_name)
                log_list.append(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {log_message}: {msg.embeds[0].author.name}")
                await asyncio.sleep(3)
            except discord.errors.HTTPException:
                log_function(f"[{client.user}] Reaksiyon eklenemedi. Muhtemelen karakter başkası tarafından çoktan alındı.", preset_name)



    async def check_new_characters(client, channel):
        async for msg in channel.history(limit=15):
            if msg.author.id == TARGET_BOT_ID:
                if msg.embeds:
                    embed = msg.embeds[0]
                    match = re.search(r"Claims: \#(\d+)", embed.description)
                    if match:
                        claims_value = int(match.group(1))
                        log_function(f"[{client.user}] New character: {embed.author.name} (Claims: #{claims_value})", preset_name)

    async def wait_for_reset(seconds, delay_seconds, log_function, preset_name):
        now = datetime.datetime.now()
        target_time = now + datetime.timedelta(seconds=seconds)

        target_minute = target_time.minute
        target_second = 0
        target_time = target_time.replace(second=target_second, microsecond=0)

        if target_time < now:
            target_time += datetime.timedelta(minutes=1)

        wait_seconds = (target_time - now).total_seconds() + delay_seconds
        log_function(f"[{client.user}] Waiting for reset. Target time: {target_time.strftime('%H:%M:%S')}, additional delay: {delay_seconds} seconds", preset_name)
        await asyncio.sleep(wait_seconds)


    async def wait_for_rolls_reset(reset_time_minutes, delay_seconds, log_function, preset_name):
        now = datetime.datetime.now()
        target_minute = (now.minute + reset_time_minutes) % 60
        target_second = 0
        target_time = now.replace(minute=target_minute, second=target_second, microsecond=0)

        if target_time < now:
            target_time += datetime.timedelta(hours=1)

        wait_seconds = (target_time - now).total_seconds() + delay_seconds
        log_function(f"[{client.user}] Waiting for rolls reset. Target time: {target_time.strftime('%H:%M:%S')}, additional delay: {delay_seconds} seconds", preset_name)
        await asyncio.sleep(wait_seconds)


    client.run(token)


def print_log(message, preset_name):
    print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}][{preset_name}] {message}")



def main_menu():
    while True:
        questions = [
            inquirer.List('option',
                          message="Please select an option:",
                          choices=['Select and Run Preset', 'Select and Run Multiple Presets', 'Exit'],
                          ),
        ]
        answers = inquirer.prompt(questions)

        if answers['option'] == 'Select and Run Preset':
            select_and_run_preset()
        elif answers['option'] == 'Select and Run Multiple Presets':
            select_and_run_multiple_presets()
        elif answers['option'] == 'Exit':
            break



def select_and_run_preset():
    preset_list = list(presets.keys())
    if not preset_list:
        print("No presets found.")
        return

    questions = [
        inquirer.List('preset',
                      message="Select a preset to run:",
                      choices=preset_list,
                      ),
    ]
    answers = inquirer.prompt(questions)
    selected_preset = answers['preset']

    preset = presets[selected_preset]
    key_mode = preset.get("key_mode", False)

    threading.Thread(target=run_bot, args=(preset["token"], preset["prefix"],
                                             preset["channel_id"], preset["roll_command"],
                                             preset["min_kakera"], preset["delay_seconds"],
                                             preset["mudae_prefix"], print_log, selected_preset, key_mode)).start()



def select_and_run_multiple_presets():
    preset_list = list(presets.keys())
    if not preset_list:
        print("No presets found.")
        return

    questions = [
        inquirer.Checkbox('presets',
                          message="Select presets to run (Use spacebar to select, Enter to confirm):",
                          choices=preset_list,
                          ),
    ]
    answers = inquirer.prompt(questions)
    selected_presets = answers['presets']

    for preset_name in selected_presets:
        preset = presets[preset_name]
        key_mode = preset.get("key_mode", False)
        threading.Thread(target=run_bot, args=(preset["token"], preset["prefix"],
                                                 preset["channel_id"], preset["roll_command"],
                                                 preset["min_kakera"], preset["delay_seconds"],
                                                 preset["mudae_prefix"], print_log, preset_name, key_mode)).start()



if __name__ == "__main__":
    main_menu()
