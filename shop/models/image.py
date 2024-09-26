from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='images', blank=True, null=True)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
