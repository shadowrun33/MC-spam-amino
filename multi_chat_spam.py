import AminoLab #library by https://github.com/LilZevi 
import pyfiglet
from colorama import init, Fore, Back, Style
from threading import Thread
thread_Ids = []
threads_lists = []

init()
print(Back.BLACK)
print(Fore.YELLOW)

print(pyfiglet.figlet_format("mc spam", font="big"))
print("         ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
print("         ┃by shadowrun                   ")
print("         ┃https://github.com/shadowrun33/")
print("         ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
email = str(input("Почта/Email > "))
password = str(input("Пароль/Password > "))
client = AminoLab.Client()
client.auth(email=email, password=password)

print("Успешный вход/Login succeded")

com = client.my_communities()
for name, ndc_Id in zip(com.name, com.ndc_Id):
    print(f"{name} - {ndc_Id}")

ndc_Id = int(input("Id сообщества/Community Id > "))

chat = client.my_chat_threads(ndc_Id = ndc_Id, size = 100)
for title, thread_Id in zip(chat.title, chat.thread_Id):
    print(f"{title} - {thread_Id}")

print("\nВведите айди чатов по одному, нажмите 0 для продолжения/Choose chats, press 0 to continue.")

while thread_Id != str(0):
    thread_Id = str(input("==> "))
    thread_Ids.append(thread_Id)
thread_Ids.sort()
thread_Ids.remove('0')

message_type = int(input("Тип сообщений/Message type > "))
message = str(input("Сообщение/Message > "))

while True:
    for i in thread_Ids:
        threads_lists.append(list(Thread(target = client.send_message, args=(ndc_Id, i, message, message_type)) for x in range(100)))
    print("spamming")
    for i in range(len(threads_lists)):
        for j in range(len(threads_lists[i])):
            threads_lists[i][j].start()
    threads_lists.clear()
    

   




    




