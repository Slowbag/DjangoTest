# Generated by Django 3.2 on 2021-04-17 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20210417_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConstructAbiturient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Model1', models.CharField(help_text='Приложение № 3 к распоряжению ДПО ТО от 15 Августа 2018 г. № ____ ', max_length=100)),
                ('Model2', models.CharField(help_text='Информация о приеме в разрезе специальностей на 15 Августа 2018 г.', max_length=100)),
                ('Model3', models.CharField(help_text=' - по программам подготовки специалистов среднего звена ( за счёт бюджетных средств)', max_length=100)),
                ('Model4', models.CharField(help_text='информация об образовательной программе', max_length=100)),
                ('Model5', models.CharField(help_text='№ п/п', max_length=100)),
                ('Model6', models.CharField(help_text='Наименование специальности', max_length=100)),
                ('Model7', models.CharField(help_text='форма обучения - указать: очно/ очно-заочно/ заочно', max_length=100)),
                ('Model8', models.CharField(help_text='срок обучения', max_length=100)),
                ('Model9', models.CharField(help_text='базовое образование', max_length=100)),
            ],
            options={
                'verbose_name': 'Конструктор запросов абитуриентов',
                'verbose_name_plural': 'Конструктор запросов абитуриентов',
            },
        ),
    ]
