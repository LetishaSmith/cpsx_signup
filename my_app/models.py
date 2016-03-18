from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
    room = models.TextField()
    key = models.TextField()

    def __str__(self):
        return self.room + " " + self.key



class Participant(models.Model):
    user = models.OneToOneField(User)
    rm_1 = models.ForeignKey(Room) # links participant to a room

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " " + self.user.username + " " + self.user.email + \
               " " + self.rm_1.room + " " + self.rm_1.key