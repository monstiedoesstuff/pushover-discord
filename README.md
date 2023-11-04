# Discord Bot with Pushover Notifications

This is a Python-based Discord bot that sends notifications via Pushover when it goes online and when it encounters errors. Additionally, it includes a command to send custom Pushover notifications.

## Requirements

- Python 3.6 or higher
- [discord.py](https://github.com/Rapptz/discord.py) library
- [python-pushover](https://github.com/Thibauth/python-pushover) library
- A Discord bot token
- A Pushover API token and user key

## Configuration

1. Install the required Python libraries:
   ```
   pip install discord.py python-pushover
   ```

2. Replace the following placeholders in the code with your actual tokens:
   - `PUSHOVER_API_TOKEN`: Your Pushover API token.
   - `PUSHOVER_USER_KEY`: Your Pushover user key.
   - `DISCORD_BOT_TOKEN`: Your Discord bot token.

## Running the Bot

1. Run the Python script:

   ```
   python your_bot_script.py
   ```

2. The bot will log in as the specified Discord bot and will send a Pushover notification when it goes online.

## Troubleshooting

- If Pushover notifications are not working, double-check your API tokens, Pushover account settings, and library installations.
- Check the console for any error messages or exceptions.
