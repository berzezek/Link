from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Link(models.Model):
    title = models.CharField('Описание', max_length=100)
    slug = models.SlugField('короткое название', unique=True)
    long_link = models.CharField('ссылка', max_length=255, null=True)
    date = models.DateTimeField('Дата', default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'ССылку'
        verbose_name_plural = 'ССылки'

    def get_absolute_url(self):
        return reverse('link-detail', kwargs={'slug': self.slug})
