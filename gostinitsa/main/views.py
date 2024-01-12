from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import *
from .models import *


# Create your views here.


def index(request):
    get_nomers = Nomer.objects.all()[:4]
    get_sostav = SostavUslugi.objects.all()
    context = {'nomers': get_nomers, 'sostav': get_sostav}
    return render(request, 'index.html', context)


def rooms(request):
    get_nomers = Nomer.objects.all()
    get_sostav = SostavUslugi.objects.all()
    context = {'nomers': get_nomers, 'sostav': get_sostav}
    return render(request, 'rooms.html', context)


class signup(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def room(request, pk):
    get_nomer = Nomer.objects.get(id=pk)
    get_sostav = SostavUslugi.objects.all()
    context = {'nomer': get_nomer, 'sostav': get_sostav,}
    return render(request, 'room.html', context)


def add_bron(request, pk):
    if request.method == "POST":
        form = BronForm(request.POST)
        if form.is_valid():
            rew = form.save(commit=False)
            rew.id_nomer = Nomer.objects.get(id=pk)
            rew.id_user = request.user
            st = Nomer.objects.get(id=pk)
            st.status = True
            rew.save()
            return redirect('room', pk=pk)
    else:
        form = BronForm()
    return render(request, 'add_bron.html', {'form': form})


class edit_room(UpdateView):
    model = Nomer
    form_class = EditRoomForm
    success_url = reverse_lazy("rooms")
    template_name = "edit_room.html"


def users(request):
    get_users = User.objects.all()
    get_bron = Bron.objects.all()
    context = {'users': get_users, 'bron': get_bron}
    return render(request, 'users.html', context)


class bron_delete(DeleteView):
    model = Bron
    success_url = reverse_lazy("users")
    template_name = "bron_delete.html"


class bron_update(UpdateView):
    model = Bron
    form_class = BronForm
    success_url = reverse_lazy("users")
    template_name = "bron_update.html"

def free_nomers(request):
    get_nomers = Nomer.objects.filter(status=False)
    context = {'nomers': get_nomers}
    return render(request, 'free_nomers.html', context)
