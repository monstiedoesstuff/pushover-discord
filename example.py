import discord
import asyncio
from discord.ext import commands
from pushover import init, Client

# Your Pushover API token and user key
PUSHOVER_API_TOKEN = 'your_pushover_api_token'
PUSHOVER_USER_KEY = 'your_pushover_user_key'

# Your Discord bot token
DISCORD_BOT_TOKEN = 'your_discord_bot_token'

# Initialize Pushover
init(PUSHOVER_API_TOKEN)

# Create a Discord client
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix='!', intents=intents)

# Function to send a Pushover notification
def send_pushover_notification(message):
    client = Client(PUSHOVER_USER_KEY)
    client.send_message(message)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

    # Send a Pushover notification when the bot comes online
    send_pushover_notification(f'{bot.user.name} is now online.'
# Run the bot
bot.run(DISCORD_BOT_TOKEN)
