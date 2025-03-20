from django.db import models
from django.db.models import Q


class MemberManager(models.Manager):
    
    def get_members(self, request):
        """Retorna membros filtrados"""
        members = self.filter(church=request.user.churches.first())
        if q := request.GET.get('q', ''):
            members = self.filter(full_name__icontains=q)
        return members
    
    def get_members_card_counts(self, request, context):
        """Retorna contagem de membros"""
        members = self.filter(church=request.user.churches.first())
        context['active_members'] = members.filter(status='active').count()
        context['baptized_members'] = members.filter(~Q(category='not_baptized')).count()
        context['not_baptized_members'] = members.filter(category='not_baptized').count()
        return context
