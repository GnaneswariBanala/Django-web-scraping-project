from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Useradd,Contact
class ContactAdmin(admin.ModelAdmin):

    
    list_display=("name","email","is_resolved","created_at")
    list_filter=("is_resolved","created_at")
    






# Register your models here.
admin.site.register(Useradd)


admin.site.register(Contact,ContactAdmin)
