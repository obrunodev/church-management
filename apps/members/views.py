from apps.members.forms import MemberForm
from apps.members.models import Member
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView


class MemberCreateView(LoginRequiredMixin, CreateView):
    model = Member
    form_class = MemberForm
    success_url = reverse_lazy('members:list')


class MemberListView(LoginRequiredMixin, ListView):
    model = Member
    context_object_name = 'members'


class MemberUpdateView(LoginRequiredMixin, UpdateView):
    model = Member
    form_class = MemberForm
    success_url = reverse_lazy('members:list')


class MemberDeleteView(LoginRequiredMixin, DeleteView):
    model = Member
    success_url = reverse_lazy('members:list')
