from django.db import models


class Task(models.Model):
    objects = None
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return '/'

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
