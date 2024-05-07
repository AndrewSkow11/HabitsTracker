from datetime import datetime
from celery import shared_task
from habits.models import Habit
from habits.services import create_bot_telegram


@shared_task
def send_message_habit():
    now_time = datetime.now().time()
    print("текущее время", now_time)
    habits = Habit.objects.all()
    print("все привычки", habits)
    for habit in habits:
        if now_time == habit.time_execute:
            text = f'Я буду {habit.action} в {habit.time_execute} в {habit.place}'
            print(text)
            chat_id = habit.user.chat_id
            print(chat_id)
            create_bot_telegram(chat_id, text)
        else:
            print("Пока нет подходящего времни")