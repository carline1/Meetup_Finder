from django.contrib import admin

# Register your models here.
from .models import Eventlist, Userlist, Taglist

admin.site.register(Eventlist)
admin.site.register(Userlist)
admin.site.register(Taglist)
