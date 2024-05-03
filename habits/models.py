from django.db import models

from users.models import User

# Create your models here.
PERIODIC_CHOICES = {
    "EVERY_DAY": "ED",
    "EVERY_WEEK": "EW",
    "EVERY_MONTH": "EM",
}


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
        verbose_name='место выполнения'
    )
    time_execute = models.TimeField(
        verbose_name='время для выполнения'
    )
    action = models.CharField(
        max_length=256,
        verbose_name='действие'
    )
    is_nice = models.BooleanField(
        default=False,
        verbose_name='приятность привычки'
    )
    related_habit = models.ForeignKey(
        'Habit',
        verbose_name='связанная привычка',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    periodicity = models.CharField(
        choices=PERIODIC_CHOICES,
        default='ED'
    )
    reward = models.CharField(
        max_length=256,
        verbose_name='вознаграждение'
    )
    time_for_execute = models.PositiveSmallIntegerField(
        verbose_name='время на выполнение'
    )
    is_public = models.BooleanField(
        verbose_name="признак публичности"
    )

    def __str__(self):
        return (f'{self.user} будет {self.action} в {self.time_for_execute}'
                f' в {self.place} ')