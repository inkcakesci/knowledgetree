# 项目主 URL 配置（knowledge_tree/urls.py）中引入 tree app 的 URL
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from tree import views as tree_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='tree/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', tree_views.register, name='register'),
    path('', include('tree.urls', namespace='tree')),
]
