import discord
from discord.ext import commands
import random
import asyncio
from google_speech import Speech

bot = commands.Bot(command_prefix='%')

class tudo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Logged on as", bot.user)
        await bot.change_presence(activity=discord.Game(name="Personagem todos pq personagem é bom :)"))

    @commands.Cog.listener()
    async def on_command(self,ctx):
        log = open("LOG.txt","a",encoding="utf8")

        a = ("-"*110 + "\nUsuário: " + ctx.message.author.name + "#" + str(ctx.message.author.discriminator) + " (id=" + str(ctx.message.author.id) + ")" + "\n" 
            + "Server: " + str(ctx.message.guild) + "\n" 
            + "Canal: " + str(ctx.message.channel) + "\n"
            + "Comando: " + ctx.message.content + "\n")
        
        print(a)
        log.write(a)  

        log.close()

    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        await ctx.send("**ERRO:** " + str(error))

    @bot.event
    async def on_member_join(member):
        channel = bot.get_channel(464298877823221763)
        await channel.send(f"{member.mention} welcome")

    @commands.command(usage="", description="Ver o ping do bot.")
    async def ping(self,ctx):
        await ctx.trigger_typing()

        embed = discord.Embed(title="pong", color=0xff0000)
        await ctx.send(embed=embed)

    @commands.command(usage="pedra/papel/tesoura", description="Jogar pedra papel tesoura com o bot.")
    async def PPT(self, ctx, arg):
        await ctx.trigger_typing()

        choices = ["pedra","papel","tesoura"]
        arg = arg.lower()

        if arg not in choices:
            await ctx.send("Você deve jogar:\n\t-pedra\n\t-papel\n\t-tesoura")
            return

        ind = random.choice(choices)

        a = ""

        if ind == arg:
            a = "Empatou :|"
        elif ind == "pedra" and arg == "tesoura" or ind == "tesoura" and arg == "papel" or ind == "papel" and arg == "pedra":
            a = "Ganhei :)"
        else:
            a = "Perdi :("

        await ctx.send("Joguei **" + ind + "**\n" + a)

    @commands.command(usage="", description="Recebe um biscoito da melhor personagem.")
    async def biscoito(self,ctx):
        await ctx.trigger_typing()

        await ctx.send("Para " + ctx.author.mention,file=discord.File("naoto.jpg"))
    
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
            text = " ".join(arg[:])
            lang = "pt"

            speech = Speech(text, lang)
            speech.save("output.mp3")

            ctx.voice_client.play(discord.FFmpegPCMAudio("output.mp3"))
        else:
            await ctx.send(ctx.author.mention + " não está en nenhum canal de áudio ou não está no mesmo canal")

    @commands.command(usage="", description="Sair audio.")
    async def leave(self, ctx):
        if ctx.author.voice.channel and ctx.author.voice.channel == ctx.voice_client.channel:
            await ctx.voice_client.disconnect()
            await ctx.message.add_reaction(emoji="👋")
        else:
            await ctx.send(ctx.author.mention + " não está en nenhum canal de áudio ou não está no mesmo canal")

    @commands.command(usage="", description="Ajuda.")
    async def help(self, ctx):
        await ctx.trigger_typing()

        message = ""

        commands = self.get_commands()

        for c in commands:
            message += "***%" + c.name + "*** " + c.usage + ": " +  c.description + "\n\n"

        embed = discord.Embed(title="HELP", color=0x00ffff)
        embed.add_field(name= "Comandos: ", value=message)

        await ctx.send(embed=embed)


bot.remove_command('help')
bot.add_cog(tudo(bot))

token = ""

with open("token.txt", "r") as f:
    token = f.readline()

bot.run(token)
