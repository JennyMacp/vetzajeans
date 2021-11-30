from django.shortcuts import render, redirect
from .forms import FormDataJual
from .models import DataJual
from jeans.models import DataJeans

def index(request):
    datajual = DataJual.objects.all()
    context = {'datajual': datajual}

    return render(request, 'jual/index.html', context)
    
def terjual(request):
    form = FormDataJual()
    if request.method == 'POST':
        form = FormDataJual(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('/jual/')
    return render(request, 'jual/jeans_terjual.html', {'form': form})

def delete(request, id):
    datajual = DataJual.objects.get(pk=id)
    datajual.delete()
    return redirect('/jual/')

def form(request, id=0):
    form = FormDataJual()
    if request.method == 'POST':
        if id == 0:
            form = FormDataJual(request.POST)
        else:
            datajual = DataJual.objects.get(pk=id)
            form = FormDataJual(request.POST, instance = datajual)
        form.save()
        return redirect('/jual/')
    else:
        if id == 0:
            form = FormDataJual()
        else:
            datajual = DataJual.objects.get(pk=id)
            form = FormDataJual(instance = datajual)
        return render(request, 'jual/jeans_terjual.html', {'form':form})

def stok(request):
    datajeans = DataJeans.objects.all()
    context = {'datajeans': datajeans}

    return render(request, 'jual/index.html', context)
