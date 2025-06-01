from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'completed')
    list_filter = ('completed', 'user')
    search_fields = ('title', 'user__username')

admin.site.register(Todo, TodoAdmin)