from django.db import models
from django.contrib.auth.models import User


class Type(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Mobilty(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    plate_number = models.CharField(max_length=15)
    number_of_seats = models.IntegerField()
    availabilty = models.BooleanField(default=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} | ({self.type})"


class Ticket(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobility = models.ForeignKey(Mobilty,on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    is_valid = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.mobility} | ({self.user})"