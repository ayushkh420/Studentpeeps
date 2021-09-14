from django.contrib import admin
from .models import RequestBrand, Contact, Foundation, Resource


# Register your models here.

admin.site.register(Contact)
admin.site.register(RequestBrand)
admin.site.register(Foundation)
admin.site.register(Resource)

