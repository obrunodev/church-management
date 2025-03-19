from apps.members.models import Member
from django import forms
from shared.forms import BootstrapModelForm


class MemberForm(BootstrapModelForm):

    class Meta:
        model = Member
        fields = [
            'full_name',
            'cpf',
            'gender',
            'civil_status',
            'birth_date',
            'member_since',
            'phone',
            'email',
            'address',
            'category',
            'status',
            'baptism_date',
            'notes',
        ]
        widgets = {
            'birth_date': forms.DateInput(
                attrs={'type': 'date'},
                format='%Y-%m-%d'
            ),
            'member_since': forms.DateInput(
                attrs={'type': 'date'},
                format='%Y-%m-%d'
            ),
            'baptism_date': forms.DateInput(
                attrs={'type': 'date'},
                format='%Y-%m-%d'
            ),
            'notes': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'full_name': 'Nome Completo',
            'cpf': 'CPF',
            'gender': 'Gênero',
            'civil_status': 'Estado Civil',
            'birth_date': 'Data de Nascimento',
            'member_since': 'Membro Desde',
            'phone': 'Telefone',
            'email': 'E-mail',
            'address': 'Endereço',
            'category': 'Categoria',
            'status': 'Status',
            'baptism_date': 'Data de Batismo',
            'notes': 'Observações',
        }
