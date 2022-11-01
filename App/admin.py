from django.contrib import admin
from .models import Job, Location, Skills, Author
# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'salary', 'date')
    list_filter = ('date', 'salary')
    search_fields = ('title',)

admin.site.register(Job, JobAdmin)
admin.site.register(Location)
admin.site.register(Skills)
admin.site.register(Author)