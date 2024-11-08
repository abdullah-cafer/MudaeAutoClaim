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
    pass  # Ignore if file doesn't exist


# Dictionary to store bots (each bot has a separate Discord client)
bots = {}


# Target bot ID (Mudae's ID)
TARGET_BOT_ID = 432610292342587392


# Log list
log_list = []


# Preset logs
preset_logs = {}


# Function to run a bot instance
def run_bot(token, prefix, target_channel_id, roll_command, claim_limit, delay_seconds, mudae_prefix, log_function, preset_name):
    client = commands.Bot(command_prefix=prefix)

    @client.event
    async def on_ready():
        log_function(f"[{client.user}] Bot is ready.", preset_name)
        # Wait for the specified delay
        log_function(f"[{client.user}] Delay: {delay_seconds} seconds", preset_name)
        await asyncio.sleep(delay_seconds)

        # Send initial commands
        channel = client.get_channel(target_channel_id)
        await channel.send(f"{mudae_prefix}limroul 1 1 1 1")  # Limit rolls to 1 for each rarity
        await asyncio.sleep(0.5)
        await channel.send(f"{mudae_prefix}dk")  # Daily kakera
        await asyncio.sleep(0.5)
        await channel.send(f"{mudae_prefix}daily")  # Daily reward
        await asyncio.sleep(0.5)

        # Check claim rights
        await check_claim_rights(client, channel)

    async def check_claim_rights(client, channel):
        log_function(f"[{client.user}] Checking claim rights...", preset_name)
        while True:
            await channel.send(f"{mudae_prefix}mu")  # Check Mudae claim status
            await asyncio.sleep(1)

            try:
                async for msg in channel.history(limit=1):
                    if msg.author.id == TARGET_BOT_ID:
                        if "right now" in msg.content.lower(): 
                            match = re.search(r"The next claim reset is in \*\*(\d+h)?\s*(\d+)\*\* min\.", msg.content)
                            if match:
                                hours = int(match.group(1)[:-1]) if match.group(1) else 0
                                minutes = int(match.group(2))
                                remaining_seconds = (hours * 60 + minutes) * 60

                                if remaining_seconds <= 3600:  # Check if less than 1 hour
                                    log_function(f"[{client.user}] Claim right available and less than 1 hour remaining.", preset_name)
                                    await check_rolls_left(client, channel, ignore_limit=True) # Send the ignore_limit flag
                                else:
                                    log_function(f"[{client.user}] Claim right available. Applying claim limit.", preset_name)
                                    await check_rolls_left(client, channel)
                            
                                return

                            else:
                                log_function(f"[{client.user}] Couldn't extract time from message.")
                                return
                        elif "you can't claim" in msg.content.lower():
                            log_function(f"[{client.user}] Claim right not available.", preset_name)

                            # Extract the waiting time
                            match = re.search(r"you can't claim for another \*\*(\d+h)?\s*(\d+)\*\* min\.", msg.content)
                            if match:
                                hours = int(match.group(1)[:-1]) if match.group(1) else 0
                                minutes = int(match.group(2))
                                total_seconds = (hours * 60 + minutes) * 60
                            
                                log_function(f"[{client.user}] Claim right not available. Will retry in {hours} hours {minutes} minutes.", preset_name)
                                await display_time(total_seconds + delay_seconds, log_function, preset_name)
                                await asyncio.sleep(total_seconds + delay_seconds)

                            else:
                                log_function(f"[{client.user}] Waiting time not found. Retrying in 1 hour.", preset_name)
                                await display_time(3600 + delay_seconds, log_function, preset_name)
                                await asyncio.sleep(3600 + delay_seconds)

                            # Retry claim rights after the waiting period
                            await check_claim_rights(client, channel)
                            return


                        else:
                            log_function(f"[{client.user}] Claim right check failed. Retrying in 5 seconds.", preset_name)
                            await asyncio.sleep(5)  # Wait for 5 seconds
            
            except Exception as e:
                log_function(f"[{client.user}] Error: {e}", preset_name)

        await asyncio.sleep(60 + delay_seconds) 


    async def check_rolls_left(client, channel, ignore_limit=False):
        await channel.send(f"{mudae_prefix}ru")  # Check remaining rolls

        try:
            start_time = time.time()
            async for msg in channel.history(limit=1):
                if msg.author.id == TARGET_BOT_ID and "rolls" in msg.content.lower():
                    matches = re.findall(r"\d+", msg.content)
                    if len(matches) >= 2:
                        rolls_left = int(matches[0])
                        reset_minutes = int(matches[1])
                        if rolls_left == 0:
                            log_function(f"[{client.user}] No rolls left.", preset_name)
                            await display_time(reset_minutes * 60 + delay_seconds, log_function, preset_name)
                            await asyncio.sleep(reset_minutes * 60 + delay_seconds)
                            await check_claim_rights(client, channel)
                            return
                        else:
                            log_function(f"[{client.user}] Rolls left: {rolls_left}", preset_name)
                            await start_roll_commands(client, channel, rolls_left, ignore_limit)
                            return
            
            if time.time() - start_time > 5:
                log_function(f"[{client.user}] No roll message received within 5 seconds. Resending ru command.", preset_name)
                await check_rolls_left(client, channel)

        except Exception as e:
            log_function(f"[{client.user}] Error while checking rolls: {e}", preset_name)
            await check_claim_rights(client, channel) # Proceed to claim check regardless of error

    async def start_roll_commands(client, channel, rolls_left, ignore_limit=False):
        for _ in range(rolls_left):
            await channel.send(f"{mudae_prefix}{roll_command}")  # Send roll command
            await asyncio.sleep(0.3)

        await asyncio.sleep(3)
        
        await check_new_characters(client, channel)

        mudae_messages = []
        async for msg in channel.history(limit=rolls_left * 2, oldest_first=False):  # Daha fazla mesajı kontrol et
            if msg.author.id == TARGET_BOT_ID:
                mudae_messages.append(msg)

        # Tüm roll mesajlarını işle
        await handle_mudae_messages(client, channel, mudae_messages, ignore_limit)

        await asyncio.sleep(3)
        await check_claim_rights(client, channel)

    async def handle_mudae_messages(client, channel, mudae_messages, ignore_limit=False):
        # En düşük claim'li karakter ve Kakera mesajlarını bul
        lowest_claim_character = None
        lowest_claim_character_message = None
        lowest_claim_kakera = None
        lowest_claim_kakera_message = None

        for msg in mudae_messages:
            if msg.embeds:
                embed = msg.embeds[0]

                # Kakera butonları varsa önce onları işle
                if msg.components:
                    for component in msg.components:
                        for button in component.children:
                            if button.emoji and button.emoji.name in ['kakeraY', 'kakeraT', 'kakeraG', 'kakera', 'kakeraO', 'kakeraR', 'kakeraW', 'kakeraL']:
                                await button.click()
                                log_function(f"[{client.user}] Claimed Kakera: {msg.embeds[0].author.name}", preset_name)
                                log_list.append(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Claimed Kakera: {msg.embeds[0].author.name}")
                                await asyncio.sleep(3)

                # Renklere göre claim limiti kontrol et ve en düşük claim'li mesajları bul
                if embed.color.value in [16751916, 1360437]:  # Normal karakter renkleri
                    # Claim sayısını al
                    match = re.search(r"Claims: \#(\d+)", embed.description)
                    if match:
                        claims_value = int(match.group(1))

                        # En düşük claim sayısını takip et ve claim limitini kontrol et
                        if (not lowest_claim_character or claims_value < lowest_claim_character) and (ignore_limit or claims_value < claim_limit):
                            lowest_claim_character = claims_value
                            lowest_claim_character_message = msg
                else:  # Kakera mesajı
                    # Claim sayısını al (Kakera mesajlarında farklı bir formatta olabilir)
                    match = re.search(r"\*\*(\d+)\*\*", embed.description)
                    if match:
                        claims_value = int(match.group(1))

                        # En düşük claim sayısını takip et
                        if not lowest_claim_kakera or claims_value < lowest_claim_kakera:
                            lowest_claim_kakera = claims_value
                            lowest_claim_kakera_message = msg

        # En düşük claim'li karakteri claim et
        if lowest_claim_character_message:
            await claim_character(client, channel, lowest_claim_character_message)

        # En düşük claim'li Kakerayı claim et
        if lowest_claim_kakera_message:
            await claim_character(client, channel, lowest_claim_kakera_message, is_kakera=True)


    async def claim_character(client, channel, msg, is_kakera=False):
        log_message = "Claimed Kakera" if is_kakera else "Claimed Character"
        # Claim butonu varsa tıkla, yoksa reaksiyon ekle
        if msg.components:
            for component in msg.components:
                for button in component.children:
                    if button.emoji and button.emoji.name in ['💖', '💗', '💘', '❤️', '💓', '💕', '♥️', '🪐']:
                        await button.click()
                        log_function(f"[{client.user}] {log_message}: {msg.embeds[0].author.name}", preset_name)
                        log_list.append(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {log_message}: {msg.embeds[0].author.name}")
                        await asyncio.sleep(3)
                        return
        else:
            await msg.add_reaction("✅")
            log_function(f"[{client.user}] {log_message}: {msg.embeds[0].author.name}", preset_name)
            log_list.append(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {log_message}: {msg.embeds[0].author.name}")
            await asyncio.sleep(3)


    async def check_new_characters(client, channel):
        # Check for new characters in the channel history
        async for msg in channel.history(limit=15):
            if msg.author.id == TARGET_BOT_ID:
                if msg.embeds:
                    embed = msg.embeds[0]
                    match = re.search(r"Claims: \#(\d+)", embed.description)
                    if match:
                        claims_value = int(match.group(1))
                        log_function(f"[{client.user}] New character: {embed.author.name} (Claims: #{claims_value})", preset_name)

    async def display_time(seconds, log_function, preset_name):
        # Calculate and display the retry time
        now = datetime.datetime.now()
        retry_time = now + datetime.timedelta(seconds=seconds)
        formatted_time = retry_time.strftime("%H:%M")
        log_function(f"[{client.user}] Retry time: {formatted_time}", preset_name)

    client.run(token)


def print_log(message, preset_name):
    print(f"[{preset_name}] {message}")


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

    threading.Thread(target=run_bot, args=(preset["token"], preset["prefix"],
                                             preset["channel_id"], preset["roll_command"],
                                             preset["claim_limit"], preset["delay_seconds"],
                                             preset["mudae_prefix"], print_log, selected_preset)).start()


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
        preset = presets[preset_name]  # Doğru preset adını kullan
        threading.Thread(target=run_bot, args=(preset["token"], preset["prefix"],
                                                 preset["channel_id"], preset["roll_command"],
                                                 preset["claim_limit"], preset["delay_seconds"],
                                                 preset["mudae_prefix"], print_log, preset_name)).start()


if __name__ == "__main__":
    main_menu()
