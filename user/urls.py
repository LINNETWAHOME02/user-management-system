from django.urls import path
from django.contrib import admin

from user import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # ################################ Frontend for now ###################################
    # path('registration_form/', views.registration_form, name='registration_form'),
    # path('user_login/', views.user_login, name='user_login'),

    ############################### Backend for now ###################################
    path('create_user/', views.create_user, name='create_user'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('test_auth/', views.test_auth, name='test_auth'),

    path('update_details/<int:id>/', views.update_details, name='update_details'),
    path('delete_user/', views.delete_user, name='delete_user'),
    path('display_users/', views.display_users, name='display_users'),

    path('change_password/', views.change_password, name='change_password')
]