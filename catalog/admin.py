from django.contrib import admin
from .models import Author, Book, BookInstance, Student, SpecialtyBydhet


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('Surname', 'Name', 'Patronymic', 'Date_of_birth',
                    'Place_of_birth', 'Citizenship', 'Identity_document',
                    'When_issued', 'Issued_by', 'residing_at_the_address', 'personal_phone')
    # fields = [ 'Identity_document', 'personal_phone', ('Date_of_birth', 'Place_of_birth')]


@admin.register(SpecialtyBydhet)
class SpecialtyBydhetAdmin(admin.ModelAdmin):
    list_display = ('id', 'Specialty_name', 'Form_of_study', 'Training_period', 'Basic_education')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'display_genre')
#     inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
