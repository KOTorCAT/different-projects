# Shrek

## Black & White AI Chat Experience

---

### О проекте

**Shrek Luxury Edition** — это веб-приложение на Django, позволяющее пользователям вести диалог с персонажем Шрек из вселенной DreamWorks. Проект сочетает минималистичный черно-белый дизайн.

Интерфейс выполнен в монохромной гамме с использованием элегантных шрифтов Montserrat и Cormorant Garamond. Диалоги с Шреком генерируются через GigaChat API от Сбера, что обеспечивает естественное общение с сохранением характера персонажа — грубоватого, но мудрого огра с болотным юмором и философскими метафорами.

---

### Функциональные возможности

- **Диалог с ИИ** — общение со Шреком на русском языке в его уникальной манере
- **Два режима чата** — мини-чат на главной странице и полноэкранный режим для развернутых бесед
- **Контекст диалога** — сохранение истории последних сообщений в сессии пользователя
- **Асинхронная отправка** — сообщения отправляются без перезагрузки страницы через AJAX
- **Адаптивный дизайн** — корректное отображение на всех типах устройств
- **Индикатор набора текста** — визуальная обратная связь при генерации ответа
- **Очистка истории** — возможность начать диалог заново

---

### Технологический стек

| Компонент | Технология | Версия |
|-----------|------------|--------|
| Backend | Django | 6.0.4 |
| База данных | PostgreSQL | 16 |
| AI API | GigaChat (Сбер) | API v2 |
| HTTP клиент | Requests | 2.32.3 |
| Переменные окружения | python-dotenv | 1.0.1 |
| Frontend | HTML5 / CSS3 / JavaScript | — |

---

### Требования к окружению

- Python 3.12 или выше
- PostgreSQL 16
- Аккаунт на платформе GigaChat (developers.sber.ru)
---

### Установка и запуск

#### 1. Клонирование репозитория
#### 2. Создание виртуального окружения

```bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
# venv\Scripts\activate         # Windows
```

#### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

#### 4. Настройка базы данных PostgreSQL

```bash
sudo -u postgres psql
```

```sql
CREATE DATABASE mydatabase;
CREATE USER myuser WITH PASSWORD 'mypassword';
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
ALTER USER myuser WITH SUPERUSER;
\q
```

#### 5. Настройка переменных окружения

Создайте файл `.env` в корне проекта:

```env
GIGACHAT_API_KEY=your_api_key_here
GIGACHAT_CLIENT_ID=your_client_id_here
GIGACHAT_SCOPE=GIGACHAT_API_PERS
```

**Где взять ключи:**
- Зарегистрируйтесь на [developers.sber.ru](https://developers.sber.ru/)
- Создайте проект в разделе GigaChat
- Скопируйте API-ключ и Client ID

#### 6. Применение миграций

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 7. Сбор статических файлов

```bash
python manage.py collectstatic
```

#### 8. Запуск сервера разработки

```bash
python manage.py runserver
```

Перейдите по адресу: `http://127.0.0.1:8000`

---

### Структура проекта

```
myproject/
├── .env                           # Переменные окружения (не в Git)
├── .gitignore                     # Игнорируемые файлы
├── manage.py                      # Утилита управления Django
├── requirements.txt               # Зависимости проекта
├── myapp/
│   ├── views.py                   # Контроллеры
│   ├── gigachat_client.py         # Клиент GigaChat API
│   ├── static/myapp/
│   │   ├── css/style.css          # Основные стили
│   │   └── js/main.js             # Клиентская логика
│   └── templates/myapp/
│       ├── home.html              # Главная страница
│       ├── about.html             # О персонаже
│       ├── chat.html              # Полноэкранный чат
│       └── item_detail.html       # Детальные страницы
└── myproject/
    ├── settings.py                # Конфигурация Django
    └── urls.py                    # Маршрутизация
```

---

### API эндпоинты

| Метод | URL | Назначение |
|-------|-----|-------------|
| GET | `/` | Главная страница |
| GET | `/about/` | Информация о Шреке |
| GET | `/chat/` | Полноэкранный чат |
| POST | `/chat/api/` | Отправка сообщения Шреку |
| POST | `/chat/clear/` | Очистка истории диалога |
| GET | `/item/<int:item_id>/` | Детальная страница |

