import pandas as pd

data_panen = []


def tampilkan_data():
    if not data_panen:
        print("Belum ada data panen.")
    else:
        df = pd.DataFrame(data_panen)
        df.index = range(1, len(df) + 1)  # tambahkan nomor urut otomatis
        print("\n=== DAFTAR HASIL PANEN ===")
        print(
            df.to_markdown(tablefmt="grid", index=True)
        )  # tampilkan tabel dengan garis


while True:
    print("\n=== PROGRAM CATATAN HASIL PANEN ===")
    print("1. Tambah Data Panen")
    print("2. Lihat Semua Data")
    print("3. Hapus Data")
    print("4. Update Data")
    print("5. Ekspor ke Excel (pandas)")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ").strip()

    if pilihan == "1":
        tanaman = input("Nama tanaman: ").strip()
        tanggal = input("Tanggal panen (dd/mm/yyyy): ").strip()
        hasil = input("Jumlah hasil panen (kg): ").strip()
        data_panen.append({"Tanaman": tanaman, "Tanggal": tanggal, "Hasil (kg)": hasil})
        print("Data berhasil ditambahkan!")

    elif pilihan == "2":
        tampilkan_data()

    elif pilihan == "3":
        tampilkan_data()
        if data_panen:
            try:
                hapus = int(input("Masukkan nomor data yang ingin dihapus: "))
                if 1 <= hapus <= len(data_panen):
                    data_panen.pop(hapus - 1)
                    print("Data berhasil dihapus.")
                else:
                    print("Nomor tidak valid.")
            except ValueError:
                print("Input harus berupa angka.")

    elif pilihan == "4":
        tampilkan_data()
        if data_panen:
            try:
                ubah = int(input("Masukkan nomor data yang ingin diupdate: "))
                if 1 <= ubah <= len(data_panen):
                    print("Masukkan data baru (kosongkan jika tidak ingin diubah):")
                    tanaman_baru = input("Nama tanaman baru: ").strip()
                    tanggal_baru = input("Tanggal panen baru: ").strip()
                    hasil_baru = input("Hasil panen baru (kg): ").strip()

                    if tanaman_baru:
                        data_panen[ubah - 1]["Tanaman"] = tanaman_baru
                    if tanggal_baru:
                        data_panen[ubah - 1]["Tanggal"] = tanggal_baru
                    if hasil_baru:
                        data_panen[ubah - 1]["Hasil (kg)"] = hasil_baru

                    print("Data berhasil diupdate.")
                else:
                    print("Nomor tidak valid.")
            except ValueError:
                print("Input harus berupa angka.")

    elif pilihan == "5":
        if not data_panen:
            print("Tidak ada data untuk diekspor.")
        else:
            df = pd.DataFrame(data_panen)
            df.to_excel("data_panen.xlsx", index=False)
            print("Data berhasil diekspor ke file data_panen.xlsx")

    elif pilihan == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Coba lagi.")
