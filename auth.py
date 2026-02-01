#│-----------------------------------------------------------│
#│  Link: t.me/FrontendVSCode                 │ 
#│  Author: Frontend & LED (𝙰𝚕𝚒𝚊 𝙴𝚝𝚑𝚎𝚛 𖤍) 🌷 │ 
#│  lang: python                              │
#│  [VS-HASH-01] ΞΩ77Λβ99PPHD8A71             │ 
#│  build:3.10.15                             │ 
#│-----------------------------------------------------------│




import hashlib
import json
import os
from colorama import Fore

CONF = "auth.json"


def _hash(p):
    return hashlib.sha256(p.encode()).hexdigest()


def _load():
    if not os.path.exists(CONF):
        with open(CONF, "w") as f:
            json.dump({"hash": _hash("8585")}, f)
    return json.load(open(CONF))


def login():
    data = _load()
    for _ in range(3):
        pwd = input(Fore.MAGENTA + "🔐 Пароль: ")
        print(Fore.CYAN + "SHA256:", _hash(pwd)[:12], "...")
        if _hash(pwd) == data["hash"]:
            print(Fore.GREEN + "✅ Вход успешен")
            return True
        print(Fore.RED + "❌ Неверно")
    return False


def change_password():
    data = _load()
    old = input("Старый пароль: ")
    if _hash(old) != data["hash"]:
        print("❌ Неверно")
        return
    new = input("Новый пароль: ")
    data["hash"] = _hash(new)
    json.dump(data, open(CONF, "w"))
    print("✅ Пароль обновлён")