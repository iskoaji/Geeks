from django.shortcuts import render, redirect
from apps.main.models import Form, Index, Steps, Contact
from django.core.mail import send_mail
from .service import get_text
# Create your views here.
def index(request):
    index = Index.objects.latest('id')
    steps = Steps.objects.all()
    contact = Contact.objects.latest('id')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        Form.objects.create(name=name, email=email, phone=phone, message=message)
        
        get_text(f"""
Имя отправителя: {name}
email: {email}
телефон: {phone}
Сообщение: {message}
""")
        return redirect('index')
    return render (request, 'index.html', locals())
