import discord, os
from discord.ext import commands
from audio import *
from text import *

bot = commands.Bot(command_prefix='%')

class main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Logged on as", bot.user)
        await bot.change_presence(activity=discord.Game(name="Personagem todos pq personagem é bom :)"))

    @commands.Cog.listener()
    async def on_command(self, ctx):
        a = ("-"*110 + "\nUsuário: " + ctx.message.author.name + "#" + str(ctx.message.author.discriminator) + " (id=" + str(ctx.message.author.id) + ")" + "\n" 
            + "Server: " + str(ctx.message.guild) + "\n" 
            + "Canal: " + str(ctx.message.channel) + "\n"
            + "Comando: " + ctx.message.content + "\n")
        
        print(a)

        with open("LOG.txt","a",encoding="utf8") as log:
            log.write(a)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send("**ERRO:** " + str(error))

bot.add_cog(main(bot))
bot.add_cog(text(bot))
bot.add_cog(audio(bot))

token = os.getenv('DISCTOKEN')

bot.run(token)