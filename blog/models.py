from datetime import datetime

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    pub_date = models.DateField(default=datetime.today)
    content = models.TextField()

    class Meta:
        ordering = ('-pub_date',)
        verbose_name_plural = 'Новости',
        verbose_name = 'Новость'

    def __str__(self):
        return self.title
