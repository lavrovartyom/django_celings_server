from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone


class Client(models.Model):
    """Модель клиента/заявки"""

    full_name = models.CharField(max_length=300, blank=False, help_text="ФИО")
    phone_number = models.CharField(
        max_length=17,
        validators=[RegexValidator(r"^\+7\(\d{3}\)-\d{3}-\d{2}-\d{2}$")],
        blank=False,
        help_text="+7(XXX)-XXX-XX-XX",
    )
    address = models.CharField(
        max_length=300, blank=False, help_text="Введите ваш адрес"
    )
    comment = models.TextField(blank=True, help_text="Комментарий к заявке")
    application_date = models.DateTimeField(default=timezone.now, editable=False)
    objects = models.Manager()

    def __str__(self):
        return self.full_name


class CarouselModel(models.Model):
    """Модель слайдера"""

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to="images", null=False, blank=False)
    objects = models.Manager()
