from django.urls import path
from . import views


urlpatterns = [
    path('<int:product_id>/', views.rating, name='rating'),
    
]
