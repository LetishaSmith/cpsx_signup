from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Participant(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " " + self.user.username + " " + self.user.email


class Room(models.Model):
    room = models.TextField()
    key = models.TextField()
    test_taker = models.ForeignKey(Participant) # allows test_taker to inherit the participant attrinutes

    def __str__(self):
        return self.room + " " + self.key + self.test_taker.first_name + " " + self.test_taker.last_name + " " + \
               self.test_taker.username + " " + self.test_taker.email