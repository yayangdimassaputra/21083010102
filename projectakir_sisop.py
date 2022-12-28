print('======================================================================================================================')
print('                                                    Assalamualaikum Wr. Wb.')
print('                                                         Halo rekan-rekan')
print('                                 Ini adalah sebuah program yang dapat menghitung hasil dari panen')
print('                                                         Hidup Petani !!!')
print(' ')              
print(' Created by: Yayang Dimas Saputra')
print(' NPM: 21083010102')
print(' ')

def memilih():
    a=input('+++++++++++++++++++++++++++++++++++++++++++++++++\npilih jenis panenan anda'
            '\n+------------------------+'
            '\n|   1.) Buah-buahan      |\n|   2.) Sayur-sayuran    |\n|   3.) Tanaman pangan   |'
            '\n|   4.) Tanaman obat     |\n|   5.) Tanaman hias     |\n|   6.) Keluar Prorgam   |'
            '\n--------------------------\npilih 6 untuk keluar dari program\n+++++++++++++++++++++++++++++++++++++++++++++++++'
            '\n \nPilih nomor berapa jenis panenan anda(1-5): ')
    return a
pilihan = 1
while pilihan <=6:
    pilihan = int(memilih())
    if pilihan == 1:
        print('-Buah-buahan-')
        print ('Buah-buahan adalah bagian dari tanaman yang terdiri dari bagian yang mengandung biji yang dikelilingi oleh bagian yang dapat dimakan, seperti kulit, daging, dan bijinya.\n contohnya apel, anggur, DLL')
        print(' ')
        buah = input('Masukkan nama buah yang akan anda hitung hasil panennya: ')
        berat_panen_buah_per_kg =int(input('Berapa berat total panen buah anda dalam (kg): '))
        harga_buah_per_kg = int(input('Masukkan harga buah panenan anda per (kg) saat ini: '))
        modal_buah = int(input('Masukkan modal pananaman buah anda dalam panen ini: '))
        hasil = berat_panen_buah_per_kg * harga_buah_per_kg
        untung = hasil - modal_buah
        print ('Total penjualan dari panen buah', buah, 'anda adalah : ',(hasil))
        print ('Hasil keutungan dari panen buah', buah, 'anda adalah : ',(untung))
        if hasil > modal_buah:
            print("Panen anda berhasil menguntungkan\n--SELAMAT--")
        elif hasil == modal_buah:
            print("hasil panen anda hanya balik modal\n--AYO LEBIH SEMANGAT LAGI--")
        elif hasil < modal_buah:
            print("Panen anda merugi\n--TETAP SEMANGAT DAN COBA EVALUASI APA PENYEBABNYA--")
        else:
            pass
        print('\n')
        continue
    elif pilihan == 2:
        print('-Sayur-sayuran-')
        print ('Sayuran adalah bagian dari tanaman yang dimakan sebagai makanan, terutama bagian yang tidak berbiji, seperti daun, batang, atau buah.\n contohnya bayam, kubis, DLL')
        print(' ')
        sayur = input('Masukkan nama sayur yang akan anda hitung hasil panennya: ')
        berat_panen_sayur_per_kg =int(input('Berapa berat total panen sayur anda dalam (kg): '))
        harga_sayur_per_kg = int(input('Masukkan harga sayur panenan anda per (kg) saat ini: '))
        modal_sayur = int(input('Masukkan modal pananaman sayur anda dalam panen ini: '))
        hasil = berat_panen_sayur_per_kg * harga_sayur_per_kg
        untung = hasil - modal_sayur
        print ('Total penjualan dari panen sayur', sayur, 'anda adalah : ',(hasil))
        print ('Hasil keutungan dari panen sayur', sayur, 'anda adalah : ',(untung))
        if hasil > modal_sayur:
            print("Panen anda berhasil menguntungkan\n--SELAMAT--")
        elif hasil == modal_sayur:
            print("hasil panen anda hanya balik modal\n--AYO LEBIH SEMANGAT LAGI--")
        elif hasil < modal_sayur:
            print("Panen anda merugi\n--TETAP SEMANGAT DAN COBA EVALUASI APA PENYEBABNYA--")
        else:
            pass
        print('\n')
        continue
    elif pilihan == 3:
        print('-Tanaman pangan-')
        print ('Tanaman pangan adalah tanaman yang menghasilkan produk yang mengandung karbohidrat dan protein utama sebagai sumber makanan pokok dan sumber energi manusia sehari-hari.\n contohnya padi, gandum, kacang tanah, DLL')
        print(' ')
        Tanamanpangan = input('Masukkan nama Tanaman pangan yang akan anda hitung hasil panennya: ')
        berat_panen_Tanamanpangan_per_kg =int(input('Berapa berat total panen Tanaman pangan anda dalam (kg): '))
        harga_Tanamanpangan_per_kg = int(input('Masukkan harga Tanaman pangan panenan anda per (kg) saat ini: '))
        modal_Tanamanpangan = int(input('Masukkan modal pananaman Tanaman pangan anda dalam panen ini: '))
        hasil = berat_panen_Tanamanpangan_per_kg * harga_Tanamanpangan_per_kg
        untung = hasil - modal_Tanamanpangan
        print ('Total penjualan dari panen Tanaman pangan', Tanamanpangan, 'anda adalah : ',(hasil))
        print ('Hasil keutungan dari panen Tanaman pangan', Tanamanpangan, 'anda adalah : ',(untung))
        if hasil > modal_Tanamanpangan:
            print("Panen anda berhasil menguntungkan\n--SELAMAT--")
        elif hasil == modal_Tanamanpangan:
            print("hasil panen anda hanya balik modal\n--AYO LEBIH SEMANGAT LAGI--")
        elif hasil < modal_Tanamanpangan:
            print("Panen anda merugi\n--TETAP SEMANGAT DAN COBA EVALUASI APA PENYEBABNYA--")
        else:
            pass
        print('\n')
        continue
    elif pilihan == 4:
        print('-Tanaman obat-')
        print ('Tanaman obat adalah Jenis-jenis tanaman yang memiliki fungsi dan berkhasiat sebagai obat dan dipergunakan untuk penyembuhan maupun mencegah suatu penyakit.\n Contohnya: temulawak, kumis kucing, DLL')
        print(' ')
        Tanamanobat = input('Masukkan nama Tanaman obat yang akan anda hitung hasil panennya: ')
        berat_panen_Tanamanobat_per_kg =int(input('Berapa berat total panen Tanaman obat anda dalam (kg): '))
        harga_Tanamanobat_per_kg = int(input('Masukkan harga Tanaman obat panenan anda per (kg) saat ini: '))
        modal_Tanamanobat = int(input('Masukkan modal pananaman Tanaman obat anda dalam panen ini: '))
        hasil = berat_panen_Tanamanobat_per_kg * harga_Tanamanobat_per_kg
        untung = hasil - modal_Tanamanobat
        print ('Total penjualan dari panen Tanaman obat', Tanamanobat, 'anda adalah : ',(hasil))
        print ('Hasil keutungan dari panen Tanaman obat', Tanamanobat, 'anda adalah : ',(untung))
        if hasil > modal_Tanamanobat:
            print("Panen anda berhasil menguntungkan\n--SELAMAT--")
        elif hasil == modal_Tanamanobat:
            print("hasil panen anda hanya balik modal\n--AYO LEBIH SEMANGAT LAGI--")
        elif hasil < modal_Tanamanobat:
            print("Panen anda merugi\n--TETAP SEMANGAT DAN COBA EVALUASI APA PENYEBABNYA--")
        else:
            pass
        print('\n')
        continue
    elif pilihan == 5:
        print('-Tanaman hias-')
        print ('Tanaman hias adalah semua jenis tanaman yang sengaja ditanam untuk tujuan dekoratif atau sebagai hiasan.\n Contohnya: Pohon bonsai, Bunga mawar, DLL')
        print(' ')
        Tanamanhias = input('Masukkan nama Tanaman hias yang akan anda hitung hasil panennya: ')
        berat_panen_Tanamanhias_per_kg =int(input('Berapa total panen Tanaman hias anda per satuan tanaman: '))
        harga_Tanamanhias_per_kg = int(input('Masukkan harga Tanaman obat panenan anda per 1 tanaman saat ini: '))
        modal_Tanamanhias = int(input('Masukkan modal pananaman Tanaman hias anda dalam panen ini: '))
        hasil = berat_panen_Tanamanhias_per_kg * harga_Tanamanhias_per_kg
        untung = hasil - modal_Tanamanhias
        print ('Total penjualan dari panen Tanaman hias', Tanamanhias, 'anda adalah : ',(hasil))
        print ('Hasil keutungan dari panen Tanaman hias', Tanamanhias, 'anda adalah : ',(untung))
        if hasil > modal_Tanamanhias:
            print("Panen anda berhasil menguntungkan\n--SELAMAT--")
        elif hasil == modal_Tanamanhias:
            print("hasil panen anda hanya balik modal\n--AYO LEBIH SEMANGAT LAGI--")
        elif hasil < modal_Tanamanhias:
            print("Panen anda merugi\n--TETAP SEMANGAT DAN COBA EVALUASI APA PENYEBABNYA--")
        else:
            pass
        print('\n')
        continue
    elif pilihan == 6:
        print (' ================================TERIMAKASIH============================== ')
        print (' ======================telah menggunakan program kami===================== ')
        break
    else:
        print('angka yang anda masukkan tidak terdefinisi')
