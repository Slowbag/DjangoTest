from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import uuid  # Required for unique book instances


# Create your models here.

# Конструктор запросов
class ConstructZapros(models.Model):
    """
    Model representing a Student_Zayavlenie (e.g. Science Fiction, Non Fiction).
    """
    Model1 = models.CharField(max_length=100,
                              help_text="Директору ОГБПОУ «Томский техникум информационных технологий» ")
    Model2 = models.CharField(max_length=100, help_text="проживающий(ей) по адресу")
    Model3 = models.CharField(max_length=100, help_text="Прошу принять меня в ОГБПОУ «ТТИТ» на обучение по "
                                                        "направлению подготовки (профессия / специальность) "
                                                        "1.(приоритетная профессия / специальность)")
    Model4 = models.CharField(max_length=100, help_text="(дополнительная профессия / специальность): ")
    Model5 = models.CharField(max_length=100, help_text="О себе сообщаю следующее:")
    Model6 = models.CharField(max_length=100, help_text="Окончил (а) в 2010 году:")
    Model7 = models.CharField(max_length=100, help_text="Уровень образования")
    Model8 = models.CharField(max_length=100, help_text="Документ об образовании:")
    Model9 = models.CharField(max_length=100, help_text="Английский язык")
    Model10 = models.CharField(max_length=100, help_text="Наличие договора о целевом обучении:")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.Model1

    class Meta:
        verbose_name = 'Конструктор запросов'
        verbose_name_plural = 'Конструктор запросов'
# Конструктор запросов


# Студенты
class Student(models.Model):
    """
    Model representing a Student_Zayavlenie (e.g. Science Fiction, Non Fiction).
    """
    Surname = models.CharField(max_length=30, help_text="Фамилия")
    Name = models.CharField(max_length=30, help_text="Имя")
    Patronymic = models.CharField(max_length=30, help_text="Отчество")
    Date_of_birth = models.DateField(null=True, blank=True, help_text="Дата рождения")
    Place_of_birth = models.CharField(max_length=100, help_text="Место рождения")
    Citizenship = models.CharField(max_length=100, help_text="Гражданство")
    Identity_document = models.CharField('Серия номер паспорта', max_length=10,
                                         help_text="Документ, удостоверяющий личност")
    When_issued = models.DateField(null=True, blank=True, help_text="Когда выдан")
    Issued_by = models.CharField(max_length=100, help_text="Кем выдан")
    residing_at_the_address = models.CharField(max_length=100, help_text="Проживающий(ей) по адресу")
    personal_phone = models.CharField('Номер телефона начиная с +7', max_length=11, help_text="Личный телефон")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.Surname

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('student-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Студенты'
        verbose_name_plural = 'Студенты'
# Студенты

# Специальности бюджет
class SpecialtyBydhet(models.Model):
    """
    Model representing a Specialty (e.g. Science Fiction, Non Fiction).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="№ п/п")
    LOAN_STATUS = (
        ('m', 'Сетевое и системное администрирование'),
        ('o', 'Информационные системы и программирование (инф. сист.)'),
        ('a', 'Информационные системы и программирование (web)'),
        ('r', 'Информационные системы и программирование (о-з)'),
        ('t', 'Обеспечение информационной безопасности автоматизированных систем')
    )
    Specialty_name = models.CharField(max_length=1, choices=LOAN_STATUS,
                                      blank=True, default='m', help_text='Наименование специалитета')
    LOAN_STATUS = (
        ('q', 'очная'),
        ('w', 'очно-заочная'),
        ('e', 'заочная')
    )
    Form_of_study = models.CharField(max_length=1, choices=LOAN_STATUS,
                                     blank=True, default='q',
                                     help_text='Форма обучения - указать: очно/ очно-заочно/ заочно')
    LOAN_STATUS = (
        ('z', '3 года 10 мес.'),
        ('x', '2 года 10 мес.'),
    )
    Training_period = models.CharField(max_length=1, choices=LOAN_STATUS,
                                       blank=True, default='z', help_text='Срок обучения')
    LOAN_STATUS = (
        ('o', '9 классов'),
        ('p', '11 классов'),
    )
    Basic_education = models.CharField(max_length=1, choices=LOAN_STATUS,
                                       blank=True, default='o', help_text='Базовое образование')

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.Specialty_name

    class Meta:
        verbose_name = 'Специальности бюджет'
        verbose_name_plural = 'Специальности бюджет'
# Специальности бюджет

# Специальности платные
class SpecialtyPlatnik(models.Model):
    """
    Model representing a Specialty (e.g. Science Fiction, Non Fiction).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="№ п/п")
    LOAN_STATUS = (
        ('m', 'Сетевое и системное администрирование'),
        ('o', 'Информационные системы и программирование (инф. сист.)'),
        ('a', 'Информационные системы и программирование (web)'),
        ('r', 'Информационные системы и программирование (о-з)'),
        ('t', 'Обеспечение информационной безопасности автоматизированных систем')
    )
    Specialty_name = models.CharField(max_length=1, choices=LOAN_STATUS,
                                      blank=True, default='m', help_text='Наименование специалитета')
    LOAN_STATUS = (
        ('q', 'очная'),
        ('w', 'очно-заочная'),
        ('e', 'заочная')
    )
    Form_of_study = models.CharField(max_length=1, choices=LOAN_STATUS,
                                     blank=True, default='q',
                                     help_text='Форма обучения - указать: очно/ очно-заочно/ заочно')
    LOAN_STATUS = (
        ('z', '3 года 10 мес.'),
        ('x', '2 года 10 мес.'),
    )
    Training_period = models.CharField(max_length=1, choices=LOAN_STATUS,
                                       blank=True, default='z', help_text='Срок обучения')
    LOAN_STATUS = (
        ('o', '9 классов'),
        ('p', '11 классов'),
    )
    Basic_education = models.CharField(max_length=1, choices=LOAN_STATUS,
                                       blank=True, default='o', help_text='Базовое образование')

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.Specialty_name

    class Meta:
        verbose_name = 'Специальности платные'
        verbose_name_plural = 'Специальности платные'
# Специальности платные


