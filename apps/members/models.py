from apps.members.managers import MemberManager
from apps.users.models import Church
from django.db import models
from shared.models import BaseModel


class Member(BaseModel):
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]

    CIVIL_STATUS_CHOICES = [
        ('single', 'Solteiro(a)'),
        ('married', 'Casado(a)'),
        ('divorced', 'Divorciado(a)'),
        ('widowed', 'Viúvo(a)'),
    ]

    CATEGORY_CHOICES = [
        ('active_member', 'Membro Ativo'),
        ('visitor', 'Visitante'),
        ('transferred', 'Transferido'),
        ('inactive_member', 'Inativo'),
        ('not_baptized', 'Não Batizado'),
        ('other', 'Outro'),
    ]

    STATUS_CHOICES = [
        ('active', 'Ativo'),
        ('inactive', 'Inativo'),
        ('suspended', 'Suspenso'),
    ]

    church = models.ForeignKey(Church, on_delete=models.CASCADE, related_name='members', blank=True, null=True)
    full_name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    civil_status = models.CharField(max_length=10, choices=CIVIL_STATUS_CHOICES)
    birth_date = models.DateField(null=True, blank=True)
    member_since = models.DateField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    baptism_date = models.DateField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    objects = MemberManager()

    class Meta:
        ordering = ['full_name']
        verbose_name = 'Membro'
        verbose_name_plural = 'Membros'

    def __str__(self):
        return self.full_name
