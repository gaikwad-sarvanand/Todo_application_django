from django.db import models
import datetime

# Create your models here.


class TodoModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    added_at = models.DateTimeField(auto_now_add=True)
    finish_by_time = models.TimeField(
        auto_created=False, auto_now=False, auto_now_add=False, default=datetime.time(12, 0, 0))
    finish_by_date = models.DateField(
        auto_created=False, auto_now=False, auto_now_add=False, default=datetime.date.today)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Todo"
