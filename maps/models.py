from django.db import models

from products.models import Product


class MapMarker(models.Model):
    coordinates = models.CharField(
        null=True,
        blank=True,
        editable=False,
        max_length=128,
        verbose_name='Координаты метки',
    )
    product = models.ForeignKey(
        Product,
        verbose_name='Продукт',
        on_delete=models.CASCADE
    )

    objects = models.Manager()

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None
    ):
        super(MapMarker, self).save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields
        )
