from django.shortcuts import render
from .models import Player
from .models import Team    
from .models import Finance

# Create your views here.

# def home(request):
#     context = {}
#     return render(request, 'sportsManagement/home.html', context)

def home(request):
        players = Player.objects.all()
        teams = Team.objects.all()
        finances = Finance.objects.all()

        context = {"players": players, "teams": teams, "finances": finances} # dict that will hold out data
        return render(request, 'sportsManagement/home.html', context)

def about(request):
    context = {}
    return render(request, 'sportsManagement/about.html', context)

def team(request):
    context = {}
    return render(request, 'sportsManagement/team.html', context)