from .models import Link
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render


def home(request):
    return render(request, 'link/index.html')

def uslugi(request):
    return render(request, 'link/uslugi.html')

def about(request):
    return render(request, 'link/about.html')




class ShowLinkView(ListView):
    model = Link
    template_name = 'link/link.html'
    context_object_name = 'link'
    ordering = ['-date']


    def get_context_data(self, **kwards):
        ctx = super(ShowLinkView, self).get_context_data(**kwards)

        ctx['title'] = 'Новости'
        return ctx

class LinkDetailView(DetailView):
    model = Link
    template_name = 'link/link_detail.html'

    def get_context_data(self, **kwards):
        ctx = super(LinkDetailView, self).get_context_data(**kwards)

        ctx['title'] = Link.objects.get(slug=self.kwargs['slug'])
        return ctx

class CreateLinkView(LoginRequiredMixin, CreateView):
    model = Link
    template_name='link/link_form.html'
    fields = ['title', 'long_link', 'slug']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwards):
        ctx = super(CreateLinkView, self).get_context_data(**kwards)

        ctx['title'] = 'Добавление статьи'
        ctx['btn_text'] = 'Добавить статью'
        return ctx

class UpdateLinkView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Link
    template_name = 'link/link_form.html'

    fields = ['title', 'long_link', 'slug']


    def get_context_data(self, **kwards):
        ctx = super(UpdateLinkView, self).get_context_data(**kwards)

        ctx['title'] = 'Обновление ссылки'
        ctx['btn_text'] = 'Обновить ссылку'
        return ctx


    def test_func(self):
        news = self.get_object()
        if self.request.user == news.autor:
            return True

        return False


    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class DeleteLinkView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Link
    success_url = '/'
    template_name = 'link/link_delete.html'

    def test_func(self):
        link = self.get_object()
        if self.request.user == link.autor:
            return True
        return False
