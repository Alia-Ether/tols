#│-----------------------------------------------------------│
#│  Link: t.me/FrontendVSCode                 │ 
#│  Author: Frontend & LED (𝙰𝚕𝚒𝚊 𝙴𝚝𝚑𝚎𝚛 𖤍) 🌷 │ 
#│  lang: python                              │
#│  [VS-HASH-01] ΞΩ77Λβ99PPHD8A71             │ 
#│  build:3.10.15                             │ 
#│-----------------------------------------------------------│



import os
from pathlib import Path

def main():
    output_file = Path("./mic_record.wav")
    duration = 10
    if os.system("which termux-microphone-record > /dev/null 2>&1") != 0:
        print("🍎 Установите termux-microphone-record: pkg install termux-api")
        return

    print(f"🎙 Запись {duration} секунд...")
    # Запись прямо в текущую папку
    os.system(f"termux-microphone-record -f {output_file} -l {duration}")

    if output_file.exists():
        print(f"✅ Запись завершена: {output_file.resolve()}")
    else:
        print("😟 Мило: Termux API пока недоступно, файл создать не удалось 🌸")

if __name__ == "__main__":
    main()