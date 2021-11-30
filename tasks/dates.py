import datetime

from discord.ext import commands, tasks


class Dates(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.current_time.start()

    @tasks.loop(minutes=60) #Defina de quantos em quantos minutos essa task deve ser executada
    async def current_time(self):
        ...
        now = datetime.datetime.now()

        now = now.strftime("%d/%m/%Y às %H:%M:%S")

        channel = self.bot.get_channel() #Inserir o id do canal que deseja enviar a hora atual

        await channel.send(now)


def setup(bot):
    bot.add_cog(Dates(bot))
