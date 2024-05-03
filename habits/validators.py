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
            raise ValidationError("Можно добавить либо связанную привычку,"
                                  "либо вознаграждение, но не одновременно!")


class HabitRelatedIsNiceValidator:
    """Валидатор проверяет, что связанная привычка -
    приятная привычка"""

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        related_habit = dict(value).get(self.field1)
        is_nice = dict(value).get(self.field2)

        if related_habit and not is_nice:
            raise ValidationError("Связанной привычкой может быть только"
                                  "приятная привычка!")


class NiceHabbitValidator:
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

        if is_nice and reward and related_habit:
            raise ValidationError("У приятной привычки не может быть"
                                  " вознаграждения или связанной привычки!")


class DurationValidatior:
    """Валиадтор проверяет, что
     время выполнения должно быть не больше 120 секунд."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        time_duration = dict(value).get(self.field)

        if time_duration and time_duration > 120:
            raise ValidationError("Превышено время выоленние привычки"
                                  "(не более 120 секунд)!")


