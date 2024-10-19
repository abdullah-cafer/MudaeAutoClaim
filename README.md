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

1. **Install Python 3.8+:** Make sure you have Python 3.8 or higher installed on your system.
2. **Install Dependencies:**
   ```bash
   pip install discord.py-self inquirer
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

1. **Obtain Tokens:** Paste this into the console in the discord window in the browser to access the token: ``` window.webpackChunkdiscord_app.push([
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
console.log(`%cYou now have your token in the clipboard!`, 'font-size: 16px'); ```
2. **Configure `presets.json`:** Fill in the `presets.json` file with the bot tokens, channel IDs, and other settings for each account.
3. **Run the Script:** Execute `python mudae_bot.py` to start the bot.
4. **Select Presets:** Choose the presets you want to run from the terminal menu.
5. **Monitor Logs:** Observe the console output for claimed characters and other events.


## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues if you find bugs or have suggestions for improvements.
