# 项目主 URL 配置（knowledge_tree/urls.py）中引入 tree app 的 URL
# 
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tree.urls', namespace='tree')),
]
