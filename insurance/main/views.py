from datetime import datetime, timedelta
from itertools import chain

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, redirect

from main.forms import AutoInsuranceForm, HealthInsuranceForm, PropertyInsuranceForm, UserForm, SalaryReportForm
from main.models import *


# фунция для главной страницы
def index(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('login')


# функция для страницы авторизации
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)  # проверка пользователя
        if user is not None:
            login(request, user)

            next_url = request.GET.get('next', 'index')  # переход на следующую страницу
            return redirect(next_url)

    return render(request, 'login.html')


# функция для выхода из аккаунта
def logout_view(request):
    logout(request)
    return redirect('index')


# функция для страницы со страховыми программами
def insurances(request):
    auto_insurances = AutoInshurance.objects.filter(agent=request.user)
    health_insurances = HealthInshurance.objects.filter(agent=request.user)
    property_insurances = PropertyInshurance.objects.filter(agent=request.user)  # получение страховок агента
    return render(request, 'insurances.html',
                  {'auto_insurances': auto_insurances, 'health_insurances': health_insurances,
                   'property_insurances': property_insurances})


# функция для страницы с автостраховками
def detail_auto_insurance(request, insurance_id):
    insurance = AutoInshurance.objects.get(id=insurance_id)
    salary = int(insurance.salary * insurance.percent_agent / 100)  # расчет зарплаты(?) агента
    return render(request, 'detail_auto_insurance.html', {'auto_insurance': insurance, 'salary': salary})


# функция для страницы с медицинскими страховками
def detail_health_insurance(request, insurance_id):
    insurance = HealthInshurance.objects.get(id=insurance_id)
    salary = int(insurance.salary * insurance.percent_agent / 100)
    return render(request, 'detail_health_insurance.html', {'health_insurance': insurance, 'salary': salary})


# функция для страницы с имущественными страховками
def detail_property_insurance(request, insurance_id):
    insurance = PropertyInshurance.objects.get(id=insurance_id)
    salary = int(insurance.salary * insurance.percent_agent / 100)
    return render(request, 'detail_property_insurance.html', {'property_insurance': insurance, 'salary': salary})


# функция для создания автостраховки
def create_auto_insurance(request):
    if request.method == 'POST':  # если метод POST, то создаем форму
        form = AutoInsuranceForm(request.POST)  # получаем данные из формы
        if form.is_valid():  # если форма валидна, то сохраняем данные
            auto_insurance = form.save(commit=False)  # создаем объект, но не сохраняем его в базу данных
            auto_insurance.agent = request.user  # добавляем агента
            auto_insurance.save()  # сохраняем объект в базу данных
            return redirect('insurances')  # переходим на страницу со страховками
    else:
        form = AutoInsuranceForm()  # иначе создаем пустую форму

    return render(request, 'create_auto_insurance.html', {'form': form})


# функция для создания медицинской страховки
def create_health_insurance(request):
    if request.method == 'POST':
        form = HealthInsuranceForm(request.POST)
        if form.is_valid():
            health_insurance = form.save(commit=False)
            health_insurance.agent = request.user
            health_insurance.save()
            return redirect('insurances')
    else:
        form = HealthInsuranceForm()

    return render(request, 'create_health_insurance.html', {'form': form})


# функция для создания имущественной страховки
def create_property_insurance(request):
    if request.method == 'POST':
        form = PropertyInsuranceForm(request.POST)
        if form.is_valid():
            property_insurance = form.save(commit=False)
            property_insurance.agent = request.user
            property_insurance.save()
            return redirect('insurances')
    else:
        form = PropertyInsuranceForm()

    return render(request, 'create_property_insurance.html', {'form': form})


# функции для удаления автостраховки
def delete_auto_insurance(request, insurance_id):
    insurance = AutoInshurance.objects.get(id=insurance_id)  # получаем страховку по id
    insurance.delete()  # удаляем страховку
    return redirect('insurances')


# функции для удаления медицинской страховки
def delete_health_insurance(request, insurance_id):
    insurance = HealthInshurance.objects.get(id=insurance_id)
    insurance.delete()
    return redirect('insurances')


# функции для удаления имущественной страховки
def delete_property_insurance(request, insurance_id):
    insurance = PropertyInshurance.objects.get(id=insurance_id)
    insurance.delete()
    return redirect('insurances')


