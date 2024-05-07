# HabitsTracker

По мотивам книги Джеймс Клир «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению
старых плохих привычек.

## Развёртывание проекта

1. Создание базы данных

```commandline
% psql -U postgres
postgres=# CREATE DATABASE habits;
CREATE DATABASE
```

2. Установка зависимостей
```commandline
pip install -r requirements.txt
```

3. Заполнение файла .env

4. Создание суперпользователя
```commandline
(venv) % python3 manage.py create_superuser
Суперпользователь создан
admin@admin.ru
1234
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




