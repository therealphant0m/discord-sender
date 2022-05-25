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
		message = input(': ')

		if(message == 's!embed'): # эмбед
			title = input('Введите заголовок: ')
			description = input('Введите описание: ')
			footer = input('Введите футер: ')

			embed = discord.Embed(title = title, description = description).set_footer(text = footer)

			await bot.get_channel(int(channel_id)).send(embed = embed)
			continue

		if(message == 's!file'): # отправить файл
			filename = input('Введите путь к файлу: ')

			await bot.get_channel(int(channel_id)).send(file = discord.File(filename))
			continue

		if(message == 's!help'):
			print('\nСписок команд:\n')
			print('s!embed - Отправить Embed\ns!file - Отправить файл\ns!help - Выводит это сообщение')
			continue

		await bot.get_channel(int(channel_id)).send(message)

bot.run(token)