from django.contrib import admin
from .models import Profile, Contact, ContactForm


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','status', 'create_at')
    list_filter = ('status', 'create_at')

admin.site.site_title = "Summer Project Admin Panel"
admin.site.site_header = "Summer Project Admin Panel"
admin.site.index_title = "Summer Project Admin Panel Home"

admin.site.register(Contact, ContactAdmin)