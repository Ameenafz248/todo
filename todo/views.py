from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, CreateView, FormView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Todo
from .forms import TodoForm, CompleteForm
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
        queryset =  Todo.objects.filter(author=self.request.user)
        q = self.request.GET.get("q")
        if q is None:
            return queryset
        return queryset.filter(title__icontains=q)
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TodoForm()
        context['complete'] = CompleteForm()
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
        return JsonResponse({'id' : todo.id, 'title' : todo.title, 'duedate' : todo.formatted_date(), 'is_past' : todo.is_past }, status=200) 

class TodoCreateView(LoginRequiredMixin, CreateView):
   model = Todo 
   fields = ['title', 'author']
   def post(self, request, *args, **kwargs):
      self.user = request.user
      return super().post(request, *args, **kwargs)

   def form_valid(self, form):
       todo = form.save(commit=False)
       todo.author = self.user
       todo.save()
       return JsonResponse({'id' : todo.id, 'title' : todo.title, 'duedate' : todo.formatted_date()}, status=200) 

class TodoCompleteView(LoginRequiredMixin,UpdateView):
    model = Todo
    template_name = "update_completed.html"
    fields = ['completed']
    success_url = reverse_lazy("home")


    def form_valid(self, form) :
        self.object = form.save()
        return JsonResponse({'hi' : self.object.id}, status=201)


    def form_invalid(self, form) :
        return JsonResponse(form.errors.as_json(), status=400)
   

    def get_queryset(self):
        queryset = super(TodoCompleteView, self).get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset

class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    template_name = "todo_delete.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        self.get_object().delete()
        return JsonResponse({}, status=200)
    
    def get_queryset(self):
        queryset = super(TodoDeleteView, self).get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset
    