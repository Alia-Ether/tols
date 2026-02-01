#│-----------------------------------------------------------│
#│  Link: t.me/FrontendVSCode                 │ 
#│  Author: Frontend & LED (𝙰𝚕𝚒𝚊 𝙴𝚝𝚑𝚎𝚛 𖤍) 🌷 │ 
#│  lang: python                              │
#│  [VS-HASH-01] ΞΩ77Λβ99PPHD8A71             │ 
#│  build:3.10.15                             │ 
#│-----------------------------------------------------------│


from audio_recorder import main as record_audio
from excel_handler import main as handle_excel
from photo_sorter import main as sort_photos
from github_info import main as github_info
from doc_filler import main as fill_doc
from snake_game import main as snake_game
from monitor import monitor
from colorama import init, Fore, Style
init(autoreset=True)

from auth import login, change_password
from monitor import monitor
from generators import run as generators
from cpuinfo import detect_cpu
from device import device_info
from logger import log
import os
import pyfiglet


def clear():
    os.system("clear")

def print_banner():
    banner = pyfiglet.figlet_format("Frontend & Led", font="slant")
    print(Fore.MAGENTA + banner)
    print(Fore.CYAN + Style.BRIGHT + "💗 Добро пожаловать до Frontend & Led 💗\n")

def main():
    clear()
    print_banner()
    
    if not login():
        return

    log("Вход выполнен")

    while True:
        clear()
        print_banner()
        print(Fore.MAGENTA + """
1 • Мониторинг + графики
2 • Генераторы
3 • CPU big.LITTLE
4 • Инфо устройства
5 • Сменить пароль
6 • Сортировка фото
7 • Заполнение Word
8 • Запись аудио
9 • Обработка Excel
10 • GitHub информация
11 • Игра Змейка
12 • Выход
""")
        c = input("> ")

        if c == "1":
            log("Мониторинг")
            monitor()
        elif c == "2":
            generators()
        elif c == "3":
            print(detect_cpu())
            input("Enter...")
        elif c == "4":
            for k, v in device_info().items():
                print(f"{k}: {v}")
            input("Enter...")
        elif c == "5":
            change_password()
        elif c == "6":
            log("Сортировка фото")
            sort_photos()
            input("Enter...")
        elif c == "7":
            log("Заполнение Word")
            fill_doc()
            input("Enter...")
        elif c == "8":
            log("Запись аудио")
            record_audio()
            input("Enter...")
        elif c == "9":
            log("Обработка Excel")
            handle_excel()
            input("Enter...")
        elif c == "10":
            log("GitHub информация")
            github_info()
            input("Enter...")
        elif c == "11":
            log("Игра Змейка")
            snake_game()
        elif c == "12":
            log("Выход")
            break

if __name__ == "__main__":
    main()