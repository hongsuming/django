from django.contrib import admin
from sangpumapp.models import Maker, Product

# Register your models here.
class MakerAdmin(admin.ModelAdmin):
    list_display = ('id', 'm_name', 'm_tel', 'm_addr')

admin.site.register(Maker, MakerAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'p_name', 'p_price', 'maker_name')

admin.site.register(Product, ProductAdmin)