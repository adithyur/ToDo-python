from django.urls import path,include
from . import views

app_name='ToDoapp'
urlpatterns = [
    # path('',views.index,name='index'),
    #path('delete/<int:task_id>/', views.delete, name='delete'),
    #path('update/<int:task_id>/', views.update, name='update'),
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>/', views.DetailTaskView.as_view(), name='detail'),
    path('update/<int:pk>/', views.UpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete'),

]