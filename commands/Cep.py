from discord.ext import commands
import requests

class Cep(commands.Cog):
    """ Talks with user """
    
    def __init__(self, bot):
        self.bot = bot

   
    @commands.command(name = 'cep',help="Verifica os dados de um CEP Brasileiro")
    async def consult_cep(self, ctx, cep):
        #viacep.com.br/ws/cep/json/
        try:
            if len(cep)>8 or len(cep)<8:
                await ctx.send(f'CEP inválido')
            else:
                response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
                data = response.json()
                localidade = data.get('localidade')
                bairro = data.get('bairro')
                logradouro = data.get('logradouro')
                complemento = data.get('complemento')
                await ctx.send(f'Localidade:{localidade}\nBairro:{bairro}\nLogradouro:{logradouro}\nComplemento: {complemento}')
        except:
            await ctx.send('Algo inesperado aconteceu...')

def setup(bot):
    bot.add_cog(Cep(bot))
