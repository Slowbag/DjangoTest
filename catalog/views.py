from django.shortcuts import render

from .models import Student, ConstructZapros, ConstructOtchetov


# Create your views here.


def index(request):
    """
        Функция отображения для домашней страницы сайта.
        """
    # Генерация "количеств" некоторых главных объектов
    s_name = Student.objects.all()
    c_name = ConstructZapros.objects.all()
    num_student = Student.objects.all().count()

    # Отрисовка HTML-шаблона index.html с данными внутри

    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'s_name': s_name, 'c_name': c_name, 'num_student': num_student})


def otchet_abit(request):
    """
        Функция отображения для домашней страницы сайта.
        """
    # Генерация "количеств" некоторых главных объектов
    s_name = Student.objects.all()
    co_name = ConstructOtchetov.objects.all()
    num_student = Student.objects.all().count()

    # Отрисовка HTML-шаблона index.html с данными внутри

    # переменной контекста context
    return render(
        request,
        'otchet_abit.html',
        context={'s_name': s_name, 'co_name': co_name, 'num_student': num_student})
