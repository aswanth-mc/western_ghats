from django.urls import path
from . import views


urlpatterns = [
    # List / Home page of protected areas (with filter options)
    path('', views.protected_area_list, name='protected_area_list'),
    
    # Detail page for a specific protected area by ID
    path('<int:pk>/', views.protected_area_detail, name='protected_area_detail'),
]