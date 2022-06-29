from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from django.urls import reverse_lazy

from manager.forms import TournamentForm
from manager.models import TournamentType, Player, Tournament


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class TournamentTypeAddView(CreateView):
    model = TournamentType
    fields = '__all__'
    success_url = reverse_lazy('index')
    template_name = 'form.html'


class PlayerAddView(CreateView):
    model = Player
    fields = '__all__'
    success_url = reverse_lazy('index')
    template_name = 'form.html'


class TournamentAddView(View):
    def get(self, request):
        form = TournamentForm
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        pass

