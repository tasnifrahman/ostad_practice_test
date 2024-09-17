from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_contact, name='add_contact'),
    path('<int:contact_id>/', views.contact_detail, name='contact_detail'),
    path('<int:contact_id>/edit/', views.edit_contact, name='edit_contact'),
    path('<int:contact_id>/delete/', views.delete_contact, name='delete_contact'),
]
