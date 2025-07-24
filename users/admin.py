from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
from .models import ContactMessage

# Custom User Admin to show role in admin
class UserProfileAdmin(UserAdmin):
    list_display = ('user')

    fieldsets = UserAdmin.fieldsets + (
        ('Role & Permissions', {'fields': ('role',)}),
    )

admin.site.register(UserProfile)

class ContactMessageAdmin(ContactMessage):
    list_display = ('name', 'email', 'message', 'sent_at')
admin.site.register(ContactMessage)



