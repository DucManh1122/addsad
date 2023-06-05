from django.contrib import admin
from .models import user_registration


class UserAdmin(admin.ModelAdmin): 
    list_display = ('fname', 'lname', 'email', 'mobile', 'password',) 
    list_display_links = ('email',) 
    list_per_page = 50 
    search_fields = ['email', 'lname','fname'] 

# Register your models here.
admin.site.register(user_registration,UserAdmin)