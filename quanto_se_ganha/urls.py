from django.conf.urls import include, url
from django.contrib import admin
import settings
from jobs import views

urlpatterns = [
	# Examples:
	# url(r'^$', 'quanto_se_ganha.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

 	url(r'^$', include('jobs.urls')),
	url(r'^search/', views.search, name='search'),
	url(r'^company/(?P<company_id>\d+)/$', views.company_detail, name='company_detail'),
	url(r'^district/(?P<district_id>\d+)/$', views.district_detail, name='district_detail'),
	url(r'^recent/', views.make_search, name='make_search'),
	url(r'^privacy/', views.privacy, name='privacy'),
 	url(r'^admin/', include(admin.site.urls)),
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
]