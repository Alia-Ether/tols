#│-----------------------------------------------------------│
#│  Link: t.me/FrontendVSCode                 │ 
#│  Author: Frontend & LED (𝙰𝚕𝚒𝚊 𝙴𝚝𝚑𝚎𝚛 𖤍) 🌷 │ 
#│  lang: python                              │
#│  [VS-HASH-01] ΞΩ77Λβ99PPHD8A71             │ 
#│  build:3.10.15                             │ 
#│-----------------------------------------------------------│




from faker import Faker
fake = Faker()

def run():
    print("1 IP | 2 Email | 3 Имя | 4 Пароль")
    c = input("> ")
    if c == "1": print(fake.ipv4())
    if c == "2": print(fake.email())
    if c == "3": print(fake.name())
    if c == "4": print(fake.password())
    input("Enter...")