from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('tambah-stok/', views.tambah),
    path('delete/<int:id>/', views.delete, name='hapus'),
    path('<int:id>/', views.form, name='ubah'),
]