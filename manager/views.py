from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from manager.forms import TournamentForm
from manager.models import TournamentType, Player, Tournament, Match, Team


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
        form = TournamentForm(request.POST)
        if form.is_valid():
            num_players = form.cleaned_data.get('num_players')
            selected = form.cleaned_data.get('players')
            if len(selected) > num_players:
                return render(request, 'form.html', {'form': form,
                                                     'error': 'You have selected more players than you declared!'})
            if len(selected) < num_players:
                return render(request, 'form.html', {'form': form,
                                                     'error': 'You have selected less players than you declared!'})
            if len(selected) == 1:
                return render(request, 'form.html', {'form': form,
                                                     'error': 'It cannot be one player in Tournament!'})
            # TODO  think about getting less than declared players exception, could be less?
            #  add exception about the player has in declared date another tournament and is not available to choose
            tournament = form.save()
        return render(request, "form.html", {"form": form})


class TournamentEditView(UpdateView):
    model = Tournament
    template_name = 'form.html'
    success_url = reverse_lazy('index')


class TournamentDeleteView(DeleteView):
    model = Tournament
    template_name = 'form.html'
    success_url = reverse_lazy('index')


class MatchResultAddView(CreateView):
    model = Match
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('index')
    # TODO add special view where you can manage a tournament, like adding players, results, viewing fixtures ect.


class TeamAddView(CreateView):
    model = Team
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('index')  # the same as up^


