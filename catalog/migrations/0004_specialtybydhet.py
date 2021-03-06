# Generated by Django 3.2 on 2021-04-16 21:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20210416_2243'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialtyBydhet',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='№ п/п', primary_key=True, serialize=False)),
                ('Specialty_name', models.CharField(blank=True, choices=[('m', 'Сетевое и системное администрирование'), ('o', 'Информационные системы и программирование (инф. сист.)'), ('a', 'Информационные системы и программирование (web)'), ('r', 'Информационные системы и программирование (о-з)'), ('t', 'Обеспечение информационной безопасности автоматизированных систем')], default='m', help_text='Наименование специалитета', max_length=1)),
                ('Form_of_study', models.CharField(blank=True, choices=[('q', 'очная'), ('w', 'очно-заочная'), ('e', 'заочная')], default='q', help_text='Форма обучения - указать: очно/ очно-заочно/ заочно', max_length=1)),
                ('Training_period', models.CharField(blank=True, choices=[('z', '3 года 10 мес.'), ('x', '2 года 10 мес.')], default='z', help_text='Срок обучения', max_length=1)),
                ('Basic_education', models.CharField(blank=True, choices=[('o', '9 классов'), ('p', '11 классов')], default='o', help_text='Базовое образование', max_length=1)),
            ],
        ),
    ]
