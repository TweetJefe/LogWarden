# Структура LogWarden

Код сгруппирован по функциональности. Каждый пакет содержит связанные маршруты,
схемы данных, модели и бизнес-логику. Файлы-заготовки заполняются по мере обучения.

```text
logwarden/
├── main.py                  # Создание приложения и подключение API
├── api/router.py            # Сборка маршрутов функциональных пакетов
├── health/router.py         # Проверка работоспособности
├── incidents/
│   ├── router.py            # HTTP-обработчики
│   ├── dependencies.py      # Фабрики зависимостей
│   ├── schemas.py           # Схемы запросов и ответов
│   ├── models.py            # Модели БД
│   ├── service.py           # Бизнес-логика
│   └── repository.py        # Доступ к данным
├── investigations/
│   ├── router.py
│   ├── schemas.py
│   ├── models.py
│   ├── service.py
│   ├── repository.py
│   ├── state.py             # Состояние расследования
│   ├── workflow.py          # Граф расследования
│   └── agents/              # Координатор и аналитики логов, Git и API
├── reports/
│   ├── models.py
│   ├── schemas.py
│   └── agent.py             # Автор отчёта
├── evidence/
│   ├── models.py
│   └── schemas.py
├── core/                    # Общие настройки
├── db/                      # Базовая модель и подключение к БД
├── integrations/            # Клиенты OpenRouter, Git, логов и мониторинга
└── workers/                 # Celery и фоновые задачи
```

В каждом Python-пакете есть `__init__.py`.

## Аналогия со Spring

| Файл | Назначение в Spring |
|---|---|
| `router.py` | Controller |
| `schemas.py` | DTO |
| `models.py` | Entity |
| `service.py` | Service |
| `repository.py` | Repository |
| `dependencies.py` | Явная сборка зависимостей, аналог конфигурации bean |

Направление вызовов: HTTP-маршрут → сервис → репозиторий.
Репозиторий инцидентов пока является заготовкой; текущий сервис возвращает
тестовый ответ с `id=1`.

Импорты используют полный путь функционального пакета, например:

```python
from logwarden.incidents.schemas import IncidentCreate, IncidentResponse
from logwarden.incidents.service import IncidentService
```

Команда запуска из корня проекта:

```shell
python -m uvicorn logwarden.main:app --reload
```
