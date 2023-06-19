from django.urls import path

from .views import (
    TodoListView,
    TodoDetailView,
    TodoCreateView,
    TodoUpdateView,
    TodoDeleteView,
)

urlpatterns = [
    path("todo/<int:pk>/", TodoDetailView.as_view(), name="todos_detail"),
    path("todo/<int:pk>/delete/", TodoDeleteView.as_view(), name="todos_delete"),
    path("todo/<int:pk>/edit/", TodoUpdateView.as_view(), name="todos_update"),
    path("newpost/new/", TodoCreateView.as_view(), name="todos_new"),
    path("", TodoListView.as_view(), name="home"),
]
