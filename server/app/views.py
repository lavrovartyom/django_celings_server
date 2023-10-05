from django.views.generic import FormView, ListView
from .models import CarouselModel

from .forms import ClientForm


class HomePage(ListView):
    model = CarouselModel
    template_name = "index.html"
    context_object_name = "carousel"


class AppclicationFormView(FormView):
    template_name = "application_add.html"
    form_class = ClientForm
    success_url = "/"
