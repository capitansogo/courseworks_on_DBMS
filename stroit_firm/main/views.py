from django.http import request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *

from .forms import *
from .models import *

#главная страница
def index(request):
    get_main1 = Materials.objects.all()[:5]
    get_main2 = Materials.objects.all()[5:9]
    get_main3 = Materials.objects.all()[4:8]
    get_main4 = Materials.objects.all()[:4]
    get_main5 = Materials.objects.all()[4:8]
    get_sub_type1 = Subtypes.objects.all()[0:3]
    get_sub_type2 = Subtypes.objects.all()[3:6]
    get_sub_type3 = Subtypes.objects.all()[6:9]
    get_all = Subtype_Type.objects.all()
    count = 0
    if request.user.is_authenticated:
        count = Cart.objects.filter(user=request.user).count()

    context = {'get_main1': get_main1, 'get_main2': get_main2, 'get_main3': get_main3,
               'get_main4': get_main4, 'get_main5': get_main5, 'get_sub_types1': get_sub_type1,
               'get_sub_types2': get_sub_type2, 'get_sub_types3': get_sub_type3, 'count': count, 'get_all': get_all}
    return render(request, 'index.html', context)

#регистрация
class signup(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"

#каталог
def shop(request):
    get_materials = Materials.objects.all()
    get_sub_type1 = Subtypes.objects.all()[0:3]
    get_sub_type2 = Subtypes.objects.all()[3:6]
    get_sub_type3 = Subtypes.objects.all()[6:9]
    count = 0
    if request.user.is_authenticated:
        count = Cart.objects.filter(user=request.user).count()

    context = {'materials': get_materials, 'get_sub_types1': get_sub_type1, 'get_sub_types2': get_sub_type2,
               'get_sub_types3': get_sub_type3, 'count': count}
    return render(request, 'shop.html', context)

#добавление в корзину
def add_to_cart(request, pk):
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            add = form.save(commit=False)
            add.user = request.user
            add.material = Materials.objects.get(id=pk)
            add.total_cost = 1
            add.save()
            return redirect('shop')
    else:
        form = AddToCartForm()
    return render(request, 'add_to_cart.html', {'form': form})

#корзина
def cart(request):
    get_cart = Cart.objects.filter(user=request.user)
    total_cost = 0
    get_sub_type1 = Subtypes.objects.all()[0:3]
    get_sub_type2 = Subtypes.objects.all()[3:6]
    get_sub_type3 = Subtypes.objects.all()[6:9]
    count = 0
    if request.user.is_authenticated:
        count = Cart.objects.filter(user=request.user).count()

    for i in get_cart:
        total_cost += i.total_cost
    context = {'cart': get_cart, 'total_cost': total_cost, 'get_sub_types1': get_sub_type1,
               'get_sub_types2': get_sub_type2, 'get_sub_types3': get_sub_type3, 'count': count}
    return render(request, 'cart.html', context)

#удаление из корзины
def delete_from_cart(request, pk):
    delete = Cart.objects.get(id=pk)
    delete.delete()
    return redirect('cart')

#продажи
def sales(request):
    get_cart = Cart.objects.all()
    get_sub_type1 = Subtypes.objects.all()[0:3]
    get_sub_type2 = Subtypes.objects.all()[3:6]
    get_sub_type3 = Subtypes.objects.all()[6:9]
    cost = 0
    for i in get_cart:
        cost += i.total_cost
    return render(request, 'sales.html',
                  {'cart': get_cart, 'get_sub_types1': get_sub_type1, 'get_sub_types2': get_sub_type2,
                   'get_sub_types3': get_sub_type3, 'cost': cost})

#детальная информация о товаре
def detail(request, pk):
    get_sub_type1 = Subtypes.objects.all()[0:3]
    get_sub_type2 = Subtypes.objects.all()[3:6]
    get_sub_type3 = Subtypes.objects.all()[6:9]
    count = 0
    if request.user.is_authenticated:
        count = Cart.objects.filter(user=request.user).count()
    get_material = Materials.objects.get(id=pk)
    context = {'material': get_material, 'get_sub_types1': get_sub_type1, 'get_sub_types2': get_sub_type2,
               'get_sub_types3': get_sub_type3, 'count': count}
    return render(request, 'detail.html', context)

#добавление товара
class add_material(CreateView):
    form_class = AddMaterialForm
    success_url = reverse_lazy("shop")
    template_name = "add_material.html"

#удаление товара
class delete_material(DeleteView):
    model = Materials
    success_url = reverse_lazy("shop")
    template_name = "delete_material.html"

#редактирование товара
class edit_material(UpdateView):
    model = Materials
    form_class = AddMaterialForm
    success_url = reverse_lazy("shop")
    template_name = "edit_material.html"
