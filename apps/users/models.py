from django.db import models
from django.contrib.auth.models import User
from shared.models import BaseModel


class Church(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Nome')
    address = models.CharField(max_length=255, verbose_name='Endereço', blank=True, null=True)
    city = models.CharField(max_length=255, verbose_name='Cidade', blank=True, null=True)
    state = models.CharField(max_length=2, verbose_name='Estado', blank=True, null=True)
    zip_code = models.CharField(max_length=10, verbose_name='CEP', blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name='Telefone', blank=True, null=True)
    email = models.EmailField(verbose_name='Email', blank=True, null=True)
    website = models.URLField(verbose_name='Website', blank=True, null=True)
    founded = models.DateField(verbose_name='Fundação', blank=True, null=True)
    active = models.BooleanField(default=True, verbose_name='Ativo')
    users = models.ManyToManyField(User, verbose_name='Usuários', blank=True, related_name='churches')

    class Meta:
        ordering = ['name']
        verbose_name = 'Igreja'
        verbose_name_plural = 'Igrejas'

    def __str__(self):
        return self.name
