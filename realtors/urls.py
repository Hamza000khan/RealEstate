from django.urls import path
from . import views

urlpatterns = [
    # path('', views.create, name='create'),
    path('<int:realtor_id>', views.detail, name='detail'),
    ]