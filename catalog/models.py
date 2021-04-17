from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import uuid  # Required for unique book instances


# Create your models here.


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
                                     blank=True, default='q', help_text='Форма обучения - указать: очно/ очно-заочно/ заочно')
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
                                     blank=True, default='q', help_text='Форма обучения - указать: очно/ очно-заочно/ заочно')
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


class Book(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN', max_length=13,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    # genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")

    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('book-detail', args=[str(self.id)])

    # def display_genre(self):
    #     """
    #     Creates a string for the Genre. This is required to display genre in Admin.
    #     """
    #     return ', '.join([genre.name for genre in self.genre.all()[:3]])


class BookInstance(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s (%s)' % (self.id, self.book.title)


class Author(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)
