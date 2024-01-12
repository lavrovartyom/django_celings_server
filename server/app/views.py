from django.http import JsonResponse
from django.views import generic

from .forms import ClientForm
from .models import CarouselModel, ExampleWorkModel


class HomePage(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["carousel"] = CarouselModel.objects.all()
        context["form"] = ClientForm()
        context["examples"] = ExampleWorkModel.objects.all()

        return context

    def post(self, request):
        form = ClientForm(request.POST)

        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})

        return JsonResponse({"success": False})
