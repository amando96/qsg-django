def search(request):
	result_list = Salary.objects.all()
	paginator = Paginator(result_list, 25)

	page = request.GET.get('page')
	try:	
		results = paginator.page(page)
	except PageNotAnInteger:
		results = paginator.page(1)
	except EmptyPage:
		results = paginator.page(paginator.num_pages)
	all_sal_avg = Salary.objects.aggregate(Avg('salary_value')).values()[0]
	return render(request, 'jobs/search.html', {'results' : results, 'all_sal_avg' : all_sal_avg, 'path' : request.path })
