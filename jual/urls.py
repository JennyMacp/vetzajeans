from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('jeans-terjual/', views.terjual),
    path('delete/<int:id>/', views.delete, name='hapus'),
    path('<int:id>/', views.form, name='ubah'),
]