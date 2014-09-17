from models import Salary, Company, District, Position
from django.db.models import Q

def search(request, district = '*', company = '*', position = '*'):
	if district == '*' and company == '*' and position == '*':
		result_list = Salary.objects.all()
	elif district == '*' and company == '*' and position != '*':
		result_list = Salary.objects.filter(salary_position__position_name__icontains=position)
	elif district == '*' and company != '*' and position == '*':
		result_list = Salary.objects.filter(salary_company__company_name__icontains=company)
	elif district != '*' and company == '*' and position == '*':
		result_list = Salary.objects.filter(salary_district__district_name__icontains=district)
	elif district != '*' and company != '*' and position != '*':
		result_list = Salary.objects.filter(Q(salary_district__district_name__icontains=district) | Q(salary_company__company_name__icontains=company) | Q(salary_position__position_name__icontains=position))
		
	return result_list
