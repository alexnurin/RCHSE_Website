# Курсовая работа: сайт для Ролевого Клуба ВШЭ <br>

<img width="1320" alt="image" src="https://github.com/alexnurin/RCHSE_Website/assets/44980361/cea6b9ff-8b7a-4eb1-b745-5732e241f0f3">

## Инструкция по развёртыванию сервера:
1. Установить репозиторий с помощью ```git clone https://github.com/alexnurin/RCHSE_Website```
2. Установить python3, включая pip3 (pip для windows)
3. Установить зависимости, выполнив ```pip3 install -r RCHSE_Website/requirements.txt``` из корневой папки репозитория (та, где расположен manage.py)
4. Добавить файл с секретными ключами в папку config. Например ```cat recieved_file.txt > RCHSE_Website/config/secrets.py```
5. Запустить локальный сервер командой ```python3 RCHSE_Website/manage.py runserver```
6. Сервер будет доступен по адресу http://127.0.0.1:8000/
