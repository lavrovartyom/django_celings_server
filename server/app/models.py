from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone


class ExampleWorkModel(models.Model):
    """Модель примеров работ."""

    image = models.ImageField(upload_to="images", null=False, blank=False)
    ceiling_type = models.CharField(
        max_length=150, blank=False, help_text="Тип натяжного полотна"
    )
    description = models.TextField(help_text="Описание")
    objects = models.Manager()


class Client(models.Model):
    """Модель клиента/заявки."""

    full_name = models.CharField(max_length=300, blank=False)
    phone_number = models.CharField(
        max_length=17,
        validators=[RegexValidator(r"^\+7\(\d{3}\)-\d{3}-\d{2}-\d{2}$")],
        blank=False,
    )
    address = models.CharField(
        max_length=300,
        blank=False,
    )
    comment = models.TextField(blank=True)
    application_date = models.DateTimeField(default=timezone.now, editable=False)
    objects = models.Manager()

    def __str__(self):
        return self.full_name


class CarouselModel(models.Model):
    """Модель слайдера."""

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to="images", null=False, blank=False)
    objects = models.Manager()
