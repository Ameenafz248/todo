from django.urls import path
from .views import  TodoListView, TodoCompleteView, TodoDeleteView

urlpatterns = [
   path("", TodoListView.as_view(), name="home"),
   path("<int:pk>/update/", TodoCompleteView.as_view(),name="update"),
   path("<int:pk>/delete/", TodoDeleteView.as_view(), name="delete")
]