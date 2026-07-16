from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

# Register your models here.
class UsuarioAdmin(UserAdmin):
    # Campos que se mostraran en la lista de usuarios
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    
    # Campos que se mostraran al editar un usuario
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permisos', {'fields': ('is_staff', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ('username','email','password','password2', 'is_staff', 'is_active')
        }),
    )
    
    search_fields = ('username', 'email')
    ordering = ('username',)
    
admin.site.register(Usuario, UsuarioAdmin)