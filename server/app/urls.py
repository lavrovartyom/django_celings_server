from django.urls import include, path

from .views import AppclicationFormView, HomePage

urlpatterns = [
    # path("", AppclicationFormView.as_view()),
    path("", HomePage.as_view()),
]
