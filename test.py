import pandas as pd

data_panen = []

# while True:
print('=' * 40)
print("Selamat Datang di CatatPanen".center(40)) # Lebih ringkas daripada menyimpan di variabel
print('=' * 40)

x = 1

while True:
    print("""
    silahkan pilih menu berikut:
    1. Tambah data panen
    2. Lihat data panen
    3. Hapus data panen
    4. Rubah data panen
    5. Ekspor data panen (excel)
    6. keluar
    """)

    pilih_menu = int(input('pilih menu dari 1-6 : '))
    
    if pilih_menu == 6:
        break
    else:
        print('no tidak sesua')