from django.urls import path
from gastoscomunes import views

urlpatterns = [
    # ... Otras URL ...
    path('inicio/', views.inicio, name='inicio'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('gastoscomunes/', views.gastoscomunes, name='gastoscomunes'),
    path('contacto/', views.contacto, name='contacto'),
    # ... Otras URL ...
]
