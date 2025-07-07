from django.contrib import admin
from .models import Budget, Income, Category, Expenses

# Register your models here.

admin.site.register(Budget)
admin.site.register(Income)
admin.site.register(Category)
admin.site.register(Expenses)