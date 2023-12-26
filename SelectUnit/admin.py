from django.contrib import admin
from .models import SelectUnit
# Third Party
from nested_admin import NestedModelAdmin


@admin.register(SelectUnit)
class SelectUnits_admin(admin.ModelAdmin):
    
    list_display = ['id','title', 'student','num_unit', 'created_at','is_active']
    
    def student(self, obj):
        return ([x for x in obj.student.all()])
    list_display_links = ("id", "title")
    filter_horizontal = ['lesson']
    search_fields = ['title']
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)
    