# функции для обновления автостраховки
def update_auto_insurance(request, insurance_id):
    insurance = AutoInshurance.objects.get(id=insurance_id)
    if request.method == 'POST':
        form = AutoInsuranceForm(request.POST, instance=insurance)
        if form.is_valid():
            insurance.agent = request.user  # добавляем агента
            form.save()
            return redirect('insurances')
    else:
        form = AutoInsuranceForm(instance=insurance)

    return render(request, 'update_auto_insurance.html', {'form': form})


# функции для обновления медицинской страховки
def update_health_insurance(request, insurance_id):
    insurance = HealthInshurance.objects.get(id=insurance_id)
    if request.method == 'POST':
        form = HealthInsuranceForm(request.POST, instance=insurance)
        if form.is_valid():
            insurance.agent = request.user
            form.save()
            return redirect('insurances')
    else:
        form = HealthInsuranceForm(instance=insurance)

    return render(request, 'update_health_insurance.html', {'form': form})


# функции для обновления имущественной страховки
def update_property_insurance(request, insurance_id):
    insurance = PropertyInshurance.objects.get(id=insurance_id)
    if request.method == 'POST':
        form = PropertyInsuranceForm(request.POST, instance=insurance)
        if form.is_valid():
            insurance.agent = request.user
            form.save()
            return redirect('insurances')
    else:
        form = PropertyInsuranceForm(instance=insurance)

    return render(request, 'update_property_insurance.html', {'form': form})


# функция для добавления клиента
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # создаем объект, но не сохраняем его в базу данных
            user.set_password(form.cleaned_data["password"])  # устанавливаем пароль
            user.role = Roles.objects.get(name='Клиент')  # добавляем роль
            user.save()  # сохраняем объект в базу данных
            messages.success(request, 'Вы успешно зарегистрированы!')  # выводим сообщение
            return redirect('clients')
    else:
        form = UserForm()

    return render(request, 'register.html', {'form': form})


# функция для страницы со списком клиентов
def clients(request):
    clients = User.objects.filter(role__name='Клиент')
    # количестов страховок
    for client in clients:
        auto_insurances = AutoInshurance.objects.filter(client=client)  # получаем страховки клиента
        health_insurances = HealthInshurance.objects.filter(client=client)
        property_insurances = PropertyInshurance.objects.filter(client=client)
        count_insurances = auto_insurances.count() + health_insurances.count() + property_insurances.count()  # считаем количество страховок
        client.count_insurances = count_insurances
        client.save()

    return render(request, 'clients.html', {'clients': clients})


# функция для страницы с детальной информацией о клиенте
def detail_client(request, client_id):
    client = User.objects.get(id=client_id)
    auto_insurances = AutoInshurance.objects.filter(client=client)
    health_insurances = HealthInshurance.objects.filter(client=client)
    property_insurances = PropertyInshurance.objects.filter(client=client)
    insurances = list(
        chain(auto_insurances, health_insurances, property_insurances))  # объединяем страховки в один список
    return render(request, 'detail_client.html', {'client': client, 'insurances': insurances})


# функция для страницы с профилем агента
def profile(request, user_id):
    user = User.objects.get(id=user_id)
    auto_insurances = AutoInshurance.objects.filter(agent=user_id)
    health_insurances = HealthInshurance.objects.filter(agent=user_id)
    property_insurances = PropertyInshurance.objects.filter(agent=user_id)  # получаем страховки агента
    insurances = list(
        chain(auto_insurances, health_insurances, property_insurances))  # объединяем страховки в один список
    salary = 0
    for insurance in insurances:
        if insurance.date >= datetime.now().date() - timedelta(
                days=14):  # если страховка была оформлена не позднее, чем 14 дней назад
            salary += int(insurance.salary * insurance.percent_agent / 100)  # то добавляем зарплату агента
    user.salary = salary

    percent = 0
    for insurance in insurances:
        percent += insurance.percent_agent  # считаем процент агента
    if len(insurances) > 0:
        percent = percent / len(insurances)  # средний процент агента
    user.percent = percent.__round__(2)  # округляем до 2 знаков после запятой

    return render(request, 'profile.html',
                  {'user': user, 'insurances': insurances, 'salary': salary, 'percent': percent})


