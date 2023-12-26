# Django
from django.contrib import admin

# Local
from .models import Lessons,College,Location,Session

# Third Party
from nested_admin import NestedModelAdmin, NestedInlineModelAdmin, NestedStackedInline



class Locations_admin_inline(NestedStackedInline):
    model = Location
    extra = 0



@admin.register(College)
class Colleges_admin(admin.ModelAdmin):
    
    list_display = ['id','loc','is_active']
    def loc(self, obj):
        return ([x for x in obj.__class__.objects.all()])
    date_hierarchy = 'created_at'




@admin.register(Location)
class Locations_admin(NestedModelAdmin):
    
    list_display = ['id','loc','is_active']
    def loc(self, obj):
        return ([x for x in obj.__class__.objects.all()])
    date_hierarchy = 'created_at'


@admin.register(Session)
class Sessions_admin(NestedModelAdmin):
    
    list_display = ['id','loc']
    def loc(self, obj):
        return ([x.location for x in obj.__class__.objects.all()])
    date_hierarchy = 'created_at'

@admin.register(Lessons)
class Lessons_admin(NestedModelAdmin):
    
    list_display = ['lesson_code','title','study_group', 'teacher','loc','num_units']
    
    def loc(self, obj):
        return ([x for x in obj.sessions.all()])
    
    search_fields = ['title','lesson_code']
    filter_horizontal = ['sessions']
    date_hierarchy = 'created_at'
    #inlines = [Locations_admin,]
    readonly_fields = ('created_at',)