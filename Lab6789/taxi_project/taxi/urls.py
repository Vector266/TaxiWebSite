from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('', views.trip_list, name='trip_list'),
    path('trips/add/', views.trip_create, name='trip_add'),
    path('trips/<int:pk>/edit/', views.trip_update, name='trip_edit'),
    path('trips/<int:pk>/delete/', views.trip_delete, name='trip_delete'),
]
