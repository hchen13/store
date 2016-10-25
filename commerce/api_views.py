import rest_framework.status
from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import detail_route, api_view, list_route, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.serializers import Serializer, ObjectDoesNotExist
from django.conf import settings

from commerce.models import Category, Item, Image, Coupon, Order
from commerce.serializers import CategorySerializer, ItemSerializer, ImageSerializer, CouponSerializer, UserSerializer, \
	OrderSerializer


class CategoryViewSet(viewsets.ModelViewSet):
	"""
	Category CRUD operation APIs
	"""
	queryset = Category.objects.all()
	serializer_class = CategorySerializer


class ItemViewSet(viewsets.ModelViewSet):
	"""
	item CRUD operation APIs

	"""
	queryset = Item.objects.all()
	serializer_class = ItemSerializer

	@detail_route(
		methods=['POST'],
		serializer_class=ImageSerializer,
		url_path='image'
	)
	def upload_image(self, request, pk=None):
		"""
		upload item image API
		---

		"""
		item = self.get_object()
		serializer = ImageSerializer(data=request.data)
		if serializer.is_valid():
			image_file = serializer.validated_data['image']
			Image.objects.create(item=item, image=image_file)
			return Response(data={
				"message": "upload complete"
			})

		return Response(data=serializer.errors, status=400)

	@detail_route(methods=['DELETE', 'PUT'], serializer_class=ImageSerializer, url_path='image/(?P<image_id>\d+)')
	def update_image(self, request, pk=None, image_id=None):
		if request.method == 'DELETE':
			return self.delete_image(request, pk, image_id)
		return self.replace_image(request, pk, image_id)

	# @detail_route(methods=['DELETE'], url_path='image/(?P<image_id>\d+)')
	def delete_image(self, request, pk=None, image_id=None):
		"""
		Delete item image API
		"""
		item = self.get_object()
		result = item.delete_image(image_id)
		if not result:
			return Response(status=400, data="delete failed")
		return Response(data="delete complete")

	# @detail_route(methods=['PUT'], url_path='image/(?P<image_id>\d+)', serializer_class=ImageSerializer)
	def replace_image(self, request, pk=None, image_id=None):
		"""
		Update item image API
		"""
		try:
			image_model = Image.objects.get(item__pk=pk, pk=image_id)
		except Image.DoesNotExist:
			err_msg = "image {0} for item {1} not found".format(image_id, pk)
			return Response(status=404, data=err_msg)

		serializer = ImageSerializer(data=request.data)
		if serializer.is_valid():
			uploaded_image = serializer.validated_data['image']
			image_model.image = uploaded_image
			image_model.save()
			return Response(data='update complete')
		return Response(data=serializer.errors, status=400)


class CouponViewSet(viewsets.ModelViewSet):
	queryset = Coupon.objects.all()
	serializer_class = CouponSerializer


class UserViewSet(viewsets.ModelViewSet):
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer


class OrderViewSet(viewsets.ModelViewSet):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer
	permission_classes = [IsAuthenticated, ]

	def list(self, request, *args, **kwargs):
		queryset = self.get_queryset().filter(placer=request.user)

		page = self.paginate_queryset(queryset)
		if page is not None:
			serializer = self.get_serializer(page, many=True)
			return self.get_paginated_response(serializer.data)

		serializer = self.get_serializer(queryset, many=True)
		return Response(serializer.data)

	# def retrieve(self, request, *args, **kwargs):
	# 	return Response()

	@list_route(methods=['POST'], permission_classes=[IsAuthenticated])
	def place(self, request):
		serializer = self.get_serializer(data=request.data)
		if serializer.is_valid():
			# create a new order instance with the user that sends the request
			# and the status to 0: payment pending
			user = request.user
			serializer.save(placer=user, status=0)
			return Response(serializer.data)
		return Response(serializer.errors, status=400)