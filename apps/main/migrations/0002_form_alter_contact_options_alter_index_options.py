# Generated by Django 5.1.5 on 2025-01-27 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('phone', models.BigIntegerField(verbose_name='Номер телефона')),
                ('message', models.TextField(verbose_name='Письмо')),
            ],
            options={
                'verbose_name': 'Отзывы',
            },
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Контакты', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.AlterModelOptions(
            name='index',
            options={'verbose_name': 'О нас', 'verbose_name_plural': 'О нас'},
        ),
    ]
