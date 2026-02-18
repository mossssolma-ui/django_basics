## Основы верстки. Bootstrap

#### Структура проекта

```
django-basics/
│
├── main.py                      # Точка входа: запуск HTTP-сервера
├── README.md                    # Документация проекта
├── .gitignore                   # ignor файлов
├── .flake8                      # конфиг flake8
├── pyproject.toml               # Poetry конфигурация (зависимости, настройки)
├── poetry.lock                  # Poetry конфигурация (зависимости)
├── poetry.toml                  
├── .venv/                       # Виртуальное окружение Poetry
└── src/                         # Исходный код проекта
    └── web_app/                  # Основной пакет приложения
        ├── __init__.py           # Маркер пакета Python
        ├── web_server.py         # HTTP-сервер (класс MyServer)
        └── site_html/             # Веб-интерфейс (HTML, статика)
            ├── contact.html        # Главная страница (контакты)
            └── static/              # Статические файлы
                ├── css/              # Стили
                │   └── bootstrap.min.css
                ├── js/               # Скрипты
                │   └── bootstrap.bundle.min.js
                └── images/           # Изображения и иконки
                    ├── bootstrap_logo.png
                    ├── face.png
                    └── bootstrap-icons-1.13.1/  # SVG-иконки Bootstrap
                        ├── house-door-fill.svg
                        ├── speedometer2.svg
                        ├── calendar-check.svg
                        └── person-circle.svg
```