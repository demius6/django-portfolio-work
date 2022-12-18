from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create'),
    path('task-page-<int:pk>', views.TaskDetailView.as_view(), name='task_page'),
    path('update-task-<int:pk>', views.UpdateTask.as_view(), name='update_task'),
    path('register', views.register, name='register'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('mail', views.test_mail, name='mail'),
]
