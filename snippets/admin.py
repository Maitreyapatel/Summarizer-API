from django.contrib import admin
from .models import Summary,Snippet

# Register your models here.

admin.site.register(Snippet)
admin.site.register(Summary)