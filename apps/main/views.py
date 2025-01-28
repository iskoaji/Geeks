from django.shortcuts import render, redirect
from .models import Form, Index, Steps, Contact
from django.core.mail import send_mail
# Create your views here.
def index(request):
    index = Index.objects.latest('id')
    steps = Steps.objects.all()
    return render (request, 'index.html', locals())

def contact(request):
    contact = Contact.objects.latest('id')

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        send_mail(
            'Cheff Contact',
            f"""Здравствуйте.
            Спасибо за обратную связь, мы скоро свами свяжемся.
            Ваше ФИО: {name}
            Ваш email: {email}
            Ваш номер телефона: {phone}
            Ваше сообщение: {message}...

            Если вы ошиблись при указании данных можете обратно зайти на сайт и оставить новый отзыв с исправленными
            данными! """,
            "noreply@somehost.local",
            ["nurlanuuulubeksultan@gmail.com"]
        )
        Form.objects.create(name=name, email=email, phone=phone, message=message)

        return redirect('index')
    return render (request, 'index.html', locals())