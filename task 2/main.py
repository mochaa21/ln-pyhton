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

# your code

def rekap_harian(riwayat):
    # tampung
    total_profit = 0

    for trade in riwayat:
        total_profit += trade['profit']

    jumlah_tp = 0
    jumlah_sl = 0

    # looping
    for hasil in riwayat:
        if hasil['hasil'] == 'TP':
            jumlah_tp += 1
        elif hasil['hasil'] == 'SL':
            jumlah_sl += 1
        else:
            print('Error..')

    print(f"Total TP: {jumlah_tp}")
    print(f"Total SL: {jumlah_sl}")
    print(f"Total profit: {total_profit}")

rekap_harian(riwayat_trading)