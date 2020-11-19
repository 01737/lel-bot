import random
import discord
from discord.ext import commands
from getHello import *

class text(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(usage="", description="Ver o ping do bot.")
    async def ping(self,ctx):
        await ctx.trigger_typing()

        embed = discord.Embed(title="pong", color=0xff0000)
        await ctx.send(embed=embed)

    @commands.command(usage="(pedra ou papel ou tesoura)", description="Jogar pedra papel tesoura com o bot.")
    async def PPT(self, ctx, arg):
        await ctx.trigger_typing()

        choices = ["pedra","papel","tesoura"]
        arg = arg.lower()

        if arg not in choices:
            await ctx.send("Você deve jogar:\n\t-pedra\n\t-papel\n\t-tesoura")
            return

        choice = random.choice(choices)

        a = ""

        if choice == arg: a = "Empatou :|"
        elif choice == "pedra" and arg == "tesoura" or choice == "tesoura" and arg == "papel" or choice == "papel" and arg == "pedra":
            a = "Ganhei :)"
        else: a = "Perdi :("

        await ctx.send("Joguei **" + choice + "**\n" + a)

    @commands.command(usage="", description="Recebe um biscoito da melhor personagem.")
    async def biscoito(self, ctx):
        await ctx.trigger_typing()

        await ctx.send("Para " + ctx.author.mention,file=discord.File("naoto.jpg"))

    @commands.command(usage="linguagem", description="Escreve um programa Hello World em qualquer linguagem (pelo menos os que estão no repo https://github.com/leachim6/hello-world)")
    async def hello(self, ctx, lang):
        await ctx.trigger_typing()

        helloReq = HelloWorld()
        helloText = helloReq.print_hello(lang)

        embed = discord.Embed(title=f"Hello World em {lang}", color=0x9200d6)
        embed.add_field(name=helloText[1], value=f"```{helloText[0]}```")

        await ctx.send(embed=embed)