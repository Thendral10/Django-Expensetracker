from django.contrib import admin
from .models import Expense
from .models import Users
# Register your models here.
admin.site.register(Expense)
admin.site.register(Users)