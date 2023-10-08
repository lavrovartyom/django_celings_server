from django.views import generic
from .models import CarouselModel, ExampleWorkModel
from .forms import ClientForm
from django.http import JsonResponse


class HomePage(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carousel'] = CarouselModel.objects.all()
        context['form'] = ClientForm()
        context['examples'] = ExampleWorkModel.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        return JsonResponse({'success': True})

    def form_invalid(self, form):
        return JsonResponse({'success': False, 'errors': form.errors})

    def post(self, request, *args, **kwargs):
        form = ClientForm(request.POST)
        if form.is_valid():
            return self.form_valid(form)

        return self.form_invalid(form)
