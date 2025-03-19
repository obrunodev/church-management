from django.db import models


class MemberManager(models.Manager):
    
    def get_members(self, request):
        """Retorna membros filtrados"""
        members = self.all()
        if q := request.GET.get('q', ''):
            members = self.filter(full_name__icontains=q)
        return members
