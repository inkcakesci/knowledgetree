from django.urls import path
from . import views

app_name = 'tree'

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/', views.edit_tree, name='edit'),
    path('api/update/', views.update_tree_api, name='update_api'),
]
