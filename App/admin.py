from django.contrib import admin
from django.contrib import messages
from django.contrib.auth.models import User, Group
from .models import *

admin.site.unregister(Group)

admin.site.site_header = "PyGod"
admin.site.site_title = "Site Title"
admin.site.site_url = "http://siteurl.com"
admin.site.index_title = "Dashboard"


class Custom_Feedback(admin.ModelAdmin):
    list_display = ['email', 'phone', 'message', 'status']  # object will represnt with this value
    exclude = ['email']
    search_fields = ["email__startswith", "email__contains"]  # search bar
    
    def has_add_permission(self, request):  # remove add product option
        return False

    # List operation creation (in select box)
    def make_active(modeladmin, request, queryset):
        queryset.update(status = True)
        messages.success(request, "Selected Record(s) Marked as Active Successfully !!") 
  
    def make_inactive(modeladmin, request, queryset): 
        queryset.update(status = False)
        messages.success(request, "Selected Record(s) Marked as Inactive Successfully !!")
    
    admin.site.add_action(make_active, "Make Active") 
    admin.site.add_action(make_inactive, "Make Inactive")


admin.site.register(Feedback, Custom_Feedback)
