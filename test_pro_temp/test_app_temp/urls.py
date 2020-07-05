from django.urls import path
from test_app_temp import views

app_name = 'tapp'

urlpatterns = [
    path('Login/',views.user_login, name='user_login'),
    path('Register/', views.reg_forms, name='reg'),
    path('users/', views.index_users, name='users'),
    path('formpage/', views.index_forms, name='formpage'),

]
