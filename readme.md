# ExchangeRUB
Web-приложение, которое отображает курс валюты по отношению к рублю на заданную дату.
## Описание задачи
При обращении к приложению по
адресу http://localhost:8000/rate/?charcode=AUD&date=2024-01-01 , оно должно выводить результат в виде JSON в формате:
```json
{
    "charcode": "AUD",
    "date": "2024-01-01",
    "rate": 57.0627
}
```
Данные по валютам должны храниться в базе данных приложения. А для пополнения этой базы данных нужно написать команду, которая будет раз в сутки обращаться к сервису ЦБ за актуальными курсами валют по адресу: https://www.cbr-xml-daily.ru/daily_json.js

## Запуск приложения
### Клонирование и настройка проекта

#### HTTPS
```bash
git clone https://github.com/StasKrut/ExchangeRUB.git
```

#### SSH
```bash
git clone git@github.com:StasKrut/ExchangeRUB.git
```

### Локальный запуск сервера

#### Переход в директорию, установка пакетов

```bash
cd exchange
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip -r requirements.txt
```

#### Миграции, заполнение базы, запуск проекта

```bash
python manage.py migrate
python manage.py collect_rates
python manage.py runserver
```

#### crontab string для сбора данных по расписанию
```bash
0 0 * * * cd /path/to/your/project && python manage.py collect_rates
```
где path/to/your/project - ваш путь до папки с manage.py
