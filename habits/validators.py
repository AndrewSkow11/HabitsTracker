from rest_framework.serializers import ValidationError

class RewardHabitValidator:

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        related_habit = dict(value).get(self.field1)
        reward = dict(value).get(self.field2)


        if related_habit and reward:
            raise ValidationError("Можно добавить либо связанную привычку,"
                                  "либо вознаграждение, но не одновременно!")