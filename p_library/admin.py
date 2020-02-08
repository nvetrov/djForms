from django.contrib import admin

# Register your models here.
from .models import (Book, Author, Friend)

[admin.site.register(item) for item in (Book, Author, Friend)]