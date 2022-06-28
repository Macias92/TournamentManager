from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from django.urls import reverse_lazy
from manager.models import TournamentType


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class TournamentTypeAddView(CreateView):
    model = TournamentType
    fields = '__all__'
    success_url = reverse_lazy('index')
    template_name = 'form.html'


class TournamentAddView(View):
    def get(self, request):
        return render('form.html')