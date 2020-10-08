from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    active = models.BooleanField(max_length=1, default=True)

    class Meta:
        db_table = 'client'

    def __str__(self):
        return '{} - {}'.format(self.name, self.email)
