from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from commerce import api_views

router = DefaultRouter()
# router.register(r'user', api_views.UserViewSet)
router.register(r'category', api_views.CategoryViewSet)
router.register(r'item', api_views.ItemViewSet)
router.register(r'coupon', api_views.CouponViewSet)
router.register(r'order', api_views.OrderViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'api-auth', include('rest_framework.urls')),
]