from django.db import models
# Create your models here.

class Index(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
        
class Steps(models.Model):
    img = models.ImageField(
        upload_to='steps/', 
        verbose_name='Фото'
    )
    name_des = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
       
    description = models.TextField(
        verbose_name='Описание'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Длительность'
    ) 
    num = models.CharField(
        max_length=255,
        verbose_name='Цена'   
    )
    
    def __str__(self):
        return f'{self.img}'
    
    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направление'

class Contact(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    phone = models.CharField(
        max_length=255,
        verbose_name='Номер телефона'
    )
    email = models.EmailField(
        verbose_name='Email'
    )
    ig = models.URLField(
        verbose_name='Instagram'
    )
    address = models.CharField(
        verbose_name='Адрес',
        max_length=255
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

class TelegramUser(models.Model):
    id_user = models.CharField(
        max_length=100,
        verbose_name="ID пользователя telegram"
    )
    email = models.EmailField(
        verbose_name="email", 
        max_length=254
    )
    
    username = models.CharField(
        max_length=255,
        verbose_name="Имя пользователя",
        blank=True, null=True
    )
    first_name = models.CharField(
        max_length=255,
        verbose_name="Имя",
        blank=True, null=True
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name="Фамилия",
        blank=True, null=True
    )
    chat_id = models.CharField(
        max_length=100,
        verbose_name="Чат ID"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата регистрации"
    )

    def __str__(self):
        return str(self.username)
    
    class Meta:
        verbose_name = "Пользователь телеграм"
        verbose_name_plural = "Пользователи телеграма"

class Form(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=50)
    email = models.EmailField(verbose_name="email", max_length=254)
    phone = models.BigIntegerField(verbose_name="Номер телефона")
    message = models.TextField(verbose_name="Письмо")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
    
