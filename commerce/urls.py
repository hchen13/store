from django.conf.urls import include, url

urlpatterns = [
	url(r'^api/', include('commerce.api_urls')),
	url(r'api-auth', include('rest_framework.urls')),
]