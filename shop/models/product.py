from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True, verbose_name="Наименование")
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    item_number = models.CharField(max_length=100, verbose_name="Артикул")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="Категория")
    images = models.ManyToManyField('Image', verbose_name="Изображения")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']