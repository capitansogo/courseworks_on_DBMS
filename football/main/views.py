from django.shortcuts import render
from .models import Teams, Players, Coach, Matches
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import MatchForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


def index(request):
    teams = Teams.objects.all()
    return render(request, 'index.html', {'teams': teams})


def teams_champions(request):
    teams = Teams.objects.filter(league_id=1)
    return render(request, 'teams.html', {'teams': teams})


def teams_europe(request):
    teams = Teams.objects.filter(league_id=2)
    return render(request, 'teams.html', {'teams': teams})


def team(request, team_id):
    team = Teams.objects.get(id=team_id)
    coach = Coach.objects.get(team_id=team_id)
    players = Players.objects.filter(team_id=team_id)
    return render(request, 'team.html', {'team': team, 'coach': coach, 'players': players})


def player(request, player_id):
    player = Players.objects.get(id=player_id)
    return render(request, 'player.html', {'player': player})


def matches_champions(request):
    matches = Matches.objects.filter(league_id=1)
    return render(request, 'matches.html', {'matches': matches})


def matches_europe(request):
    matches = Matches.objects.filter(league_id=2)
    return render(request, 'matches.html', {'matches': matches})


def match(request, match_id):
    match = Matches.objects.get(id=match_id)
    return render(request, 'match.html', {'match': match})


# фунция авторизации
def login(request):
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    # После выхода пользователя, перенаправьте его на главную страницу или любую другую страницу
    return redirect('index')


@login_required
def edit_match(request, match_id):
    match = get_object_or_404(Matches, pk=match_id)
    if request.method == 'POST':
        form = MatchForm(request.POST, instance=match)
        if form.is_valid():
            form.save()
            return redirect('match', match_id=match_id)
    else:
        form = MatchForm(instance=match)
    return render(request, 'edit_match.html', {'form': form, 'match_id': match_id})


@login_required
def delete_match(request, match_id):
    match = get_object_or_404(Matches, pk=match_id)
    match.delete()
    return redirect('index')


def add_match(request):
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('matches_champions')  # Перенаправление после успешного добавления матча
    else:
        form = MatchForm()
    return render(request, 'add_match.html', {'form': form})


def add_team(request):
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Перенаправление после успешного добавления матча
    else:
        form = MatchForm()
    return render(request, 'add_team.html', {'form': form})