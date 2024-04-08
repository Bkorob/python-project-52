from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.UserLoginFormView.as_view(), name='login'),
    path('logout/', views.UserLogoutFormView.as_view(), name='logout'),
    path('users/', include('task_manager.users.urls')),
#     path('statuses/', include('task_manager.statuses.urls')),
#     path('tasks/', include('task_manager.tasks.urls')),
#     path('labels/', include('task_manager.labels.urls')),
]
