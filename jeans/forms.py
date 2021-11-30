from django import forms
from django.forms import widgets
from .models import DataJeans

class FormDataJeans(forms.ModelForm):
    class Meta:
        model = DataJeans
        fields = ('idjeans', 'merk', 'ukuran', 'stok', 'harga', 'keterangan', 'tanggal')
        
        widgets = {
            'idjeans': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'merk': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'ukuran': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'stok': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'harga': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'keterangan': forms.TextInput(attrs={'class': 'form-control', 'type': 'textarea'}),
            'tanggal': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            }