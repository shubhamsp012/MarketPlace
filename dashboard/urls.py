from django.urls import path
from . import views

app_name = 'dashboard'  # ✅ Ensure this is present

urlpatterns = [
    path('', views.index, name='index'),  # ✅ This should match 'dashboard:index'
]
