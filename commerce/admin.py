from django.contrib import admin

# Register your models here.
from commerce.models import Category, Item, Image, Coupon, Order


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'parent')


class ItemImageInline(admin.TabularInline):
	model = Image
	extra = 1


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
	inlines = [ItemImageInline, ]
	list_display = ['name', ]


admin.site.register(Coupon)
admin.site.register(Order)
admin.site.register(Image)