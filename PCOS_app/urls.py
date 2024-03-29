from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login_view, name="login_view"),
    path('register/', views.register, name="registration"),
    path('Polycyctic-ovary-Syndrome/', views.pcos, name="pcos"),
    path('output/<str:rs>/', views.output, name="output"),
    path('logout/',views.logout_form, name = 'logout'),
]
