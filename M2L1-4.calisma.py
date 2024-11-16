import discord  # Discord API'si ile iletişim kurmak için kullanılan kütüphane
from discord.ext import commands  # Komut tabanlı bot oluşturmak için framework
import requests  # HTTP isteklerini yapmak için kullanılan kütüphane

# Discord botunun mesaj içeriğine erişmesini sağlamak için gerekli izinleri ayarlıyoruz.
intents = discord.Intents.default()
intents.message_content = True

# Botun komut ön ekini belirliyoruz ($) ve izinleri aktarıyoruz.
bot = commands.Bot(command_prefix='$', intents=intents)

# Botun Discord'a başarıyla bağlandığını kontrol etmek için bir olay tanımlıyoruz.
@bot.event
async def on_ready():
    # Botun başarıyla çalıştığını ve giriş yaptığını terminalde yazdırır.
    print(f'{bot.user} olarak giriş yaptık')

# Rastgele bir ördek resminin URL'sini almak için bir fonksiyon tanımlıyoruz.
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'  # Ördek resimlerinin URL'sini sağlayan API
    res = requests.get(url)  # API'ye HTTP GET isteği gönderiyoruz
    data = res.json()  # Gelen yanıtı JSON formatına dönüştürüyoruz
    return data['url']  # JSON yanıtından resim URL'sini alıp döndürüyoruz

# Duck komutu tanımlanıyor: Kullanıcı $duck yazdığında tetiklenecek
@bot.command('duck')
async def duck(ctx):
    '''
    $duck komutunu çağırdığımızda, get_duck_image_url fonksiyonu çalışır ve bir rastgele ördek resmi URL'si döndürür.
    Bot, bu URL'yi Discord kanalına gönderir.
    '''
    image_url = get_duck_image_url()  # Ördek resminin URL'sini alıyoruz
    await ctx.send(image_url)  # Ördek resminin URL'sini Discord kanalına gönderiyoruz

# Botun Discord tokeni ile çalıştırılmasını sağlıyoruz.
bot.run("token")
