import pandas as pd

data = {
    "Nama Mata Kuliah": [],
    "SKS": [],
    "Nilai": []
}

for i in range(3):
    print(f"\nData ke-{i+1}")
    nama = input("Masukkan nama matkul : ")
    sks = int(input("SKS : "))
    nilai = int(input("Nilai : "))
    
    data["Nama Mata Kuliah"].append(nama)
    data["SKS"].append(sks)
    data["Nilai"].append(nilai)
    
df = pd.DataFrame(data)

print("\n===== DATA NILAI MATA KULIAH =====")
print(df)