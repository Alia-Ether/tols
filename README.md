
![Realme Banner](Realme.png)


├── tols 
      ├── Realme.png
      ├── __pycache__
      ├── audio_recorder.py 
      ├── auth.json
      ├── auth.py
      ├── cpuinfo.py
      ├── device.py
      ├── doc_filler.py
      ├── excel_handler.py
      ├── files
      ├── generators.py
      ├── github_info.py
      ├── logger.py
      ├── main.py
      ├── monitor.py
      ├── photo
      ├── photo_sorter.py
      ├── realme.md
      ├── snake_game.py
      └── sorted_photo







1️⃣ Директории и файлы

Модуль	Основная директория / путь	Файлы	Особенности

photo_sorter.py	./photo (входные) → ./sorted_photo (выходные)	фото .jpg, .jpeg, .png	Авто создаются папки по годам; если нет фото — милое сообщение
doc_filler.py	./files	template.docx → filled_contract.docx	Можно менять слова в data словаре; шаблон нужен обязательно
audio_recorder.py	текущая папка ./	mic_record.wav	Использует Termux API; путь можно менять; если API недоступно — вывод милого предупреждения
excel_handler.py	текущая папка ./	sales.xlsx → filtered_sales.xlsx, summary_by_manager.xlsx	Фильтрация по сумме и дате; автосоздание файлов, если не существует
github_info.py	—	—	Запрос к GitHub API по username без @; выводит имя, репозитории, followers, company
snake_game.py	—	—	Консольная игра на curses; символ змейки и еды можно менять
monitor.py / generators.py / cpuinfo.py / device.py	—	—	Служебные модули, интегрируются через меню
auth.py / logger.py	—	—	Логин и логирование действий


2️⃣ Возможности изменения слов и сообщений
В doc_filler.py можно менять словарь data → любые плейсхолдеры в шаблоне.
В photo_sorter.py можно менять сообщение при переносе/ошибке.
В audio_recorder.py можно менять название файла mic_record.wav.
В excel_handler.py можно менять фильтры (сумма, дата) и названия выходных файлов.
Все милые эмодзи и сообщения можно менять на свои, чтобы софт был «живым» 💖.


3️⃣ Структура меню (main.py)

Меню полностью готово для интеграции всех модулей.
Новые функции добавляются только через импорты и вызовы функций, менять main.py почти не нужно.
Каждое действие через меню выводит милое сообщение с эмодзи 💗, чтобы софт был дружелюбным.


пароль: { 123 }
