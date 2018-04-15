import discord
import sys
import os
from discord.ext import commands
bot = commands.Bot(command_prefix=commands.when_mentioned_or('.'),description="Ghost's new Discord bot! \n\nHelp Commands:",owner_id=231028316843278346)

@bot.command()
async def testing(ctx):
  await ctx.say("testing...")

bot.run(os.environ.get('TOKEN'))
