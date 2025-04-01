from django.urls import path
from . import views

app_name = 'item'  # ✅ This registers 'item' as a namespace

urlpatterns = [
  path('', views.items, name='items'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
]# ✅ Correct
  # Example URL pattern

