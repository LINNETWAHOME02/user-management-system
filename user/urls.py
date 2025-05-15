from django.urls import path
from django.contrib import admin

from user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_user/', views.create_user, name='create_user'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('update_details/<int:id>/', views.update_details, name='update_details'),
    path('delete_user/', views.delete_user, name='delete_user'),
    path('display_users/', views.display_users, name='display_users'),

    path('change_password/', views.change_password, name='change_password')
]