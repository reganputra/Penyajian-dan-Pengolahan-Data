import pandas as pd
import numpy as np
from statistics import mode, StatisticsError

# Membaca data dari file Excel
path = 'C:\Kuliah\Semester 3\Statistika Komputasi\Code statkom\dataRegan.xlsx'
df = pd.read_excel(path, skiprows=1, usecols='A:E', nrows=2129)

#Mengganti nama kolom sesuai pada excel
df.columns = ['age', 'total_value', 'avg_year', 'total_guaranteed', 'fully_guaranteed']

# Menghitung mean, median, modus, standar deviasi, dan varians untuk setiap kolom
for kolom in df.columns:
    data = df[kolom].tolist()

    # Menghitung mean
    mean = np.mean(data)

    # Menghitung median
    median = np.median(data)

    # Menghitung modus
    try:
        modus = mode(data)
    except StatisticsError:
        modus = "Tidak ada modus"

    # Menghitung standar deviasi
    std_deviation = np.std(data)

    # Menghitung varians
    variance = np.var(data)

    # Menampilkan hasil statistik
    print(f"Statistik untuk Kolom '{kolom}':")
    print(f"Mean: {mean:.6f}")
    print(f"Modus: {modus:.6f}")
    print(f"Median: {median:.6f}")
    print(f"Variansi: {variance:.6f}")
    print(f"Standar Deviasi: {std_deviation:.6f}")
    print()
