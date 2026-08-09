'''
Buatlah sebuah fungsi bernama rekap_harian(riwayat) yang melakukan kalkulasi otomatis dengan alur logika berikut:

Siapkan tiga variabel penampung dengan nilai awal 0: total_profit, jumlah_tp, dan jumlah_sl.

Lakukan looping untuk membaca setiap transaksi di dalam list data tersebut.

Di dalam looping, gunakan logika if/elif untuk mengecek key 'hasil':

Jika hasilnya 'TP', tambahkan angka 1 ke variabel jumlah_tp.

Jika hasilnya 'SL', tambahkan angka 1 ke variabel jumlah_sl.

Di setiap putaran looping, pastikan lu juga menambahkan nilai dari key 'profit' ke dalam variabel total_profit.

Setelah looping selesai, cetak (print) laporan akhirnya agar menampilkan teks seperti ini:

Total TP: 2 kali
Total SL: 2 kali
Total Keuntungan: 22.0 USD
'''

riwayat_trading = [
    {'hasil': 'TP', 'profit': 15.5},
    {'hasil': 'SL', 'profit': -5.0},
    {'hasil': 'TP', 'profit': 20.0},
    {'hasil': 'SL', 'profit': -8.5}
]