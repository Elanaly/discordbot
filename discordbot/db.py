#-------------------------------------------------------------------------------
# Name:        discordbot
#
# reference:
# https://qiita.com/sizumita/items/cafd00fe3e114d834ce3
# Author:      dra
#
# Created:     19/11/2020
# Copyright:   (c) dra 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import discord
import random
import ffmpeg
client = discord.Client()


haire = "呼ぶ前にボイスチャンネル入れよ"

@client.event

async def on_ready():
    print("on_ready")
    print(discord.__version__)

@client.event
async def on_message(message):

    if message.author.bot:
        return
    if message.content == "tasukete":

        await message.channel.send("これがコマンド一覧だ")
        await message.channel.send(file=discord.File("コマンド一覧.txt"))
    #bot入室
    if message.content == "omaenodebanda":
        if message.author.voice is None:
            await message.channel.send(haire)
            return

        await message.author.voice.channel.connect()

        await message.channel.send("待たせたな")

    #bot退出
    elif message.content == "kaere":
        if message.author.voice is None:
            await message.channel.send("haire")
            return
        await message.guild.voice_client.disconnect()

        await message.channel.send("じゃあな")

    if message.content == "ohiruni":
        message.guild.voice_client.play(discord.FFmpegPCMAudio("ohiru.mp3"))

    elif message.content == "d1":
        message.guild.voice_client.play(discord.FFmpegPCMAudio("d1.mp3"))

    elif message.content == "d2":
        message.guild.voice_client.play(discord.FFmpegPCMAudio("d2.mp3"))

    elif message.content == "cobweb":
        message.guild.voice_client.play(discord.FFmpegPCMAudio("cobweb.mp3"))

    elif message.content == "route2":
        message.guild.voice_client.play(discord.FFmpegPCMAudio("route2.mp3"))

    elif message.content == "vpen1":
        message.guild.voice_client.play(discord.FFmpegPCMAudio("vpen1.mp3"))

    elif message.content == "vpen2":
        message.guild.voice_client.play(discord.FFmpegPCMAudio("vpen2.mp3"))

    elif message.content == "vpen3":
        message.guild.voice_client.play(discord.FFmpegPCMAudio("vpen3.mp3"))

    elif message.content == "rip":
        message.guild.voice_client.play(discord.FFmpegPCMAudio("rip.mp3"))

    elif message.content == "lala1":
        message.guild.voice_client.play(discord.FFmpegPCMAudio("lala1.mp3"))

    elif message.content == "kakke1":
        message.guild.voice_client.play(discord.FFmpegPCMAudio("kakke1.mp3"))


client.run("Nzc4ODMwNDIxNzc3MTg2ODE2.X7XsWg.f0JIkE0Hy_ucJ76pdi3IYkUXqcU")
