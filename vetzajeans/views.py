from django.shortcuts import render
from jeans.models import DataJeans
from jual.models import DataJual

def index(request):
	penjualan = DataJual.objects.all()
	pembelian = DataJeans.objects.all()

	list_total_penjualan = []
	for i in penjualan:
		list_total_penjualan.append(i.jumlah)

	list_total_pembelian = []
	for i in pembelian:
		list_total_pembelian.append(i.stok)

	total_penjualan = sum(list_total_penjualan)
	total_pembelian = sum(list_total_pembelian)

	context = {
	"total_penjualan": total_penjualan,
	"total_pembelian": total_pembelian,
	}

	return render(request, 'index.html', context)