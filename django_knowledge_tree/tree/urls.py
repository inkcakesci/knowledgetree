from django.urls import path
from . import views

app_name = 'tree'

urlpatterns = [
    path('', views.index, name='index'),
    path('tree/<int:tree_id>/', views.view_tree, name='view_tree'),
    path('edit/', views.edit_tree, name='create_tree'),
    path('edit/<int:tree_id>/', views.edit_tree, name='edit_tree'),
    path('delete/<int:tree_id>/', views.delete_tree, name='delete_tree'),
    path('api/update/', views.update_tree_api, name='update_api'),
]