from django.db import models

DAYS = [
    ('mon', 'Monday'),
    ('tue', 'Tuesday'),
    ('wed', 'Wednesday'),
    ('thurs', 'Thursday'),
    ('fri', 'Friday'),
]

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    day = models.CharField(max_length=5,choices=DAYS)
    date = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)


    def __str__(self):
        return self.title