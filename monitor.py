#│-----------------------------------------------------------│
#│  Link: t.me/FrontendVSCode                 │ 
#│  Author: Frontend & LED (𝙰𝚕𝚒𝚊 𝙴𝚝𝚑𝚎𝚛 𖤍) 🌷 │ 
#│  lang: python                              │
#│  [VS-HASH-01] ΞΩ77Λβ99PPHD8A71             │ 
#│  build:3.10.15                             │ 
#│-----------------------------------------------------------│


import os
import re
import psutil
import requests
import http.server
import socketserver
import socket
from colorama import Fore, init
init(autoreset=True)

def bar(value, maxv=100, size=20):
    fill = int(size * value / maxv)
    return "█" * fill + "░" * (size - fill)


def parse_getprop(file_path):
    props = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                match = re.match(r"\[(.*?)\]: \[(.*?)\]", line)
                if match:
                    key, value = match.groups()
                    props[key] = value
    return props

def display_info(props):
    print(Fore.MAGENTA + "📱 Модель и прошивка")
    print(f"  🏭 Производитель SoC: {props.get('ro.vendor.soc.manufacturer','Unknown')}")
    print(f"  💻 Модель SoC: {props.get('ro.vendor.soc.model','Unknown')}")
    print(f"  🆔 Кодовое имя телефона: {props.get('ro.vendor.build.fingerprint','Unknown')}")
    print(f"  🛠 Версия прошивки: {props.get('ro.vendor.build.version.incremental','Unknown')}")
    print(f"  📅 Дата сборки: {props.get('ro.vendor.build.date','Unknown')}")
    print(f"  ⚙️ Тип сборки: {props.get('ro.vendor.build.type','Unknown')}\n")

    print("🖥 Процессор и архитектура")
    print(f"  🧠 CPU поддержка: {props.get('ro.vendor.product.cpu.abilist','None')}")
    print(f"  🔢 Поддержка 32-бит: {props.get('ro.vendor.product.cpu.abilist32','None')}")
    print(f"  🔢 Поддержка 64-бит: {props.get('ro.vendor.product.cpu.abilist64','None')}\n")

    print("📡 Связь и SIM")
    print(f"  📶 LTE поддержка: {props.get('ro.vendor.mtk_md1_support','Unknown')}")
    print(f"  📞 CDMA поддержка: {props.get('ro.vendor.mtk_md3_support','Unknown')}")
    print(f"  💳 SIM карты: {props.get('vendor.gsm.ril.uicctype','Unknown')}")
    print(f"  🌐 Сети: {props.get('ro.vendor.mtk_protocol1_rat_config','Unknown')}\n")

    print("📸 Камеры")
    print(f"  📷 Основная камера: {props.get('vendor.camera.sensor.rearMain.fuseID','None')}")
    print(f"  🤳 Фронтальная камера: {props.get('vendor.camera.sensor.f.fuseID','None')}")
    print(f"  📷 Макро камера: {props.get('vendor.camera.sensor.rearMacro.fuseID','None')}\n")

    print("⚙️ Система и Android")
    print(f"  📱 Версия Android: {props.get('ro.vendor.build.version.release','Unknown')}")
    print(f"  🔢 SDK: {props.get('ro.vendor.build.version.sdk','Unknown')}")
    print(f"  🔄 Zygote: {props.get('ro.zygote','Unknown')}\n")

    print("💾 Память и хранилище")
    print(f"  📦 Общая память: {props.get('ro.vendor.md_apps.load_gencfg','Unknown')}")
    print(f"  💽 DRAM макс: {props.get('ro.vendor.mtk_config_max_dram_size','Unknown')}\n")

    print("🔋 Батарея и питание")
    print(f"  🔋 Статус батареи: {props.get('sys.battery.status','Unknown')}")
    print(f"  ⚡ Уровень заряда: {props.get('sys.battery.level','Unknown')}\n")

    print("📡 Сети и датчики")
    print(f"  📶 Wi-Fi: {props.get('vendor.wlan.driver.version','Unknown')} / {props.get('vendor.wlan.firmware.version','Unknown')}")
    print(f"  🔊 Bluetooth: {props.get('vendor.connsys.bt_fw_ver','Unknown')}")
    print(f"  📡 GPS поддержка: {props.get('ro.vendor.mtk_gps_support','Unknown')}\n")

