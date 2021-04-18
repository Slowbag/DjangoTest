# Generated by Django 3.2 on 2021-04-18 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_delete_constructabiturient'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConstructOtchetov',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Model1', models.TextField(help_text='Приложение № 3 к распоряжению ДПО ТО от 15 Августа 2018 г. № ____', max_length=100)),
                ('Model2', models.CharField(help_text=' Информация о приеме в разрезе специальностей на 15 Августа 2018 г.', max_length=100)),
                ('Model3', models.CharField(help_text='информация об образовательной программе', max_length=100)),
                ('Model4', models.CharField(help_text='прием документов ', max_length=100)),
                ('Model5', models.CharField(help_text='зачисление', max_length=100)),
                ('Model6', models.CharField(help_text='№ п/п', max_length=100)),
                ('Model7', models.CharField(help_text='Наименование специальности', max_length=100)),
                ('Model8', models.CharField(help_text='форма обучения - указать: очно/ очно-заочно/ заочно', max_length=100)),
                ('Model9', models.CharField(help_text='срок обучения', max_length=100)),
                ('Model10', models.CharField(help_text='базовое образование', max_length=100)),
            ],
            options={
                'verbose_name': 'Конструктор отчетов',
                'verbose_name_plural': 'Конструктор отчетов',
            },
        ),
    ]