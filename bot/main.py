import discord
from discord.ext import commands
import os
import asyncio
from utils.config import Config

Config.check_required()
intents = discord.Intents.default()
bot = commands.Bot(
    command_prefix='!',
    intents=intents,
    integration_types=[
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install
    ]
)
bot.remove_command('help')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to use this command.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing required argument.")
    else:
        await ctx.send(f"An error occurred: {str(error)}")
        print(f"Error: {error}")

async def load_cogs():
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'commands.{filename[:-3]}')
                print(f'Loaded command: {filename}')
            except Exception as e:
                print(f'Failed to load command {filename}: {e}')

    for filename in os.listdir('./events'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'events.{filename[:-3]}')
                print(f'Loaded event: {filename}')
            except Exception as e:
                print(f'Failed to load event {filename}: {e}')

async def main():
    async with bot:
        await load_cogs()
        await bot.start(Config.DISCORD_TOKEN)

if __name__ == '__main__':
    asyncio.run(main())