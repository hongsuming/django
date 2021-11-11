from django.contrib import admin
from miniguest.models import Guest

# Register your models here.
class GuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'regdate')
    
admin.site.register(Guest, GuestAdmin)