from django.db import models

# Create your models here.
class AgileValue(models.Model):
    field_value = models.CharField(max_length=200)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class AgilePrinciple(models.Model):
    field_value = models.CharField(max_length=200)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)