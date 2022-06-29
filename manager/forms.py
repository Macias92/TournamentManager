from django import forms

from manager.models import Tournament


class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = '__all__'
        widgets = {
            'players': forms.CheckboxSelectMultiple}
