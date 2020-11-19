import os
import discord
from discord.ext import commands
from google_speech import Speech

class audio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(usage="", description="Entrar audio.")
    async def join(self, ctx):
        voice_channel = ctx.message.author.voice.channel

        if voice_channel != None:
            await voice_channel.connect()
        else:
            await ctx.send(ctx.author.mention + " não está en nenhum canal de áudio")

    @commands.command(usage="texto", description="Tocar audio.")
    async def play(self, ctx, *arg):
        if ctx.author.voice.channel and ctx.author.voice.channel == ctx.voice_client.channel:
            ffmpegExecutable = os.getenv("ffmpeg")

            text = " ".join(arg[:])
            lang = "pt"

            speech = Speech(text, lang)
            speech.save("output.mp3")

            ctx.voice_client.play(discord.FFmpegPCMAudio("output.mp3", executable=ffmpegExecutable))
        else:
            await ctx.send(ctx.author.mention + " não está en nenhum canal de áudio ou não está no mesmo canal")

    @commands.command(usage="", description="Sair audio.")
    async def leave(self, ctx):
        if ctx.author.voice.channel and ctx.author.voice.channel == ctx.voice_client.channel:
            await ctx.voice_client.disconnect()
            await ctx.message.add_reaction(emoji="👋")
        else:
            await ctx.send(ctx.author.mention + " não está en nenhum canal de áudio ou não está no mesmo canal")