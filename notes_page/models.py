from django.db import models


class Task(models.Model):
    objects = None
    title = models.CharField('Название', max_length=25)
    task = models.TextField('Описание',max_length=100)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return '/'

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
