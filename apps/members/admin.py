from apps.members.models import Member
from django.contrib import admin


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'gender', 'member_since', 'category']
    search_fields = ['full_name']
    list_filter = ['gender', 'category']
