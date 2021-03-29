from django.contrib import admin

from .forms import ComicForm
from .models import Comic


@admin.register(Comic)
class ComicAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'status')
    form = ComicForm
