from django.urls import path
from . import views




urlpatterns = [
    path('', views.index, name='home'),
    path('<slug:link_slug>/', views.root_link, name='root_link'),
    path('link/create/', views.add_link, name='add_link'),
    
    
    
]