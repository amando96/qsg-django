from django.contrib import admin
from jobs.models import District,Company,Position,Gender,Salary

class SalaryAdmin(admin.ModelAdmin):
	list_display = ('salary_value', 'salary_district', 'salary_company', 'salary_position', 'salary_gender')
	

admin.site.register(District)
admin.site.register(Company)
admin.site.register(Position)
admin.site.register(Gender)
admin.site.register(Salary, SalaryAdmin)

