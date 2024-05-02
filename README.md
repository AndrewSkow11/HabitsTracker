# HabitsTracker
По мотивам книги Джеймс Клир «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек. 

## Развёртывание проекта 

1. Создание базы данных 
```commandline
% psql -U postgres
postgres=# CREATE DATABASE habits;
CREATE DATABASE
```

2. Установка зависимостей 

3. Заполнение файла .env

4. Создание суперпользователя
```commandline
(venv) % python3 manage.py create_superuser
Суперпользователь создан
admin@admin.ru
1234
```
