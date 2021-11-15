from django.db import models

# Create your models here.
class migrations_test(models.Model):
    my_name = models.CharField(max_length=100, null=True, blank=True)