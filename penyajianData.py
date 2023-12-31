import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate

#Pemrosesan Data
interval = ['20-22','23-25', '26-28', '29-31', '32-34', '35-37', '38-40', '41-43', '44-46', '47-49', '50-52', '53-55']
frekuensi = ['91', '673', '689', '493', '130', '40', '9', '2', '0', '1', '0', '0']
frek_kumulatif_lebih_kecil = ['91', '764', '1453', '1946', '2076', '2116', '2125', '2127', '2127', '2128','2128', '2128' ]
frek_kumulatif_lebih_besar = ['2128','2128','2128', '2127', '2127','2125','2116','2076', '1946','1453', '764', '91' ]
frekuensi_relatif = ['4.276315789', '31.62593985','32.37781955','23.16729323', '6.109022556', '1.879699248', '0.422932331', '0.093984962', '0', '0.046992481', '0', '0'        ]
frekuensi_relatif_kurang_dari = ['4.276315789','35.90225564','68.28007519', '91.44736842', '97.55639098', '99.43609023', '99.85902256', '99.95300752','99.95300752', '100', '100', '100'  ]
frekuensi_relatif_lebih_dari = ['100', '100', '100','99.95300752','99.95300752','99.85902256','99.43609023','97.55639098','91.44736842','68.28007519','35.90225564','4.276315789']


data = {
    'Interval': interval,
    'Frekuensi': frekuensi,
    'Frek. Kumulatif Lebih Kecil (<)': frek_kumulatif_lebih_kecil,
    'Frek. Kumulatif Lebih Besar (>)': frek_kumulatif_lebih_besar,
    'Frek. Relatif': frekuensi_relatif,
    'Frek. Relatif Kurang dari (<)': frekuensi_relatif_kurang_dari,
    'Frek. Relatif Lebih dari (>)': frekuensi_relatif_lebih_dari,
}

#Membentuk DataFrame dari data yang telah disediakan
df = pd.DataFrame(data)

# Mencetak DataFrame dengan tata letak tabel yang diformat dengan judul kolom dan grid
table = tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False)

# Membuat sebuah objek gambar dengan ukuran 13x5.
plt.figure(figsize=(13, 5))

#Membuat dua subplot di dalam gambar.
plt.subplot(121)

# Menggambar plot garis berdasarkan interval dan data yang diberikan.
plt.plot(interval, frekuensi, marker='o', color='b', label="Frekuensi")
plt.plot(interval, frek_kumulatif_lebih_kecil, marker='o', color='g', label='Frek. Kumulatif Lebih Kecil (<)')
plt.plot(interval, frek_kumulatif_lebih_besar, marker='o', color='r', label='Frek Kumulatif Lebih Besar (>)')
#Mengatur label sumbu x, sumbu y, dan judul pada plot.
plt.xlabel('Interval')
plt.ylabel('Frekuensi')
plt.title('Kelompok Frekuensi Kumulatif')

#Menambahkan legenda ke dalam plot
plt.legend()

plt.subplot(122)
plt.plot(interval, frekuensi_relatif, marker='o', linestyle='dashed', color='c', label='Frek. relatif')
plt.plot(interval, frekuensi_relatif_kurang_dari, marker='o', linestyle='dashed', color='m', label='Frek. relatif kurang dari (<)')
plt.plot(interval, frekuensi_relatif_lebih_dari, marker='o', linestyle='dashed', color='y', label='Frek. relatif lebih dari (>)')
plt.xlabel('Interval')
plt.ylabel('Frek. relatif')
plt.title('Kelompok Frekuensi Kumulatif Relatif')

plt.legend()

#Menambahkan grid ke dalam plot
plt.grid(True, linestyle='--')

#Menampilkan tabel
print(table)

# Menyesuaikan tata letak plot agar sesuai dan rapi
plt.tight_layout()

#Menampilkan plot
plt.show()
