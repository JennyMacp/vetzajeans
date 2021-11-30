from django import forms
from django.forms import widgets
from .models import DataJual
from jeans.models import DataJeans

class FormDataJual(forms.ModelForm):
    # jeans = DataJeans.objects.all()
    idjeans = forms.ModelChoiceField(queryset=DataJeans.objects.all())

    class Meta:
        model = DataJual
        fields = ('idjeans', 'merk', 'ukuran', 'jumlah', 'harga', 'keterangan', 'tanggal')

        widgets = {
            # 'idjeans': forms.ChoiceField(**option={'class': 'form-control'}),
            'merk': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'ukuran': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'jumlah': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'harga': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'keterangan': forms.TextInput(attrs={'class': 'form-control', 'type': 'textarea'}),
            'tanggal': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            }