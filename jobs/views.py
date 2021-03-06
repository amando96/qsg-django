from django.shortcuts import get_object_or_404, render
from django.http import Http404
from jobs.models import Salary, Company, District, Position
from django.db.models import Avg, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from utils import search

def index(request):
	return render(request, 'jobs/index.html',{'path' : request.path })

def privacy(request):
	return render(request, 'jobs/privacy.html',{'path' : request.path})

def submit(request):
	districts = District.objects.all()
	return render(request, 'jobs/submit.html',{'path' : request.path, 'districts' : districts })

def search_form(request):
	if 'by' in request.GET and 's' in request.GET:
		by = request.GET['by']
		s = request.GET['s']
		if by == 'all':
			result_list = search(request, s, s, s)
		elif by == 'district':
			 result_list = search(request, s, '*', '*')
		elif by == 'company':
			 result_list = search(request, '*', s, '*')
		elif by == 'position':
			 result_list = search(request, '*', '*', s)
	else:	
		result_list = search(request, '*', '*', '*')

	paginator = Paginator(result_list, 25)
	page = request.GET.get('page')
	try:	
		results = paginator.page(page)
	except PageNotAnInteger:
		results = paginator.page(1)
		print ('shit')
	except EmptyPage:
		results = paginator.page(paginator.num_pages)
		
	all_sal_avg = Salary.objects.aggregate(Avg('salary_value')).values()[0]
	return render(request, 'jobs/search.html', {'results' : results, 'all_sal_avg' : all_sal_avg, 'path' : request.path })

def make_search(request):
	results = Salary.objects.order_by('pk')[:10]
	all_sal_avg = Salary.objects.aggregate(Avg('salary_value')).values()[0]
	return render(request, 'jobs/search_results.html', {'results' : results, 'all_sal_avg' : all_sal_avg })

def company_detail(request, company_id):
	try:
		company = Company.objects.get(pk=company_id)
		sal_cnt = Salary.objects.all().filter(salary_company=company_id).count()
		all_sal_avg = Salary.objects.filter(~Q(salary_company=company_id)).aggregate(Avg('salary_value')).values()[0]
		company_sal_avg = Salary.objects.filter(salary_company=company_id).aggregate(Avg('salary_value')).values()[0]
		company_salaries = Salary.objects.filter(salary_company=company_id)
	except Company.DoesNotExist:
		raise Http404
	return render(request, 'jobs/company_detail.html', {'company' : company, 'sal_cnt' : sal_cnt, 'company_sal_avg': company_sal_avg, 'all_sal_avg' : all_sal_avg, 'salaries' : company_salaries })

def district_detail(request, district_id):
	try:
		district = District.objects.get(pk=district_id)
		sal_cnt = Salary.objects.all().filter(salary_district=district_id).count()
		all_sal_avg = Salary.objects.filter(~Q(salary_district=district_id)).aggregate(Avg('salary_value')).values()[0]
		district_sal_avg = Salary.objects.filter(salary_district=district_id).aggregate(Avg('salary_value')).values()[0]
		district_salaries = Salary.objects.filter(salary_district=district_id)
	except District.DoesNotExist:
		raise Http404
	return render(request, 'jobs/district_detail.html', {'district' : district, 'sal_cnt' : sal_cnt, 'district_sal_avg' : district_sal_avg, 'all_sal_avg' : all_sal_avg, 'salaries' : district_salaries })

def position_detail(request, position_id):	
	try:
		position = Position.objects.get(pk=position_id)
		sal_cnt = Salary.objects.all().filter(salary_position=position_id).count()
		all_sal_avg = Salary.objects.filter(~Q(salary_position=position_id)).aggregate(Avg('salary_value')).values()[0]
		position_sal_avg = Salary.objects.filter(salary_position=position_id).aggregate(Avg('salary_value')).values()[0]
		position_salaries = Salary.objects.filter(salary_position=position_id)
	except Position.DoesNotExist:
		raise Http404
	return render(request, 'jobs/position_detail.html', {'position' : position, 'sal_cnt' : sal_cnt, 'position_sal_avg' : position_sal_avg, 'all_sal_avg' : all_sal_avg, 'salaries' : position_salaries })





















