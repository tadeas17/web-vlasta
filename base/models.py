from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class PhotoType(models.Model):
    name = models.CharField(max_length=128, verbose_name='Název')
    type_photo = models.IntegerField(verbose_name='Číslo typu')
    main_type_photo = models.BooleanField(default=False, verbose_name='Zobrazovat jako náhled na kategorii')

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Typ fotky'
        verbose_name_plural = 'Typy fotek'

        # TODO: přidat metodu na limit 4 pro homepage nebo nějaké pseudonáhodné zobrazování fotek
class Photo(models.Model):
    name = models.CharField(max_length=128, verbose_name='Název')
    photo = models.ImageField(upload_to="fotky")
    photo_type = models.ForeignKey(PhotoType, on_delete=models.CASCADE)
    home_page_photo = models.BooleanField(default=False, verbose_name="Zobratovat na homepage")
    type_galeri_photo = models.BooleanField(default=False, verbose_name="Zobrazovat jako náhled na ketegorii")
    slider_photo = models.BooleanField(default=False, verbose_name="Zobrazovat ve slideru")

    created = models.DateTimeField(default=datetime.now, blank=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False,
                             default=1)  # TODO: nastav default jako aktuálního usera

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Fotka'
        verbose_name_plural = 'Fotky'
