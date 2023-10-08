from django.views import generic
from .models import CarouselModel, ExampleWorkModel
from django.shortcuts import render, HttpResponseRedirect
from .forms import ClientForm
from django.shortcuts import redirect


class HomePage(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carousel'] = CarouselModel.objects.all()
        context['form'] = ClientForm()
        context['examples'] = ExampleWorkModel.objects.all()
        context['success'] = self.request.session.pop('success', False)
        return context

    def form_valid(self, form):
        form.save()
        self.request.session['success'] = True
        return redirect('home')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        form = ClientForm(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
