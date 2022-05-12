from django.db import models
# Give us access to the built in user model in django
from django.contrib.auth import get_user_model
# Create your models here.

class Snack(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True)
    description = models.TextField()
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name