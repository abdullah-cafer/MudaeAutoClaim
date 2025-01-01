# Mudae Auto-Claim Bot

This Python-based Discord bot automates the process of claiming characters from the popular Mudae bot. It allows you to configure and manage multiple Discord accounts, set preferences for claims, and monitor activity.

**IMPORTANT WARNING:** This bot operates as a self-bot, which **violates Discord's Terms of Service**. Using self-bots can lead to the suspension or permanent termination of your Discord account. **You are solely responsible for any consequences resulting from using this bot. Proceed with extreme caution and at your own risk.**

## Key Features

*   **Multi-Account Management:** Run multiple bot instances, each with its own unique configuration.
*   **Configurable Claim Preferences:** Define minimum `kakera` values and claim limits, influencing claim decisions.
*   **Intelligent Automation:** Automatically handles roll commands, claim checks, and roll resets for continuous operation.
*   **Customizable Delays:** Set delays between actions to avoid rate limits and appear more human-like.
*  **Key Mode:** Enable or disable key mode to adjust if the bot will roll only for kakera while the claim is not available.
*   **Simple JSON Configuration:** Easily configure all bot settings via a `presets.json` file.
*   **Real-time Console Monitoring:** View bot activity and statuses in the console in real-time.
*   **Detailed Logging:** Keep track of claimed characters and other events with detailed logging.

## Installation

1.  **Install Python 3.8+:** Make sure you have Python 3.8 or a newer version installed.
2.  **Install Required Libraries:**
    ```bash
    pip install discord.py-self inquirer
    ```
3.  **Configure Presets:**
    Create a `presets.json` file with your desired settings. Here's the structure:
    ```json
    {
      "preset1": {
        "token": "YOUR_BOT_TOKEN",
        "prefix": "!",
        "channel_id": 1234567890,
        "roll_command": "wa",
        "delay_seconds": 1,
        "mudae_prefix": "$",
        "min_kakera": 50,
        "key_mode": false
      },
      "preset2": { ... }
    }
    ```
    *   **`token`**:  Your Discord account's bot token (see "Usage" for how to obtain)
    *   **`prefix`**:  The command prefix for the bot (e.g. `!`)
    *   **`channel_id`**: The Discord channel ID where you want the bot to operate
    *   **`roll_command`**: The Mudae command to use (e.g. `wa`, `wg`, etc.)
    *   **`delay_seconds`**: Delay between actions (in seconds)
    *   **`mudae_prefix`**: The Mudae bot command prefix (usually `$`)
    *   **`min_kakera`**: The minimum kakera value to consider for character claiming.
    *   **`key_mode`**: True or False. If true it will continue rolling only for kakera while the claim is not available
4.  **Run the script:**
    ```bash
    python mudae_bot.py
    ```
5.  **Follow the terminal prompts** to choose which presets to run.

## Usage

1.  **Get Your Account Token:** Open Discord in your browser, and paste the following JavaScript code into the browser's developer console. **Be very cautious with your token, as it gives full access to your account.**
 ```

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
 
2.  **Configure `presets.json`:** Fill the file using the bot tokens, channel IDs, roll commands, and other settings for each account. You can also set `min_kakera` to influence claiming.
3.  **Run the Script:** Execute `python mudae_bot.py` to start the bot.
4.  **Select Presets:** Choose the presets you want to run from the terminal menu.
5.  **Monitor:** The console will show you the real-time status of your bots.
6.  **Check Logs:** A detailed history is available in the `logs.txt` file.

 

## Contributing

Contributions are welcome! If you find bugs, have ideas for improvements, or want to contribute code, please submit pull requests or open issues.
