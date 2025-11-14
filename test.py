import pandas as pd

# import tabulate as tb
from tabulate import tabulate

data_panen = []


def show_data():
    if not data_panen:
        print("tidak ada data panen!")
    else:
        dp = pd.DataFrame(data_panen)
        dp.index = range(1, len(dp) + 1)
        print(tabulate(dp, headers="keys", tablefmt="grid"))


# while True:
print("=" * 40)
print(
    "Selamat Datang di CatatPanen".center(40)
)  # Lebih ringkas daripada menyimpan di variabel
print("=" * 40)

x = 1

while True:
    print(
        """
    silahkan pilih menu berikut:
    1. Tambah data panen
    2. Lihat data panen
    3. Hapus data panen
    4. Rubah data panen
    5. Ekspor data panen (excel)
    6. keluar
    """
    )

    pilih_menu = int(input("pilih menu dari 1-6 : "))

    if pilih_menu == 1:
        data_panen.append(
            {
                "Jenis Panen": input("Jenis Panen : "),
                "Tanggal Panen": input("Tanggal Panen : "),
                "Berat Panen": input("Berat Panen : "),
            }
        )
        show_data()
    elif pilih_menu == 2:
        if data_panen:
            show_data()
        else:
            print("Tidak ada data panen!")
    elif pilih_menu == 3:
        show_data()
        if data_panen:
            try:
                hapus_no = int(input("Inputkan data nomor berapa yang akan dihapus : "))
            except ValueError:
                print("Inputan harus berupa angka !")
            else:
                if 1 <= hapus_no and hapus_no <= len(data_panen):
                    data_panen.pop(hapus_no - 1)
                    print("berhasil hapus data no", hapus_no)
                else:
                    print("nomor yang dipilih tidak ada")
        else:
            print("tidak ada data!")
    elif pilih_menu == 6:
        break
    else:
        print("no tidak sesua")
