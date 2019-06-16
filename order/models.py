from django.db import models
from user.models import CustomUser

class Order(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    price = models.IntegerField()
    owner = models.ForeignKey(CustomUser, verbose_name='Заказчик', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
