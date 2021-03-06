"""TournamentManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts.views import LoginView, LogoutView, CreateUserView
from manager.views import IndexView, TournamentTypeAddView, PlayerAddView, TournamentAddView, TournamentDeleteView, \
    TournamentEditView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ttype_add/', TournamentTypeAddView.as_view(), name='ttype_add'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create_user/', CreateUserView.as_view(), name='create_user'),

    path('', IndexView.as_view(), name='index'),
    path('player_add/', PlayerAddView.as_view(), name='player_add'),
    path('tournament_add/', TournamentAddView.as_view(), name='tournament_add'),
    path('tournament_edit/', TournamentEditView.as_view(), name='tournament_edit'),
    path('tournament_delete/', TournamentDeleteView.as_view(), name='tournament_delete')




]
