from vk import *
from pyfiglet import Figlet
import random, vk, time
import os
import sys
import shutil
import traceback

os.system('clear') 
f = Figlet(font='ascii___')

def DrawText(text,center=True):
    if center:
      print(*[x.center(shutil.get_terminal_size().columns) for x in f.renderText(text).split("\n")],sep="\n")  
    else:
      print(f.renderText(text))

DrawText('666',center=True)
print("\033[35m{}\033[0m".format("\nДанный скрипт написал darknesss666🦋."))

tg = input("\033[33m{}\033[0m".format("Хочешь добавить автора скрипта в друзья в ВК? [y/n]"))
if tg == "y":
    os.system("termux-open-url 'https://vk.com/i_am_sorry_but_my_life_is_shit'")
    print("\033[32m{}\033[0m".format("Правда, я лучший?<3"))
    TOKEN = input("\033[33m{}\033[0m".format("🔐Введи токен kate_mobile: "))
    user_id = input("\033[33m{}\033[0m".format("🔆Введи айди страницы: "))
    posts_id = input("\033[33m{}\033[0m".format("🔆Введи айди поста: "))
    msgs = input("\033[33m{}\033[0m".format("🔆Введи комментарий накрутки: "))
    print("\033[1;33m{}\033[0m".format("Чтобы остановить скрипт нажми ctrl + c + enter."))
    session = vk.Session(access_token=TOKEN)
    apivk = vk.API(session, v = 5.95)
elif tg == "n":
    print("\033[31m{}\033[0m".format("Ну не хочешь, как хочешь(("))
    TOKEN = input("\033[33m{}\033[0m".format("🔐Введи токен kate_mobile: "))
    user_id = input("\033[33m{}\033[0m".format("🔆Введи айди страницы: "))
    posts_id = input("\033[33m{}\033[0m".format("🔆Введи айди поста: "))
    msgs = input("\033[33m{}\033[0m".format("🔆Введи комментарий накрутки: "))
    print("\033[1;33m{}\033[0m".format("Чтобы остановить скрипт нажми ctrl + c + enter.")) 
    session = vk.Session(access_token=TOKEN)
    apivk = vk.API(session, v = 5.95)
while True:
    try:
        apivk.wall.createComment(owner_id=user_id, post_id=posts_id, message=msgs, guid=random.randint(0, 9999999999))
        print(time.strftime("\033[36m[%d.%m.%Y|%H:%M:%S]", time.localtime()), "1 комм был отправлен.")
    except:
        traceback.print_exc() 
    time.sleep(3)