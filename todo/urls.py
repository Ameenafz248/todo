from django.urls import path
from .views import  TodoListView, TodoCompleteView, TodoDeleteView, TodoCreateView, TodoListPostView

urlpatterns = [
   path("", TodoListView.as_view(), name="home"),
   path("create/", TodoListView.as_view(),name="create"),
   path("<int:pk>/update/", TodoCompleteView.as_view(),name="update"),
   path("<int:pk>/delete/", TodoDeleteView.as_view(), name="delete")
]