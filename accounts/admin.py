from django.contrib import admin
from django.contrib.auth.models import User
from accounts.models import Profile
from manager.models import TournamentType

admin.site.register(Profile),
admin.site.register(TournamentType),
