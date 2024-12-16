from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty', 'review', 'image') 
    search_fields = ('name', 'faculty', 'review')          
    list_filter = ('faculty',)                             
    ordering = ('name',)                                   
