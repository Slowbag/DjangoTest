from django.contrib import admin
from .models import Student, SpecialtyBydhet, ConstructZapros, ConstructOtchetov


# Register your models here.
@admin.register(ConstructOtchetov)
class ConstructOtchetovAdmin(admin.ModelAdmin):
    list_display = ('Model1', 'Model2', 'Model3', 'Model4', 'Model5', 'Model6',
                    'Model7', 'Model8', 'Model9', 'Model10')


@admin.register(ConstructZapros)
class ConstructZaprosAdmin(admin.ModelAdmin):
    list_display = ('Model1', 'Model2', 'Model3', 'Model4', 'Model5', 'Model6',
                    'Model7', 'Model8', 'Model9', 'Model10')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('Surname', 'Name', 'Patronymic', 'Date_of_birth',
                    'Place_of_birth', 'Citizenship', 'Identity_document',
                    'When_issued', 'Issued_by', 'residing_at_the_address', 'personal_phone')
    # fields = [ 'Identity_document', 'personal_phone', ('Date_of_birth', 'Place_of_birth')]


@admin.register(SpecialtyBydhet)
class SpecialtyBydhetAdmin(admin.ModelAdmin):
    list_display = ('id', 'Specialty_name', 'Form_of_study', 'Training_period', 'Basic_education')



