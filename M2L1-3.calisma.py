import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True  # Botun mesaj içeriğine erişimini aktif hale getiriyoruz.

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def mem(ctx):
    try:
        # 'images' klasöründeki tüm dosyaların listesini alıyoruz.
        files = os.listdir('images')
        if not files:  # Eğer klasör boşsa kullanıcıya bilgi veriyoruz.
            await ctx.send("Resim klasörü boş!")
            return
        
        # Rastgele bir dosya seçiyoruz.
        img_name = random.choice(files)
        
        # Dosyayı açıp kullanıcıya gönderiyoruz.
        with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    except FileNotFoundError:
        await ctx.send("Resim klasörü bulunamadı! Lütfen 'images' klasörünün mevcut olduğundan emin olun.")
    except Exception as e:
        await ctx.send(f"Bir hata oluştu: {e}")

bot.run("token")
