from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from .models import Todos
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class TodoListView(LoginRequiredMixin, ListView):
    model = Todos
    template_name = "home.html"
    context_object_name = "Todos"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Todos"] = context["Todos"].filter(user=self.request.user)
        context["count"] = context["Todos"].filter(completed=False).count()
        search_input = self.request.GET.get("search-area") or ""
        if search_input:
            context["Todos"] = context["Todos"].filter(title__icontains=search_input)
            context["search_input"] = search_input
        return context


class TodoDetailView(DetailView):
    model = Todos
    template_name = "todos_detail.html"
    context_object_name = "Todos"


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todos
    template_name = "create.html"
    fields = ["title", "description", "completed"]
    success_url = reverse_lazy("home")

    def form_valid(self, form: BaseModelForm):
        form.instance.user = self.request.user
        return super(TodoCreateView, self).form_valid(form)


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todos
    template_name = "todos_update.html"
    fields = ["title", "description", "completed"]
    context_object_name = "Todos"
    success_url = reverse_lazy("home")


class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todos
    template_name = "todos_delete.html"
    ontext_object_name = "Todos"
    success_url = reverse_lazy("home")
