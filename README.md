## Простой клиент для перессылки сообщений

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

# Запуск клиента
- python3 main.py