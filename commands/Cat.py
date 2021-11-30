from discord.ext import commands

class Cats(commands.Cog):
    """ Talk like a cat """
    
    def __init__(self, bot):
        self.bot = bot

   
    @commands.command(name = 'cat',help="Gatos.")
    async def get_random_image(self, ctx, msg):
        msg = str(msg).replace(' ', '%20')
        url_image = f'https://cataas.com/cat/says/{msg}'
        await ctx.send(url_image)

def setup(bot):
    bot.add_cog(Cats(bot))
