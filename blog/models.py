from datetime import datetime

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateField(default=datetime.today)

    class Meta:
        ordering = ('-date',)
        verbose_name_plural = 'Новости',
        verbose_name = 'Новость'

    def __str__(self):
        return self.title
