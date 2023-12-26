from django.urls import path
from .views import index, update, delete

urlpatterns = [
    path('', index , name='index'),
    path('update/<int:pk>/', update , name='update'),
    path('delete/<int:pk>/', delete , name='delete'),
    
]
