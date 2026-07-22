# Dictionary kosong untuk menyimpan bahan baku dan mengelolah resep
bahan_bahan = {}

# Fungsi untuk menambahkan bahan baku 
def tambah_bahan(nama, jumlah):
        """Tambah bahan baru dengan jumlahnya"""
        if nama not in bahan_bahan:
            bahan_bahan[nama] = jumlah
            return f"Berhasil menambahkan {nama} dengan jumlah {jumlah}"
        return f"{nama} sudah ada dalam daftar"

# Fungsi untuk memperbarui jumlah bahan baku   
def perbarui_jumlah(nama, jumlah_baru):
        """Perbarui jumlah bahan yang sudah ada"""
        if nama in bahan_bahan:
            bahan_bahan[nama] = jumlah_baru
            return f"Berhasil memperbarui jumlah {nama} menjadi {jumlah_baru}"
        return f"{nama} tidak ditemukan"

# Fungsi untuk menghapus bahan baku 
def hapus_bahan(nama):
        """Hapus bahan dari resep"""
        if nama in bahan_bahan:
            del bahan_bahan[nama]
            return f"Berhasil menghapus {nama} dari daftar bahan"
        return f"{nama} tidak ditemukan"
    
# Fungsi untuk menampilkan bahan baku
def tampilkan_bahan():
        """Tampilkan semua bahan dan jumlahnya"""
        if bahan_bahan:
            print("\nDaftar Bahan Saat Ini:")
            print("-" * 30)
            for nama, jumlah in bahan_bahan.items():
                print(f"{nama}: {jumlah}")
            print("-" * 30)
        else:
            print("Tidak ada bahan dalam daftar")

# Fungsi utama untuk menjalankan aplikasi Menu Pengelolah Resep
def main():
    
    while True:
        print("\nMenu Pengelola Resep:")
        print("1. Tambah bahan")
        print("2. Perbarui jumlah")
        print("3. Hapus bahan")
        print("4. Tampilkan semua bahan")
        print("5. Keluar")
        
        pilihan = input("Masukkan pilihan Anda (1-5): ")
        
        if pilihan == "1":
            nama = input("Masukkan nama bahan: ")
            jumlah = input("Masukkan jumlah: ")
            print(tambah_bahan(nama, jumlah))
            
        elif pilihan == "2":
            nama = input("Masukkan nama bahan: ")
            jumlah = input("Masukkan jumlah baru: ")
            print(perbarui_jumlah(nama, jumlah))
            
        elif pilihan == "3":
            nama = input("Masukkan nama bahan yang akan dihapus: ")
            print(hapus_bahan(nama))
            
        elif pilihan == "4":
            tampilkan_bahan()
            
        elif pilihan == "5":
            print("Terima kasih telah menggunakan Pengelola Resep!")
            break
            
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()

#Nama       : Amalia Nania Abyanti
#NPM        : 240403010027
#Matkul     : UAS Pemograman Dasar