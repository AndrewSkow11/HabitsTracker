from django.db import models
from users.models import User


class Habit(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='создатель',
        null=True,
        blank=True,
    )
    place = models.CharField(
        max_length=256,
        default='любое место',
        verbose_name='место выполнения'
    )
    time_execute = models.TimeField(
        verbose_name='время для выполнения',
        default='00:00:00'
    )
    action = models.CharField(
        max_length=256,
        verbose_name='действие',
        default='новые действие',
    )
    is_nice = models.BooleanField(
        default=False,
        verbose_name='приятность привычки',
    )
    related_habit = models.ForeignKey(
        'Habit',
        verbose_name='связанная привычка',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    periodicity = models.PositiveSmallIntegerField(
        default=1,
        verbose_name='периодичность выполнения (дни)',
    )
    reward = models.CharField(
        max_length=256,
        verbose_name='вознаграждение',
        null=True,
        blank=True,
    )
    time_duration = models.PositiveSmallIntegerField(
        verbose_name='время на выполнение в секундах',
        default='60',
    )
    is_public = models.BooleanField(
        verbose_name="признак публичности",
        default=True
    )

    def __str__(self):
        return (f'Пользователь: {self.user}\n'
                f'Действие: {self.action}\n'
                f'Время: {self.time_duration}\n'
                f'Место: {self.place}')

    class Meta:
        verbose_name = "привычка",
        verbose_name_plural = "привычки"
        ordering = ("id",)
