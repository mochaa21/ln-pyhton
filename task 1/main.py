"""
Bisakah lu bikin sebuah fungsi bernama cek_sinyal(market) yang mengekstrak "Harga Saat Ini", "Stop Loss", dan "Take Profit" dari data di atas?
Lalu, buat aturan if/else:

Kalau Harga Saat Ini >= Take Profit, cetak "Take Profit Tersentuh! Jual sekarang."

Kalau Harga Saat Ini <= Stop Loss, cetak "Stop Loss Tersentuh! Cut loss sekarang."

Selain itu, cetak "Harga masih aman, tahan posisi."
"""

market_data = {
    'ticker': 'XAUUSD',
    'prices': [2045.50, 2055.00], # [Harga Buka, Harga Saat Ini]
    'limits': [2040.00, 2060.00]  # [Stop Loss, Take Profit]
}