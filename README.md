## Простой клиент для перессылки сообщений
Две реализации по работе с апи telegram, пакет telethon и pygram
# Требования
- python3

# Установка зависимостей
- pip3 install -r requirements.txt

# Настройка
- Здесь https://telegram.org/ создаем приложение и достаем api_id, api_hash. 
Указываем в .env переменные:
- user_tag=<например @test_user> указываем тэг куда хотим пересылать сообщения.
- api_id=<ваш api_id>
- api_hash=<ваш api_hash>

# Запуск клиента на telethon
- python3 src/client_telethon/main.py

# Запуск клиента на pygram
- python3 src/client_pygram/main.py