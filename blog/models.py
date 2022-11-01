from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    amount = models.IntegerField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def plus1(self):
        self.amount += 1
        self.save() 
        # saveしないと保存されない
    def minus1(self):
        self.amount -= 1
        self.save()
    def __str__(self):
        return self.title
    # def __init__(self):
    #     self.amount = 0

class Wallet(models.Model):
    amount = models.IntegerField(0)

    def plus1(self):
        self.amount += 1
    def minus1(self):
        self.amount -= 1

    def __str__(self):
        return f"{self.amount}"
    # def __init__(self):
    #     self.amount = 0
        # self.save()