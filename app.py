import pandas as pd
from tabulate import tabulate

data_panen = []


def show_data():
    print("\n")
    if not data_panen:
        print("Tidak ada data panen!\n")
        print("=" * 40)
    else:
        dp = pd.DataFrame(data_panen)
        dp.index = range(1, len(dp) + 1)
        print(tabulate(dp, headers="keys", tablefmt="grid"))
        print("\n")


print("=" * 40)
print("Selamat Datang di CatatPanen".center(40))
print("=" * 40)

while True:
    print(
        """
Silahkan pilih menu berikut:
1. Tambah data panen
2. Lihat data panen
3. Hapus data panen
4. Ubah data panen
5. Ekspor data panen (excel)
6. Keluar
"""
    )

    try:
        pilih_menu = int(input("Pilih menu dari 1-6 : "))
        print("\n")
    except ValueError:
        print("\nInput harus angka 1-6\n")
        print("=" * 40)
        continue

    # tambah data
    if pilih_menu == 1:
        print("\nMasukkan data panen:\n")
        data_panen.append(
            {
                "Jenis Panen": input("Jenis Panen : "),
                "Tanggal Panen": input("Tanggal Panen : "),
                "Berat Panen": input("Berat Panen (kg) : "),
            }
        )
        print("\nData berhasil ditambahkan.\n")
        show_data()
        print("=" * 40 + "\n")

    # lihat data
    elif pilih_menu == 2:
        show_data()
        print("=" * 40 + "\n")

    # hapus data
    elif pilih_menu == 3:
        show_data()
        if data_panen:
            try:
                hapus_no = int(input("Nomor data yang akan dihapus : "))
                print("\n")
            except ValueError:
                print("Input harus angka!\n")
                continue

            if 1 <= hapus_no <= len(data_panen):
                data_panen.pop(hapus_no - 1)
                print("Berhasil menghapus data nomor", hapus_no, "\n")
            else:
                print("Nomor tidak ditemukan\n")

    # update data
    elif pilih_menu == 4:
        show_data()
        if data_panen:
            try:
                update_no = int(input("Nomor data yang akan diubah : "))
                print("\n")
            except ValueError:
                print("Input harus angka!\n")
                continue

            if 1 <= update_no <= len(data_panen):
                print("Masukkan data baru (enter untuk skip)\n")

                jenis_baru = input("Jenis Panen (baru) : ")
                tanggal_baru = input("Tanggal Panen (baru) : ")
                berat_baru = input("Berat Panen (baru) : ")

                if jenis_baru:
                    data_panen[update_no - 1]["Jenis Panen"] = jenis_baru
                if tanggal_baru:
                    data_panen[update_no - 1]["Tanggal Panen"] = tanggal_baru
                if berat_baru:
                    data_panen[update_no - 1]["Berat Panen"] = berat_baru

                print("\nBerhasil mengubah data nomor", update_no, "\n")
            else:
                print("Nomor tidak ditemukan\n")

    # ekspor excel
    elif pilih_menu == 5:
        if data_panen:
            df = pd.DataFrame(data_panen)
            df.to_excel("data_panen.xlsx", index=False)
            print("Berhasil ekspor data\n")
        else:
            print("Tidak ada data! tidak bisa ekspor!\n")

    # exit
    elif pilih_menu == 6:
        print("Program selesai. Terima kasih telah menggunakan.\n")
        break

    else:
        print("Pilihan menu tidak tersedia\n")
