# Mudae Auto-Claim Bot

This Python-based Discord bot automates the process of claiming characters in the popular Mudae bot. It allows you to configure multiple accounts, set claim limits, and customize delays to maximize your chances of collecting your favorite waifus and husbandos.

## Features

* **Multi-Account Support:** Manage and run multiple bot accounts with individual settings.
* **Configurable Claim Limits:** Set a maximum claim limit for each account to target rarer characters.
* **Automatic Roll Resetting:** Handles roll resets and claim right checks to ensure continuous claiming.
* **Customizable Delays:** Adjust delays between actions to avoid rate limits and mimic human behavior.
* **Easy Configuration:** Use a simple `presets.json` file to define settings for each bot account.
* **Detailed Logging:** Logs claimed characters and other events for monitoring and analysis.

## Installation

1. **Install Python 3.7+:** Make sure you have Python 3.7 or higher installed on your system.
2. **Install Dependencies:**
   ```bash
   pip install discord.py inquirer
   ```
3. **Configure Presets:**
   Create a `presets.json` file with the following structure:
   ```json
   {
     "preset1": {
       "token": "YOUR_BOT_TOKEN",
       "prefix": "!", 
       "channel_id": 1234567890,
       "roll_command": "wa",
       "claim_limit": 5,
       "delay_seconds": 1,
       "mudae_prefix": "$" 
     },
     "preset2": { ... } 
   }
   ```
4. **Run the script:**
   ```bash
   python mudae_bot.py 
   ```
5. **Follow the prompts in the terminal to select and run the desired presets.**


## Usage

1. **Create Discord Bot Accounts:** Create Discord bot accounts for each server where you want to use the bot.
2. **Obtain Bot Tokens:** Get the bot tokens for each account from the Discord Developer Portal.
3. **Configure `presets.json`:** Fill in the `presets.json` file with the bot tokens, channel IDs, and other settings for each account.
4. **Run the Script:** Execute `python mudae_bot.py` to start the bot.
5. **Select Presets:** Choose the presets you want to run from the terminal menu.
6. **Monitor Logs:** Observe the console output for claimed characters and other events.


## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues if you find bugs or have suggestions for improvements.
