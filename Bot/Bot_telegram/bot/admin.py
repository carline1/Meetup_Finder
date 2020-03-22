from django.contrib import admin

# Register your models here.
from .models import Eventlist, Userlist, Taglist, Usertaglist, Eventtaglist, Placelist

admin.site.register(Eventlist)
admin.site.register(Eventtaglist)
admin.site.register(Usertaglist)
admin.site.register(Userlist)
admin.site.register(Taglist)
admin.site.register(Placelist)