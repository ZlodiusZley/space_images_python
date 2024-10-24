import telegram
import os
import random
import time

folder = 'images'
send_time = 4

tg_token = '6937143904:AAGIRJtbhxjtPqI8aZj_AVVGIicaJ2SNTkw'
tg_chat_id = '5162389967'


bot = telegram.Bot(token=tg_token)


while True:
       all_files = []
       for root, _, files in os.walk(folder):
           all_files.extend([os.path.join(root, file) for file in files])
       
       if not all_files:
              print(f'Папка {folder} не содержит файлов.')
              break

       random_file = random.choice(all_files)
       with open(random_file, 'rb') as file:
              bot.send_document(chat_id=tg_chat_id, document=file)
       time.sleep(send_time)
