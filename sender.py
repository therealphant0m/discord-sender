import discord, os
from discord.ext import commands

if not os.path.exists('token.txt'): # первый запуск
	with open('token.txt', 'w') as f:
		f.write(input('Введите токен бота (это сообщение появится только один раз): '))
		f.close()

with open('token.txt') as f: # чтение токена
	token = f.read()
	f.close()

channel_id = input('ID канала: ')

bot = commands.Bot(command_prefix = 's!')

@bot.event
async def on_ready(): # отправка сообщения в канал, который находится по айди
	while True:
		await bot.get_channel(int(channel_id)).send(input(': '))

bot.run(token)