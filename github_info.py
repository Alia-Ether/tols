#│-----------------------------------------------------------│
#│  Link: t.me/FrontendVSCode                 │ 
#│  Author: Frontend & LED (𝙰𝚕𝚒𝚊 𝙴𝚝𝚑𝚎𝚛 𖤍) 🌷 │ 
#│  lang: python                              │
#│  [VS-HASH-01] ΞΩ77Λβ99PPHD8A71             │ 
#│  build:3.10.15                             │ 
#│-----------------------------------------------------------│


import requests
from datetime import datetime


def main():
    username = input("🐙 Введите GitHub username: ").strip()
    if not username:
        print("⚠️ Имя пользователя не указано")
        input("Enter...")
        return

    try:
        r = requests.get(f"https://api.github.com/users/{username}", timeout=10)

        if r.status_code == 404:
            print("❌ Пользователь не найден")
            input("Enter...")
            return

        r.raise_for_status()
        user = r.json()

        created = datetime.strptime(
            user["created_at"], "%Y-%m-%dT%H:%M:%SZ"
        ).strftime("%d.%m.%Y")

        print("\n💙 GitHub профиль")
        print(f"👤 Username: {user.get('login')}")
        print(f"🏢 Company: {user.get('company') or '—'}")
        print(f"🌐 Blog: {user.get('blog') or '—'}")
        print(f"📧 Email: {user.get('email') or '—'}")
        print(f"📅 Account created: {created}")
        print(f"📦 Public repos: {user.get('public_repos')}")
        print(f"⭐ Followers: {user.get('followers')}")
        print(f"🔁 Following: {user.get('following')}")
        print(f"🔗 Profile: {user.get('html_url')}")

    except requests.exceptions.RequestException as e:
        print("❌ Ошибка сети:", e)
    except Exception as e:
        print("❌ Ошибка:", e)

    input("\nEnter...")


if __name__ == "__main__":
    main()