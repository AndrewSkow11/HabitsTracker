# HabitsTracker

По мотивам книги Джеймс Клир «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению
старых плохих привычек.

## Развёртывание проекта

1. Создание базы данных

```commandline
psql -U postgres
```

2. Установка зависимостей
```commandline
pip install -r requirements.txt
```

3. Заполнение файла .env

4. Создание суперпользователя
```commandline
 manage.py create_superuser
```

5. Запуск сервера redis

```commandline
redis-server
```

6. Запуск celery

```commandline
celery -A config worker -l INFO
```

7. Запуск celery - beat

```commandline
celery -A config worker --beat --scheduler django --loglevel=info
```




