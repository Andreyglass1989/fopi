# -*- coding: utf-8 -*-
import telebot
import constant
import sqlite3
import os

chats = []
conn = sqlite3.connect('../db.sqlite3')
bd = conn.cursor()
bd.execute('SELECT * FROM users;')
# bd.execute('SELECT chat_id FROM users;')
for b in bd:
	print(b)
	ch = {"chat_id": int(b[3]), "status": int(b[-1])}
	chats.append(ch)
# print()

#chats = [355503529]#, 185106322, 198735333]

bot = telebot.TeleBot(constant.token)

for c in chats:
	if c["status"] == 1:
		message = 'Присоединяйтесь к нашему официальному каналу чтобы быть в курсе последних новостей! '
		message1 = ''
		directory = "/home/toshiba/django/fopi/telbot/image"
		file_in_directory = os.listdir(directory)
		# print(file_in_directory)
		try:
			# for z in file_in_directory:
				# img = open(directory + '/' + z, 'rb')
				# bot.send_chat_action(c, 'upload_photo')
				# bot.send_photo(c, img, caption="Друзья мои, вы готовы к большой тренировке? )))")
				# img.close()
				# bot.send_message(c, message1) 
			print(c)
			bot.send_message(c["chat_id"], message) 
		except telebot.apihelper.ApiTelegramException:
			# pass
			bd.execute('UPDATE users SET status={} WHERE chat_id={}'.format(0, c["chat_id"]))
bd.close()
conn.commit()
conn.close()
			# t = bd.fetchall()
			# print(t)






# https://api.telegram.org/bot5576706434:AAF782BFiSmp6MlJzMLKw9g3gcTar90Pc-c/sendMessage?chat_id=355503529&text=Hello