from datetime import datetime
from celery import shared_task
from habits.models import Habit
from habits.services import create_bot_telegram


@shared_task
def send_message_habit():
    print("Запуск задачи отправки уведомления в телеграм")
    now_time_hour = datetime.now().time().hour
    now_time_minute = datetime.now().minute

    habits = Habit.objects.all()
    for habit in habits:

        if (now_time_hour == habit.time_execute.hour and
                now_time_minute == habit.time_execute.minute):
            text = (f'Напоминание о привычке\n'
                    f'Сделать: {habit.action}\n'
                    f'Время: {habit.time_execute}\n'
                    f'Место: {habit.place}')
            chat_id = habit.user.chat_id
            create_bot_telegram(chat_id, text)
