from django.shortcuts import render
from jual.forms import FormDataJual
from jeans.models import DataJeans
from jual.models import DataJual
import statistics

def index(request):
	# penjualan
	penjualan = DataJual.objects.all()
	
	list_total_penjualan = []
	for i in penjualan:
		list_total_penjualan.append(i.jumlah)
	total_penjualan = sum(list_total_penjualan)

	total_harga = []
	for y in penjualan:
		total_harga.append(y.harga)
	harga_penjualan = sum(total_harga)
	
	# pembelian
	pembelian = DataJeans.objects.all()
	
	list_total_pembelian = []
	for i in pembelian:
		list_total_pembelian.append(i.stok)
	total_pembelian = sum(list_total_pembelian)

	total_harga1 = []
	for y in pembelian:
		total_harga1.append(y.harga)
	harga_pembelian = sum(total_harga1)

	# max dan min penjualan
	max_penjualan = []
	for m in penjualan:
		max_penjualan.append(m.harga)
	penjualan_termahal = max(max_penjualan)
	perjualan_terendah = min(max_penjualan)

	# max min pembelian
	max_pembelian = []
	for m in pembelian:
		max_pembelian.append(m.harga)
	pembelian_tertinggi = max(max_pembelian)
	pembelian_terendah = min(max_pembelian)

	# paling banyak
	# modus = []
	# for x in pembelian:
	# 	modus.append(x.merk)
	# modus_pembelian = statistics.mode(modus)

	modus1 = []
	for x in penjualan:
		modus1.append(x.merk)
	modus_penjualan = statistics.mode(modus1)

	context = {
	"total_penjualan": total_penjualan,
	"total_pembelian": total_pembelian,
	"penjualan_termahal": penjualan_termahal,
	"perjualan_terendah": perjualan_terendah,
	"pembelian_tertinggi": pembelian_tertinggi,
	"pembelian_terendah": pembelian_terendah,
	# "modus_pembelian": modus_pembelian,
	"modus_penjualan": modus_penjualan,
	"harga_penjualan": harga_penjualan,
	"harga_pembelian": harga_pembelian,
	}

	return render(request, 'laporan/index.html', context)