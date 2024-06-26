from rest_framework.serializers import ValidationError


class RewardHabitValidator:
    """Валидатор проверяет не установлено ли вознаграждение
    и полезная привычка одновременно"""

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        related_habit = dict(value).get(self.field1)
        reward = dict(value).get(self.field2)

        if related_habit and reward:
            raise ValidationError(
                "Можно добавить либо связанную привычку,"
                "либо вознаграждение, но не одновременно!"
            )


class HabitRelatedIsNiceValidator:
    """Валидатор проверяет, что связанная привычка -
    приятная привычка"""

    def __init__(self, field1):
        self.field1 = field1

    def __call__(self, value):
        if value:
            related_habit = dict(value).get(self.field1)
            if related_habit and not related_habit.is_nice:
                raise ValidationError(
                    "Связанной привычкой может быть только "
                    "приятная привычка!"
                )


class NiceHabitValidator:
    """Валидатор проверяет, что у приятной привычки не может
    быть вознаграждения или связанной привычки."""

    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def __call__(self, value):
        related_habit = dict(value).get(self.field1)
        reward = dict(value).get(self.field2)
        is_nice = dict(value).get(self.field3)

        if is_nice:
            if related_habit:
                raise ValidationError(
                    "У приятной привычки не может быть связанной привычки!"
                )
            if reward:
                raise ValidationError(
                    "У приятной привычки не может быть вознаграждения!"
                )


class DurationValidator:
    """Валиадатор проверяет, что
    время выполнения должно быть не больше 120 секунд."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if "time_duration" in dict(value):
            time_duration = dict(value).get(self.field)

            if time_duration and time_duration >= 120:
                raise ValidationError(
                    "Превышено время выполнение привычки"
                    "не более 120 секунд)!")


class PeriodicValidator:
    """Валидатор проверяет, что За одну неделю необходимо
    выполнить привычку хотя бы один раз."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if "periodicity" in dict(value):
            periodicity = dict(value).get(self.field)

            if periodicity and periodicity < 1 or periodicity > 7:
                raise ValidationError("Интервал задания периодичности [1; 7]!")
            if periodicity == 0:
                raise ValidationError("Периодичность"
                                      " не может быть задана нулём!")
