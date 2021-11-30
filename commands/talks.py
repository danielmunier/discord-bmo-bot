from discord.ext import commands
import discord


class Talks(commands.Cog):
    """Talks with user"""

    def __init__(self, bot):
        self.bot = bot

 
    @commands.command(name="oi", help="Oi :)")
    async def send_hello(self, ctx):

        response = f"Oi, {ctx.author.name}. Tudo bem?"

        await ctx.send(response)

    @commands.command(
        name="secret", help="Envia um segredo no privado"
    )
    async def secret(self, ctx):
        try:
            await ctx.author.send("Comando secreto!")
            await ctx.author.send("Não conte pra ninguém!")

        except discord.errors.Forbidden:
            await ctx.send(
                "Habilite o recebimento de mensagens para qualquer pessoa do servidor (Opções > Privacidade)"
            )


def setup(bot):
    bot.add_cog(Talks(bot))
