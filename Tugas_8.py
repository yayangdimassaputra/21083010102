from os import getpid
from time import time, sleep
from multiprocessing import Pool, Process

def cetak(i):
    bil = i % 2
    if bil == 0:
        print(i, "Genap - ID proses", getpid())
    else:
        print(i, "Ganjil - ID proses", getpid())
    sleep(1)

n = int(input("Angka batasan: "))

# Sekuensial
print("\nSekuensial")
sekuensial_awal = time()
for i in range(1, n + 1):
    cetak(i)
sekuensial_akhir = time()

# Kelas Process
print("\nmultiprocessing.Process")
kumpulan_proses = []
process_awal = time()
for i in range(1, n + 1):
    p = Process(target=cetak, args=(i,))
    kumpulan_proses.append(p)
    p.start()

for i in kumpulan_proses:
    p.join()
process_akhir = time()

# Kelas Pool
print("\nmultiprocessing.Pool")
pool_awal = time()
pool = Pool()
pool.map(cetak, range(1, n + 1))
pool.close()
pool_akhir = time()

# Perbandingan waktu eksekusi
print("\nwaktu eksekusi sekuensial              :", sekuensial_akhir - sekuensial_awal, "detik")
print("waktu eksekusi multiprocessing.Process :", process_akhir - process_awal, "detik")
print("waktu eksekusi multiprocessing.Pool    :", pool_akhir - pool_awal, "detik")
