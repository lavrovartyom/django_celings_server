from django.views import generic
from .models import CarouselModel
from django.shortcuts import render
from .forms import ClientForm


class HomePage(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carousel'] = CarouselModel.objects.all()
        context['form'] = ClientForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request,
                self.template_name,
                {
                    'carousel': CarouselModel.objects.all(),
                    'form': ClientForm(),
                    'success': True
                }
            )
        else:
            return render(
                request,
                self.template_name,
                {
                    'carousel': CarouselModel.objects.all(),
                    'form': form,
                    'success': False
                }
            )
