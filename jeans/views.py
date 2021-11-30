from django.shortcuts import render, redirect
from .forms import FormDataJeans
from .models import DataJeans

def index(request):
    datajeans = DataJeans.objects.all()
    context = {'datajeans': datajeans}

    return render(request, 'jeans/index.html', context)
    
def tambah(request):
    form = FormDataJeans()
    if request.method == 'POST':
        form = FormDataJeans(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('/jeans/')
    
    return render(request, 'jeans/tambah_stok.html', {'form': form})

def delete(request, id):
    datajeans = DataJeans.objects.get(pk=id)
    datajeans.delete()
    return redirect('/jeans/')

def form(request, id=0):
    form = FormDataJeans()
    if request.method == 'POST':
        if id == 0:
            form = FormDataJeans(request.POST)
        else:
            datajeans = DataJeans.objects.get(pk=id)
            form = FormDataJeans(request.POST, instance = datajeans)
        form.save()
        return redirect('/jeans/')
    else:
        if id == 0:
            form = FormDataJeans()
        else:
            datajeans = DataJeans.objects.get(pk=id)
            form = FormDataJeans(instance = datajeans)
        return render(request, "jeans/tambah_stok.html", {'form':form})

