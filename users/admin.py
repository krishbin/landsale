from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .base_form import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    readonly_fields = ('username','password','first_name','last_name','email', 'gender','phone_number','location','profile_picture',)
    list_display = ('username', 'is_staff', 'is_active','gender','phone_number','location','profile_picture',)
    list_filter = ('username', 'is_staff', 'is_active','gender','phone_number','location','profile_picture',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email','gender','phone_number','location','profile_picture',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_superuser', 'groups', 'user_permissions',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','first_name','last_name', 'password1', 'password2', 'is_staff', 'is_active','gender','phone_number','location','profile_picture',)}
        ),
    )
    search_fields = ('username',)
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)
