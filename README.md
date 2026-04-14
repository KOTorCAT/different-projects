# Shrek Luxury Edition — AI Chat with the Ogre

![Django](https://img.shields.io/badge/Django-6.0.4-092E20?style=for-the-badge&logo=django)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?style=for-the-badge&logo=postgresql)
![GigaChat](https://img.shields.io/badge/GigaChat-API-005A9C?style=for-the-badge&logo=sberbank)
![License](https://img.shields.io/badge/License-MIT-FF69B4?style=for-the-badge)

---

##  О проекте

**Shrek Luxury Edition** — это премиальный веб-интерфейс для общения с культовым персонажем DreamWorks. Проект сочетает элегантный черно-белый дизайн в стиле люксовых брендов с современными AI-технологиями.

Пользователь может вести диалог со Шреком, который отвечает в своем уникальном характере — грубовато, с юмором и философскими нотками, используя метафоры про болото и луковицы.

### Ключевые особенности

-  **AI-диалоги** — Интеграция с GigaChat API (бесплатно, 1 млн токенов/месяц)
-  **Два режима чата** — Мини-чат на главной странице и полноценная страница диалога
-  **Характер Шрека** — Глубокая настройка промпта для сохранения аутентичности персонажа
-  **История диалогов** — Сохранение контекста беседы в сессиях пользователя
-  **Асинхронные запросы** — AJAX-коммуникация без перезагрузки страницы

---

##  Технологический стек

| Компонент | Технология | Версия |
|-----------|------------|--------|
| Backend | Django | 6.0.4 |
| База данных | PostgreSQL | 16 |
| AI API | GigaChat (Сбер) | API v2 |
| Frontend | HTML5 / CSS3 / JavaScript | — |
| HTTP клиент | Requests | 2.32.3 |
| Переменные окружения | python-dotenv | 1.0.1 |

---

##  Установка и запуск

### Требования

- Python 3.12+
- PostgreSQL 16+
- Аккаунт в [GigaChat API](https://developers.sber.ru/) (бесплатно)

### 1. Клонирование репозитория

```bash
git clone https://github.com/yourusername/shrek-luxury-edition.git
cd shrek-luxury-edition
2. Создание виртуального окружения
bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
3. Установка зависимостей
bash
pip install -r requirements.txt
4. Применение миграций
bash
python manage.py makemigrations
python manage.py migrate
5. Сбор статических файлов
bash
python manage.py collectstatic
6. Запуск сервера
bash
python manage.py runserver
Откройте в браузере: http://127.0.0.1:8000/

 Структура проекта
text
myproject/
├── .env                    # Переменные окружения (API ключи)
├── .gitignore              # Игнорируемые файлы
├── manage.py               # Утилита управления Django
├── requirements.txt        # Зависимости проекта
├── myapp/                  # Основное приложение
│   ├── views.py            # Контроллеры
│   ├── gigachat_client.py  # Клиент GigaChat API
│   ├── static/myapp/       # Статические файлы (CSS, JS)
│   │   ├── css/style.css
│   │   └── js/main.js
│   └── templates/myapp/    # HTML шаблоны
│       ├── home.html
│       ├── about.html
│       ├── chat.html
│       └── item_detail.html
└── myproject/              # Конфигурация проекта
    ├── settings.py
    └── urls.py
 Дизайн
Проект выполнен в монохромной гамме с использованием:

Шрифты: Montserrat (минималистичный sans-serif) и Cormorant Garamond (элегантный serif)

Анимации: Плавное появление элементов при скролле

Эффекты: Трансформация при наведении, индикатор печати Шрека

Адаптивность: Корректное отображение на всех устройствах

 API Интеграция
GigaChat API
Проект использует GigaChat API от Сбера для генерации ответов Шрека.

Маршруты (URLs)
URL	Назначение
/	Главная страница с мини-чатом
/about/	Информация о Шреке
/chat/	Полноценная страница чата
/chat/api/	API эндпоинт для сообщений (POST)
/item/<int:item_id>/	Детальные страницы (луковица/болото/наследие)
/admin/	Админ-панель Django