def auto_getprop():
    file_path = "getprop.txt"
    try:
        os.system(f"getprop > {file_path}")
        props = parse_getprop(file_path)
        display_info(props)
    except Exception as e:
        print("❌ Ошибка при создании getprop:", e)
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

def ip_info():
    import time
    while True:
        try:
            ip_response = requests.get("https://api64.ipify.org?format=json")
            ip_response.raise_for_status()
            ip = ip_response.json()["ip"]

            geo_response = requests.get(f"https://ipapi.co/{ip}/json/")
            geo_response.raise_for_status()
            geo_data = geo_response.json()

            print(Fore.CYAN + "\n📡 Информация о вашем IP:")
            print(f"IP: {geo_data.get('ip')}")
            print(f"Версия IP: {geo_data.get('version')}")
            print(f"Страна: {geo_data.get('country_name')} ({geo_data.get('country_code')})")
            print(f"Регион: {geo_data.get('region')}")
            print(f"Город: {geo_data.get('city')}")
            print(f"Почтовый индекс: {geo_data.get('postal')}")
            print(f"Координаты: {geo_data.get('latitude')}, {geo_data.get('longitude')}")
            print(f"Часовой пояс: {geo_data.get('timezone')}")
            print(f"Организация (ISP): {geo_data.get('org')}")
            print(f"ASN: {geo_data.get('asn')}")
            print(f"Континент: {geo_data.get('continent_code')}")
            print(f"EU: {geo_data.get('in_eu')}")
            print(f"Телефонный код страны: +{geo_data.get('country_calling_code')}")
            print(f"Валюта: {geo_data.get('currency')} ({geo_data.get('currency_name')})")
            print(f"Языки: {geo_data.get('languages')}")
            print(f"Google Maps: https://www.google.com/maps?q={geo_data.get('latitude')},{geo_data.get('longitude')}\n")
        except Exception as e:
            print("❌ Ошибка получения IP:", e)
        again = input("💖 Хотите проверить IP снова? (y/n): ").strip().lower()
        if again != 'y':
            break


suspicious_keywords = ["record", "spy", "sniff", "keylog", "debug", "wireshark", "obs", "screen", "capture", "hook"]

def suspicious_processes():
    found = []
    for proc in psutil.process_iter(['name']):
        try:
            name = proc.info['name'].lower()
            if any(keyword in name for keyword in suspicious_keywords):
                found.append(name)
        except:
            pass
    print(Fore.RED + "⚠️ Подозрительные процессы:" if found else Fore.GREEN + "✅ Подозрительных процессов нет")
    for p in found:
        print(" -", p)
    print()


def file_server(default_port=8000):
  
    directory = os.getcwd()
    print(Fore.GREEN + f"💗 Раздаём файлы из: {directory}")

    
    def is_port_free(port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('0.0.0.0', port)) != 0

    while True:
        try:
            port_input = input(f"Порт сервера (по умолчанию {default_port}): ").strip()
            port = int(port_input) if port_input else default_port
        except:
            print("❌ Некорректный ввод, используем порт по умолчанию")
            port = default_port

        if not is_port_free(port):
            print(Fore.RED + f"❌ Порт {port} занят, попробуйте другой")
            continue
        break

    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=directory, **kwargs)

    try:
        with socketserver.TCPServer(("", port), Handler) as httpd:
            ip = socket.gethostbyname(socket.gethostname())
            print(Fore.CYAN + f"\n🌍 Файловый сервер запущен: http://{ip}:{port}")
            print(Fore.YELLOW + "💡 Нажмите Ctrl+C, чтобы остановить сервер и вернуться в меню")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n💗 Сервер остановлен и порт освобождён")
    except Exception as e:
        print("❌ Ошибка сервера:", e)




def monitor():
    while True:
        os.system("clear")
        print(Fore.MAGENTA + "💗 Панель софта 💗")
        print("1. Модель и прошивка")
        print("2. Информация о IP")
        print("3. Проверка подозрительных процессов")
        print("4. Файловый сервер")
        print("q. Выход")
        choice = input("\nВыберите опцию: ").strip().lower()
        if choice == "1":
            auto_getprop()
        elif choice == "2":
            ip_info()
        elif choice == "3":
            suspicious_processes()
        elif choice == "4":
            file_server()
        elif choice == "q":
            break
        input(Fore.MAGENTA + "\nНажмите Enter для возврата в меню...")
