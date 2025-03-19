from apps.members.models import Member
from django import forms


class MemberForm(forms.ModelForm):

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
