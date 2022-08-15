from django.contrib import admin
from departamento.models import Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company')
    list_display_links = ('id',)
    list_editable = ('name', 'company')