import logging

from django.db.models import Count, Q
from django.http import Http404

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404

from .forms import JournalCreateForm
from .models import Journal, Category, Tag




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








class CategoryListView(generic.ListView):
    queryset = Category.objects.annotate(
        num_journals=Count('journal', filter=Q(journal__is_public=True)))


class TagListView(generic.ListView):
    queryset = Tag.objects.annotate(num_journals=Count(
        'journal', filter=Q(journal__is_public=True)))








class CategoryJournalView(generic.ListView):
    model = Journal
    template_name = 'category_journal.html'

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        self.category = get_object_or_404(Category, slug=category_slug)
        qs = super().get_queryset().filter(category=self.category)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context




class TagJournalView(generic.ListView):
    model = Journal
    template_name = 'tag_journal.html'

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']
        self.tag = get_object_or_404(Tag, slug=tag_slug)
        qs = super().get_queryset().filter(tags=self.tag)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context



class SearchJournalView(generic.ListView):
    model = Journal
    template_name = 'search_journal.html'
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        lookups = (
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(category__name__icontains=query) |
            Q(tags__name__icontains=query)
        )
        if query is not None:
            qs = super().get_queryset().filter(lookups).distinct()
            return qs
        qs = super().get_queryset()
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context

