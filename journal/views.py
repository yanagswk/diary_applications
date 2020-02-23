import logging

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from .forms import JournalCreateForm
from .models import Journal



logger = logging.getLogger(__name__)



class JournalListView(generic.ListView):
    model = Journal
    template_name = 'diary_list.html'
    paginate_by = 6

    def get_queryset(self):
        diaries = Journal.objects.order_by('-created_at')
        return diaries


class JournalDetailView(generic.DetailView):
    model = Journal
    template_name = 'diary_detail.html'
        


class JournalCreateView(LoginRequiredMixin, generic.CreateView):
    model = Journal
    template_name = 'diary_create.html'
    form_class = JournalCreateForm
    success_url = reverse_lazy('journal:diary_list')

    def form_valid(self, form):
        journal = form.save(commit=False)
        journal.user = self.request.user
        journal.save()
        messages.success(self.request, '日記を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "日記の作成に失敗しました。")
        return super().form_invalid(form)


class JournalUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Journal
    template_name = 'diary_update.html'
    form_class = JournalCreateForm

    def get_success_url(self):
        return reverse_lazy('journal:diary_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '日記を更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "日記の更新に失敗しました。")
        return super().form_invalid(form)


class JournalDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Journal
    template_name = 'diary_delete.html'
    success_url = reverse_lazy('journal:diary_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "日記を削除しました。")
        return super().delete(request, *args, **kwargs)
