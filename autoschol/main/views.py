from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from main.models import *


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'index')
            return redirect(next_url)

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('index')


def groups(request):
    groups = Group.objects.all()
    return render(request, 'groups.html', {'groups': groups})


def programs(request):
    programs = Program.objects.all()
    return render(request, 'programs.html', {'programs': programs})


def add_program(request):
    if request.method == 'POST':
        category_id = int(request.POST['category'])
        category = Category.objects.get(id=category_id)
        hours = request.POST['hours']
        price = request.POST['price']
        program = Program.objects.create(category=category, hours=hours, price=price)
        return redirect('programs')
    else:
        categories = Category.objects.all()
        return render(request, 'add_program.html', {'categories': categories})


def edit_program(request, program_id):
    program = Program.objects.get(id=program_id)
    if request.method == 'POST':
        category_id = int(request.POST['category'])
        category = Category.objects.get(id=category_id)
        hours = request.POST['hours']
        price = request.POST['price']
        program.category = category
        program.hours = hours
        program.price = price
        program.save()
        return redirect('programs')
    else:
        categories = Category.objects.all()
        return render(request, 'edit_program.html', {'categories': categories, 'program': program})


def delete_program(request, program_id):
    program = Program.objects.get(id=program_id)
    program.delete()
    return redirect('programs')


def add_group(request):
    if request.method == 'POST':
        name = request.POST['name']
        program_id = int(request.POST['program'])
        program = Program.objects.get(id=program_id)
        time = request.POST['time']
        date = request.POST['date']
        teacher = request.POST['teacher']
        teacher = User.objects.get(id=teacher)
        group = Group.objects.create(program=program, time=time, date=date, teacher=teacher, name=name)
        return redirect('groups')
    else:
        programs = Program.objects.all()
        teachers = User.objects.filter(role__name='Преподаватель')
        return render(request, 'add_group.html', {'programs': programs, 'teachers': teachers})


def edit_group(request, group_id):
    group = Group.objects.get(id=group_id)
    if request.method == 'POST':
        name = request.POST['name']
        program_id = int(request.POST['program'])
        program = Program.objects.get(id=program_id)
        time = request.POST['time']
        date = request.POST['date']
        teacher = request.POST['teacher']
        teacher = User.objects.get(id=teacher)
        group.program = program
        group.name = name
        group.time = time
        group.date = date
        group.teacher = teacher
        group.save()
        return redirect('groups')
    else:
        programs = Program.objects.all()
        teachers = User.objects.filter(role__name='Преподаватель')
        date = group.date.strftime('%Y-%m-%d')
        group.date = date
        time = group.time.strftime('%H:%M')
        group.time = time
        return render(request, 'edit_group.html', {'programs': programs, 'teachers': teachers, 'group': group})


def delete_group(request, group_id):
    group = Group.objects.get(id=group_id)
    group.delete()
    return redirect('groups')


def instructors(request):
    # объединение таблиц
    instructors = User.objects.filter(role__name='Инструктор').values('first_name', 'last_name', 'exp',
                                                                      'employment_date', 'car__name',
                                                                      'car__year', 'car__mileage')

    return render(request, 'instructors.html', {'instructors': instructors})


def students(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})


def add_student(request):
    if request.method == 'POST':
        birthday = request.POST['birthday']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        middle_name = request.POST['middle_name']
        phone_number = request.POST['phone']
        serial_number = request.POST['serial_number']
        number = request.POST['number']
        group_id = int(request.POST['group'])
        group = Group.objects.get(id=group_id)
        instructor = request.POST['instructor']
        instructor = User.objects.get(id=instructor)
        student = Student.objects.create(first_name=first_name, last_name=last_name, phone=phone_number,
                                         birthday=birthday, middle_name=middle_name, serial_number=serial_number,
                                         number=number, group=group, instructor=instructor)
        return redirect('students')
    else:
        instructors = User.objects.filter(role__name='Инструктор')
        groups = Group.objects.all()
        return render(request, 'add_student.html', {'groups': groups, 'instructors': instructors})


def group(request, group_id):
    group = Group.objects.get(id=group_id)
    students = Student.objects.filter(group=group)
    return render(request, 'group.html', {'group': group, 'students': students})


def add_exam(request):
    if request.method == 'POST':
        type_exam_id = int(request.POST['type_exam'])
        type_exam = TypeExam.objects.get(id=type_exam_id)
        examiner_first_name = request.POST['examiner_first_name']
        examiner_last_name = request.POST['examiner_last_name']
        examiner_middle_name = request.POST['examiner_middle_name']
        time = request.POST['time']
        date = request.POST['date']
        exam = Exam.objects.create(type_exam=type_exam, examiner_first_name=examiner_first_name,
                                   examiner_last_name=examiner_last_name,
                                   examiner_middle_name=examiner_middle_name, time=time, date=date)
        return redirect('students')
    else:
        type_exams = TypeExam.objects.all()
        return render(request, 'add_exam.html', {'students': students, 'type_exams': type_exams})


def exams(request):
    exams = Exam.objects.all()
    return render(request, 'exams.html', {'exams': exams})


def edit_exam(request, exam_id):
    exam = Exam.objects.get(id=exam_id)
    if request.method == 'POST':
        type_exam_id = int(request.POST['type_exam'])
        type_exam = TypeExam.objects.get(id=type_exam_id)
        examiner_first_name = request.POST['examiner_first_name']
        examiner_last_name = request.POST['examiner_last_name']
        examiner_middle_name = request.POST['examiner_middle_name']
        time = request.POST['time']
        date = request.POST['date']
        exam.type_exam = type_exam
        exam.examiner_first_name = examiner_first_name
        exam.examiner_last_name = examiner_last_name
        exam.examiner_middle_name = examiner_middle_name
        exam.time = time
        exam.date = date
        exam.save()
        return redirect('exams')
    else:
        type_exams = TypeExam.objects.all()
        date = exam.date.strftime('%Y-%m-%d')
        exam.date = date
        time = exam.time.strftime('%H:%M')
        exam.time = time
        exam.examiner_middle_name = exam.examiner_middle_name
        return render(request, 'edit_exam.html', {'type_exams': type_exams, 'exam': exam})


def delete_exam(request, exam_id):
    exam = Exam.objects.get(id=exam_id)
    exam.delete()
    return redirect('exams')


def create_results_exams(request):
    if request.method == 'POST':
        exam_id = int(request.POST['exam'])
        exam = Exam.objects.get(id=exam_id)
        student = request.POST['student']
        student = Student.objects.get(id=student)
        result = request.POST.get('result') == 'on'
        Result.objects.create(exam=exam, student=student, result=result)
        return redirect('results_exams')
    else:
        exams = Exam.objects.all()
        students = Student.objects.all()
        return render(request, 'create_results_exams.html', {'exams': exams, 'students': students})


def results_exams(request):
    results = Result.objects.all()
    return render(request, 'results_exams.html', {'results': results})
