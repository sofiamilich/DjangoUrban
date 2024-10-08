from django.shortcuts import render
from .forms import UserRegister
from django.template.exceptions import TemplateDoesNotExist



def sign_up_by_django(request):
    users = ['user1', 'user2', 'user3']
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        print("Данные, полученные из формы:", request.POST)
        if form.is_valid():
            print("Форма валидна!")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            print(f"Username: {username}, Age: {age}")

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                print("Пароли не совпадают")

            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
                print("Возраст меньше 18 лет")
            elif username in users:
                info['error'] = 'Пользователь уже существует'
                print("Пользователь уже существует")
            else:
                info['message'] = f'Приветствуем, {username}!'
                print(f"Регистрация прошла успешно: {username}")

        else:
            print("Форма невалидна, ошибки:", form.errors)

        info['form'] = form
    else:
        info['form'] = UserRegister()
    return render(request, 'fifth_task/registration_page.html', info)

def sign_up_by_html(request):
    users = ['user1', 'user2', 'user3']
    info = {}
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            repeat_password = request.POST.get('repeat_password')
            age = int(request.POST.get('age'))  # Преобразование в целое число

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                info['message'] = f'Приветствуем, {username}!'
        return render(request, 'fifth_task/registration_page.html', info)
    except TemplateDoesNotExist as e:
        print(e)
        print(e.args)
        raise e