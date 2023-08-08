from django.urls import path
from django.urls import path
from .views import (
    TaskList, 
    TaskCreate, 
    TaskUpdate, 
    TaskDelete, 
    TaskDetailView, 
    CustomLoginView, 
    RegisterView, 
    LogoutView
    )

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('list/', TaskList.as_view(), name='task-list'),
    path('create/', TaskCreate.as_view(), name='task-create'),
    path('update/<int:pk>', TaskUpdate.as_view(), name='task-update'),
    path('delete/<int:pk>', TaskDelete.as_view(), name='task-delete'),
    path('details/<int:pk>', TaskDetailView.as_view(), name='task-detail'),
]
