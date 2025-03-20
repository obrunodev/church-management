from apps.members.models import Member
from django.shortcuts import render
from django.views import View


class DashboardView(View):
    def get(self, request):
        context = {
            'members_count': Member.objects.get_members(request).count(),
        }
        return render(request, 'dashboard/index.html', context)
