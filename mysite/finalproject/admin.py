from django.contrib import admin
from .models import Post, Contact, Newsletter

# Register your models here.


admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(Newsletter)