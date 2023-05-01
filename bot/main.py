import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")

@bot.command(name="register")
async def test(ctx, username: str):
	# Check if user already exists
    # ...

    # If user doesn't exist, create a new account
    # ...

    # Send confirmation message
    await ctx.send(f"Registered user {username}!")

bot.run(os.getenv("DISCORD_BOT_TOKEN"))
