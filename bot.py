import discord
import sys
import os
from discord.ext import commands
bot = commands.Bot(command_prefix=commands.when_mentioned_or('.'),description="Ghost's new Discord bot! \n\nHelp Commands:",owner_id=231028316843278346)

@bot.command()
async def testing(ctx):
  """kkkkk"""
  await ctx.send("testing...")

@bot.command()
async def ping(ctx):
    """Gets the bot latency. Pong!"""
    color = discord.Color(value=0x00ff00)
    em = discord.Embed(color=color, title='Pong! My latency is:')
    em.description = f"{bot.latency * 1000:.4f} ms"
    await ctx.send(embed=em)

bot.run(os.environ.get('TOKEN'))
