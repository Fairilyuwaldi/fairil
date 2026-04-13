print ("=== PENGHITUNG LUAS LINGKARAN ===")
# Meminta input Jari-Jari 
Jari_Jari = float (input("Masukkan panjang Jari-Jari lingkaran (cm): "))
# Proses matematika 
# Rumus: Pi * r^2
pi = 3.14
luas = pi * (Jari_Jari ** 2)
# Output
print("\n---HASIL PERHITUNGAN ---")
print(f"Jari-Jari lingkaran: {Jari_Jari}cm")
print(f"Luas lingkaran     : {luas} cm persegi")