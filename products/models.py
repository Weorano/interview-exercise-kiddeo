from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name='Название продукта'
    )
    image = models.ImageField(
        verbose_name='Картинка',
        upload_to='product_images/'
    )
    address = models.CharField(
        max_length=256,
        verbose_name='Адрес продукта'
    )

    objects = models.Manager()

    def __str__(self):
        return self.name

