# coding=utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Category(models.Model):
	name = models.CharField(max_length=50)
	parent = models.ForeignKey('self', null=True, blank=True)

	def __str__(self):
		return self.name


@python_2_unicode_compatible
class Item(models.Model):
	category = models.ManyToManyField(Category, related_name='items')
	name = models.CharField(max_length=50)
	price = models.FloatField()
	stock = models.IntegerField()
	description = models.TextField()

	def __str__(self):
		return self.name

	def delete_image(self, image_id):
		"""
		Delete the given image from item's image list
		:param image_id: id of the Image model instance
		:return: boolean indicating whether or not the deletion completes
		"""
		queryset = self.images.filter(pk=image_id)
		if not len(queryset):
			return False
		queryset.delete()
		return True


class Image(models.Model):
	image = models.ImageField()
	item = models.ForeignKey(Item, related_name='images')


class Coupon(models.Model):
	COUPON_TYPES = [('r', 'ratio'), ('f', 'fixed')]
	type = models.CharField(max_length=1, choices=COUPON_TYPES)
	ratio = models.FloatField(default=1)
	amount = models.FloatField(default=0)
	threshold = models.FloatField(default=0)
	start = models.DateTimeField()
	end = models.DateTimeField()
	name = models.CharField(max_length=50)
	image = models.ImageField(blank=True, null=True)


class Order(models.Model):
	STATUS_TABLE = [
		(-1, 'payment failed'),
		(0, 'payment pending'),
		(1, 'not shipped'),
		(2, 'shipped'),
		(3, 'complete')
	]
	item = models.ForeignKey(Item, related_name='orders')
	count = models.IntegerField()
	placer = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		related_name='orders',
	)
	status = models.IntegerField(choices=STATUS_TABLE, default=0)
	place_date = models.DateTimeField(auto_now_add=True)
	modify_date = models.DateTimeField(auto_now=True)


class Cart(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
