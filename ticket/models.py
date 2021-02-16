from django.db import models


# Create your models here.
class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    seat_num = models.IntegerField(unique=True)

    def __str__(self):
        return self.ticket_id