# функция для страницы с отчетом по зарплате
def salary_report(request):
    results = None  # результаты расчета зарплаты

    if request.method == 'POST':
        form = SalaryReportForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']  # получаем данные из формы
            end_date = form.cleaned_data['end_date']  # получаем данные из формы
            # перебор по агентам для расчета зарплаты
            agents = User.objects.filter(role__name='Агент')
            results = []
            for agent in agents:
                auto_insurances = AutoInshurance.objects.filter(agent=agent, date__gte=start_date, date__lte=end_date)
                health_insurances = HealthInshurance.objects.filter(agent=agent, date__gte=start_date,
                                                                    date__lte=end_date)
                property_insurances = PropertyInshurance.objects.filter(agent=agent, date__gte=start_date,
                                                                        date__lte=end_date)  # получаем страховки агента
                insurances = list(chain(auto_insurances, health_insurances,
                                        property_insurances))  # объединяем страховки в один список
                salary = 0
                for insurance in insurances:
                    salary += int(insurance.salary * insurance.percent_agent / 100)  # считаем зарплату агента
                results.append({'agent': agent, 'salary': salary})

            # формирование массивов для графика
            labels = []
            data = []
            average_salary = 0
            for result in results:
                labels.append(result['agent'].first_name + ' ' + result['agent'].last_name)  # добавляем агента в массив
                data.append(result['salary'])  # добавляем зарплату агента в массив
                average_salary += result['salary']  # считаем среднюю зарплату
            average_salary = average_salary / len(results)  # средняя зарплата
            average_salary = average_salary.__round__(2)  # округляем до 2 знаков после запятой

            # массивы для графика сумм сделок по видам страховок
            labels_auto = []
            data_auto = []
            labels_health = []
            data_health = []
            labels_property = []
            data_property = []
            print(agents)
            for agent in agents:
                auto_insurances = AutoInshurance.objects.filter(agent=agent, date__gte=start_date, date__lte=end_date)
                health_insurances = HealthInshurance.objects.filter(agent=agent, date__gte=start_date,
                                                                    date__lte=end_date)
                property_insurances = PropertyInshurance.objects.filter(agent=agent, date__gte=start_date,
                                                                        date__lte=end_date)
                labels_auto.append(agent.first_name + ' ' + agent.last_name)
                temp = []
                for auto_insurance in auto_insurances:
                    temp.append(auto_insurance.salary)
                try:
                    data_auto.append(sum(temp) / auto_insurances.count())
                except:
                    data_auto.append(0)
                labels_health.append(agent.first_name + ' ' + agent.last_name)
                temp = []
                for health_insurance in health_insurances:
                    temp.append(health_insurance.salary)
                try:
                    data_health.append(sum(temp) / len(temp))
                except:
                    data_health.append(0)
                labels_property.append(agent.first_name + ' ' + agent.last_name)
                temp = []
                for property_insurance in property_insurances:
                    temp.append(property_insurance.salary)
                try:
                    data_property.append(sum(temp) / len(temp))
                except:
                    data_property.append(0)

        return render(request, 'salary_report.html',
                      {'form': form, 'results': results, 'labels': labels, 'data': data,
                       'average_salary': average_salary,
                       'labels_auto': labels_auto, 'data_auto': data_auto, 'labels_health': labels_health,
                       'data_health': data_health, 'labels_property': labels_property, 'data_property': data_property})



    else:
        form = SalaryReportForm()

    return render(request, 'salary_report.html',
                  {'form': form, 'results': results})


# функция для страницы со списком агентов
def agents(request):
    agents = User.objects.filter(role__name='Агент')  # получаем агентов
    return render(request, 'agents.html', {'agents': agents})


# функция для страницы с документом автостраховки
def doc_auto_insurance(request, insurance_id):
    insurance = AutoInshurance.objects.get(id=insurance_id)
    agent_salary = int(insurance.salary * insurance.percent_agent / 100)
    return render(request, 'doc_auto_insurance.html', {'insurance': insurance, 'agent_salary': agent_salary})


# функция для страницы с документом медицинской страховки
def doc_health_insurance(request, insurance_id):
    insurance = HealthInshurance.objects.get(id=insurance_id)
    agent_salary = int(insurance.salary * insurance.percent_agent / 100)
    return render(request, 'doc_health_insurance.html', {'insurance': insurance, 'agent_salary': agent_salary})


# функция для страницы с документом имущественной страховки
def doc_property_insurance(request, insurance_id):
    insurance = PropertyInshurance.objects.get(id=insurance_id)
    agent_salary = int(insurance.salary * insurance.percent_agent / 100)
    return render(request, 'doc_property_insurance.html', {'insurance': insurance, 'agent_salary': agent_salary})
