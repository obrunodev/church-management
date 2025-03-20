from apps.members.forms import MemberForm
from apps.members.models import Member
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView


class MemberCreateView(LoginRequiredMixin, CreateView):
    model = Member
    form_class = MemberForm
    success_url = reverse_lazy('members:list')

    def form_valid(self, form):
        church = self.request.user.churches.first()
        if not church:
            form.add_error(None, "Nenhuma igreja vinculada ao usuário.")
            return self.form_invalid(form)
        form.instance.church = church
        return super().form_valid(form)


class MemberListView(LoginRequiredMixin, ListView):
    model = Member
    context_object_name = 'members'

    def get_queryset(self):
        return Member.objects.get_members(self.request)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = Member.objects.get_members_card_counts(self.request, context)
        return context


class MemberUpdateView(LoginRequiredMixin, UpdateView):
    model = Member
    form_class = MemberForm
    success_url = reverse_lazy('members:list')


class MemberDeleteView(LoginRequiredMixin, DeleteView):
    model = Member
    success_url = reverse_lazy('members:list')
