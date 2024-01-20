from django.urls import path

from .views import HomePage

app_name = "app"

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
]
