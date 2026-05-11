from django.contrib import admin
from api.models import company,Employee
#admin,admin123
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','type')
    search_fields=('name',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','email','company')
    

admin.site.register(company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)
