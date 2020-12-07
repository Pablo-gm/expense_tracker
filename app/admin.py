from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models import Account
# Register your models here.

# Custom admin view properties
class AccountAdmin(UserAdmin):
    # display fields
    list_display = ('email','username','date_joined', 'last_login', 'is_admin','is_staff')
    
    # fields on search bar
    search_fields = ('email','username')

    # fields admin won't want to update
    readonly_fields=('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
