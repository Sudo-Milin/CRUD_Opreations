from django.db import models

# Create your models here.

class CRUD(models.Model):
    class Meta:
        verbose_name = 'CRUD'
        verbose_name_plural = 'CRUD'

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text