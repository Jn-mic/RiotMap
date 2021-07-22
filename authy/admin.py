from django.contrib import admin
from .models import Hospital, Location, Police, Post,Profile,Hotspot, Work, Data

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Hotspot)
admin.site.register(Location)
admin.site.register(Police)
admin.site.register(Work)
admin.site.register(Hospital)
admin.site.register(Data)

