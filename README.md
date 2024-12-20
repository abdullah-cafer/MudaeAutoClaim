# Mudae Auto-Claim

This Python-based Discord bot automates the process of claiming characters in the popular Mudae bot. It allows you to configure multiple accounts, set claim preferences, and monitor their activity in real-time.

**SERIOUS WARNING:** This bot is a self-bot and its use violates Discord's Terms of Service. Using self-bots can lead to the suspension or permanent termination of your Discord account. **You are solely responsible for any consequences resulting from the use of this bot. Proceed with extreme caution and at your own risk.**

## Key Features

* **Multi-Account Management:** Run and manage multiple bot instances with individual configurations.
* **Configurable Claim Preferences:** Define claim limits and now, influence claiming based on kakera value (in-game currency).
* **Intelligent Automation:** Automatically handles roll commands, claim right checks, and roll resets for continuous operation.
* **Customizable Delays:** Set delays between actions to help avoid rate limits and appear more human-like.
* **Simple JSON Configuration:**  Configure all bot settings easily through a `presets.json` file.
* **Real-time Console Monitoring:** View a live, updating table in your console showing the status, recent activity, and next refresh times for each bot instance. Navigate between bots using the `k` and `l` keys.
* **Detailed Logging:**  Comprehensive logging of claimed characters and other events, saved to `logs.txt`. Errors are clearly highlighted in the console.
* **Improved Error Handling:**  More robust handling of Discord errors and communication issues for increased reliability.

## Installation

1. **Install Python 3.8+:** Ensure you have Python 3.8 or a later version installed on your system.
2. **Install Dependencies:**
   ```bash
   pip install discord.py-self inquirer rich keyboard
   ```
3. **Configure Presets:**
   Create a `presets.json` file with the following structure. You can now also specify a `min_kakera` value:
   ```json
   {
     "preset1": {
       "token": "YOUR_BOT_TOKEN",
       "prefix": "!",
       "channel_id": 1234567890,
       "roll_command": "wa",
       "claim_limit": 5,
       "delay_seconds": 1,
       "mudae_prefix": "$",
       "min_kakera": 50
     },
     "preset2": { ... }
   }
   ```
4. **Run the script:**
   ```bash
   python mudae_bot.py
   ```
5. **Follow the prompts in the terminal to select and run the desired presets.** You will now see a live status table updating in your console.

## Usage

1. **Obtain Tokens:** Paste this code into the console within your Discord browser window to get your account token (use with caution and understand the risks):
   ```javascript
   window.webpackChunkdiscord_app.push([
     [Math.random()],
     {},
     req => {
       if (!req.c) return;
       for (const m of Object.keys(req.c)
         .map(x => req.c[x].exports)
         .filter(x => x)) {
         if (m.default && m.default.getToken !== undefined) {
           return copy(m.default.getToken());
         }
         if (m.getToken !== undefined) {
           return copy(m.getToken());
         }
       }
     },
   ]);
   console.log('%cWorked!', 'font-size: 50px');
   console.log(`%cYou now have your token in the clipboard!`, 'font-size: 16px');
   ```
2. **Configure `presets.json`:**  Fill in the `presets.json` file with the bot tokens, channel IDs, roll commands, claim limits, and other settings for each account. You can now optionally set `min_kakera` to influence claim decisions.
3. **Run the Script:** Execute `python mudae_bot.py` to start the bot.
4. **Select Presets:** Choose the presets you want to run from the terminal menu.
5. **Monitor the Live Status:** Observe the real-time status of your bots in the console. Use the `k` key to go to the previous page and the `l` key to go to the next page if you are running multiple bots.
6. **Check Logs:** For a detailed history, review the `logs.txt` file.

## Contributing

Contributions are welcome! If you find bugs, have suggestions for improvements, or want to contribute code, feel free to submit pull requests or open issues.
