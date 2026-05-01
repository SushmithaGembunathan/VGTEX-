from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('sarees/', views.sarees, name='sarees'),
    path('dryfruits/', views.dryfruits, name='dryfruits'),
    path('healthmixes/', views.healthmixes, name='healthmixes'),
    path('contact/', views.contact, name='contact'),
    path('reviews/', views.reviews, name='reviews'),
]