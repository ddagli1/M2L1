import discord
# Discord botları için komut tabanlı bir framework sağlar. 
# Bu framework sayesinde, botumuzun belirli komutlara yanıt vermesini kolayca tanımlayabiliriz.
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True # botun mesaj içeriğine erişimini aktif hale getiriyoruz.

bot = commands.Bot(command_prefix='$', intents=intents)
#Bu özellik, botun kendisine gönderilen komutları tanıması için bir ön ek tanımlar.
#  $ işareti komut ön eki olarak belirlenmiştir. Yani bot sadece $ ile başlayan komutlara yanıt verir.

@bot.event # bot belirli bir olay gerçekleştiğinde tetiklensin.
async def on_ready(): # bot başarılı bir şekilde Discord'a bağlandığında tetiklenir
    print(f'{bot.user} olarak giriş yaptık')


@bot.command()
async def mem(ctx):
    with open('images/mem2.png', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
  
bot.run("token")
