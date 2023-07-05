from django.urls import path
from . import views

urlpatterns = [
    path('', views.getContacts, name='contacts'),
    path('contact/<str:pk>/', views.getContact, name='contact'),
    path('contacts/<str:pk>/update', views.updateContact, name='update-contact'),
    path('contacts/<str:pk>/delete/', views.deleteContact, name='delete-contact'),
    path('contacts/add/', views.createContact, name='add')
]
