# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

# Local
from .models import Roles
# Third Party
from nested_admin import NestedModelAdmin



User = get_user_model()


class MyUserAdmin(UserAdmin, NestedModelAdmin):
    # OverWrite
    fieldsets = (
        (_('personal info'), {"fields": ('phone_number', 'password','role','name', 'email', 'nick_name', 'avatar', 'birthday', 'gender')}),
        (_('permissions'), {"fields": ('is_active','is_superuser', 'user_permissions')}),
        (_('important dates'), {"fields": ('date_joined',)}),
    )
    
    # OverWrite
    add_fieldsets = [
        ("اطلاعات اولیه", {
            'classes': ('wide',),
            "fields": ('phone_number', 'password1', 'password2')
        })
    ]

    list_display = ('id', 'phone_number', 'email','role')
    search_fields = ('phone_number__exact',)
    ordering = ('id',)
    list_filter = ('is_superuser', 'is_active', 'date_joined')

    def email_view(self, obj):
        return obj.email
    
    email_view.empty_value_display = 'No known email'

    def phone_view(self, obj):
        return obj.phone_number
    
    phone_view.empty_value_display = 'No known phone'

    def get_search_results(self, request, queryset, search_term):
        queryset, may_have_duplicates = super().get_search_results(
            request, queryset, search_term)
        try:
            search_term_as_int = int(search_term)
        except ValueError:
            pass
        else:
            queryset |= self.model.objects.filter(
                phone_number=search_term_as_int)
        return queryset, may_have_duplicates


@admin.register(Roles)
class Roles_Admin(NestedModelAdmin):
    list_display = ['title','is_active','description','created_at','updated_at']
    search_fields = ['title']
    ordering = ('id',)
    

admin.site.unregister(Group)
admin.site.register(User, MyUserAdmin)
