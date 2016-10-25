from django.contrib.auth import get_user_model
from rest_framework import serializers

from commerce.models import Category, Item, Image, Coupon, Order


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ('url', 'name', 'parent')


class ImageURLField(serializers.RelatedField):
	"""
	Define a custom field to represent the image
	whichever model may have a relationship to the Image model
	"""

	def to_representation(self, value):
		return value.image.url


class ImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Image
		fields = ('id', 'image', )


class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = ('url', 'id', 'category', 'name', 'price', 'stock', 'description', 'images')

	category = serializers.PrimaryKeyRelatedField(
		many=True,
		queryset=Category.objects.all()
	)
	images = ImageSerializer(many=True, read_only=True)


class CouponSerializer(serializers.ModelSerializer):
	class Meta:
		model = Coupon
		excludes = []


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = get_user_model()
		fields = ['id', 'username', 'email']


class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = ['id', 'item', 'count', 'status', 'placer']
	status = serializers.CharField(read_only=True, source='get_status_display')
	placer = UserSerializer(read_only=True)
