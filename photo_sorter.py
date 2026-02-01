#│-----------------------------------------------------------│
#│  Link: t.me/FrontendVSCode                 │ 
#│  Author: Frontend & LED (𝙰𝚕𝚒𝚊 𝙴𝚝𝚑𝚎𝚛 𖤍) 🌷 │ 
#│  lang: python                              │
#│  [VS-HASH-01] ΞΩ77Λβ99PPHD8A71             │ 
#│  build:3.10.15                             │ 
#│-----------------------------------------------------------│


import os
import shutil
from pathlib import Path
from PIL import Image, UnidentifiedImageError

PHOTO_FOLDER = os.path.abspath("photo")
RESULT_FOLDER = os.path.abspath("sorted_photo")
PHOTO_FORMATS = (".jpg", ".jpeg", ".png")


def get_year(file_path):
    try:
        image = Image.open(file_path)
        exifdata = image.getexif()
        date = exifdata.get(306)
        image.close()
        if date:
            return date[:4]
    except UnidentifiedImageError:
        pass
    return None


def move_photo(photo_path, year_dir):
    name = os.path.basename(photo_path)
    target = os.path.join(year_dir, name)

    if not os.path.exists(target):
        print(f'✅ {name} → {year_dir}')
        shutil.move(photo_path, year_dir)
    else:
        print(f'⛔ {name} уже существует')


def scan(cur):
    found = False

    for item in os.listdir(cur):
        path = os.path.join(cur, item)

        if os.path.isdir(path):
            if scan(path):
                found = True

        elif Path(path).suffix.lower() in PHOTO_FORMATS:
            year = get_year(path)
            if year:
                year_dir = os.path.join(RESULT_FOLDER, year)
                os.makedirs(year_dir, exist_ok=True)
                move_photo(path, year_dir)
                found = True

    return found


def remove_empty(cur):
    for item in os.listdir(cur):
        path = os.path.join(cur, item)
        if os.path.isdir(path):
            remove_empty(path)
            if not os.listdir(path):
                os.rmdir(path)


def main():
    if not os.path.exists(PHOTO_FOLDER):
        print("🍎 Извините, у вас нет изображений в этой директории 🥺")
        print(f"📂 Ожидалась папка: {PHOTO_FOLDER}")
        return

    os.makedirs(RESULT_FOLDER, exist_ok=True)

    found = scan(PHOTO_FOLDER)

    if not found:
        print("🍎 Извините, у вас нет изображений в этой директории 🥺")
        return

    remove_empty(PHOTO_FOLDER)
    print("🌸 Сортировка завершена успешно! 💗")


if __name__ == "__main__":
    main()