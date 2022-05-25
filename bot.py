from http import client
import discord
from discord.ext import commands
import time
import asyncio

bot = commands.Bot(command_prefix='!')
TOKEN = "Твой токен"


@bot.event
async def on_ready():
    print('connected')




@bot.command(pass_context=True)
#@commands.has_permissions(administrator=True) нужна что бы команды распростронялмсь абсолютно на всех
@bot.event
async def mtm(ctx): #Перемещает всех на канал и мутит, кроме тебя
    for channel in ctx.guild.voice_channels:
        for member in channel.members:
            await member.move_to(ctx.author.voice.channel)
            await member.edit(mute=True)

@bot.command(pass_context=True)
#@commands.has_permissions(administrator=True)
@bot.event
async def mta(ctx, time_sleep): #Перемещает всех на канал и мутит, кроме тебя и через указанное время размучивает все. Вводится с аргументом, в качестве аргумента принимает целое число - это количество секунд через которое все размутятся
    for channel in ctx.guild.voice_channels:
        for member in channel.members:
            await member.move_to(ctx.author.voice.channel)
            await member.edit(mute=True)

    await asyncio.sleep(int(time_sleep))                
    for channel in ctx.guild.voice_channels:
        for member in channel.members:
            await member.edit(mute=False)

@bot.command(pass_context=True) 
#@commands.has_permissions(administrator=True)
@bot.event
async def mte(ctx): #Unmute all
    for channel in ctx.guild.voice_channels:
        for member in channel.members:
                await member.edit(mute=False)

@bot.command(pass_context=True) 
#@commands.has_permissions(administrator=True)              
@bot.event
async def mts(ctx): #Mute all
    for channel in ctx.guild.voice_channels:
        for member in channel.members:
                await member.edit(mute=True)

bot.run(TOKEN)    



