from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Todo
from .forms import TodoForm
from django.urls import reverse_lazy


class TodoListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = TodoListGetView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = TodoListPostView.as_view()
        return view(request, *args, **kwargs)
    

class TodoListGetView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = "home.html"
    
    def get_queryset(self):
        return Todo.objects.filter(author=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TodoForm()
        return context

class TodoListPostView(LoginRequiredMixin, FormView):
    model  = Todo
    form_class = TodoForm
    template_name = "home.html"

    def get_success_url(self) -> str:
        return reverse_lazy("home")

    def post(self, request, *args, **kwargs):
        self.user = request.user
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        todo = form.save(commit=False)
        todo.author = self.user
        todo.save()
        return super().form_valid(form) 

