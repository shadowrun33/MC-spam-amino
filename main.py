import aminofix
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
client = aminofix.Client()
client.login(email=email, password=password)

print("Успешный вход/Login succeded")

com = client.sub_clients()
for name, comId in zip(com.name, com.comId):
    print(f"{name} - {comId}")

comId = int(input("Id сообщества/Community Id > "))

subclient = aminofix.SubClient(comId = comId, profile = client.profile)

chat = subclient.get_chat_threads(start = 0, size = 100)
for title, chatId in zip(chat.title, chat.chatId):
    print(f"{title} - {chatId}")

print("\nВведите айди чатов по одному, нажмите 0 для продолжения/Choose chats, press 0 to continue.")

while chatId != str(0):
    chatId = str(input("==> "))
    thread_Ids.append(chatId)
thread_Ids.sort()
thread_Ids.remove('0')

messageType = int(input("Тип сообщений/Message type > "))
message = str(input("Сообщение/Message > "))

while True:
    for chatId in thread_Ids:
        threads_lists.append(list(Thread(target = subclient.send_message, args=(chatId, message, messageType)) for x in range(100)))
    for i in range(len(threads_lists)):
        for j in range(len(threads_lists[i])):
            threads_lists[i][j].start()
    threads_lists.clear()