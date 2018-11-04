from django.db import models

class Ticket(models.Model):
    ticket_id = models.CharField(max_length=7)
    team = models.CharField(max_length=11)
    priority = models.CharField(max_length=9)
