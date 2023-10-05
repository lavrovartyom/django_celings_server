from django.contrib import admin

from .models import Client, CarouselModel


class ClientAdmin(admin.ModelAdmin):
    list_display = [
        "full_name",
        "phone_number",
        "address",
        "comment",
        "application_date",
    ]
    list_filter = ["application_date"]


class CarouselAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "image"]


admin.site.register(CarouselModel, CarouselAdmin)
admin.site.register(Client, ClientAdmin)
