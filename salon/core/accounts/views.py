from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from .forms import *
from .models import *


class signup(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def index(request):
    get_staff = Users.objects.filter(st=True)[:4]
    get_types_of_services = Types_of_services.objects.all()[:3]
    return render(request, 'index.html', {'get_staff': get_staff, 'ToS': get_types_of_services})


def services(request):
    get_types_of_services = Types_of_services.objects.all()
    return render(request, 'services.html', {'ToS': get_types_of_services})


def materials(request):
    get_materials = Materials.objects.all()
    return render(request, 'materials.html', {'materials': get_materials})


class BuyMaterials(CreateView):
    model = Purchases
    form_class = BuyMaterialsForm
    template_name = 'buy_materials.html'
    success_url = reverse_lazy('materials')

    def get_initial(self):
        return {
            'user': self.request.user.id,
            'material': self.kwargs['pk']
        }


class EditMaterials(UpdateView):
    model = Materials
    form_class = EditMaterialsForm
    template_name = 'edit_materials.html'
    success_url = reverse_lazy('materials')


class CreateWrite_offs(CreateView):
    model = Write_offs
    form_class = Write_offsForm
    template_name = 'write_offs.html'
    success_url = reverse_lazy('materials')

    def get_initial(self):
        return {
            'user': self.request.user.id,
            'material': self.kwargs['pk']
        }


class Profile(DetailView):
    model = Users
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Orders.objects.filter(client=self.kwargs['pk'])
        return context


class CreateOrder(CreateView):
    model = Orders
    form_class = OrderForm
    template_name = 'create_order.html'
    success_url = reverse_lazy('index')

    def get_initial(self):
        return {
            'client': self.request.user.id,
            'types_of_services': self.kwargs['pk']
        }


def please_login(request):
    return render(request, 'please_login.html')


def orders(request):
    get_orders = Orders.objects.all()
    return render(request, 'orders.html', {'get_orders': get_orders})


class DeleteOrder(DeleteView):
    model = Orders
    template_name = 'delete_order.html'
    success_url = reverse_lazy('orders')


class EditOrder(UpdateView):
    model = Orders
    form_class = OrderForm
    template_name = 'edit_order.html'
    success_url = reverse_lazy('orders')


def logout_view(request):
    logout(request)
    return redirect('index')
