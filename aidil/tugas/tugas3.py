print("=== KALKULATOR BMI===")
# Meminta input dan mengubahnya menjadi float (desimal)
berat = float(input("Masukan berat badan anda (kg) :"))
tinggi = float(input("Masukan tinggi badan anda (meter, contoh 1.70): "))

# Proses perhitungan matematika
# Rumus BMI: Berat / (Tinggi kuadrat)
bmi = berat / (tinggi ** 2)

# Output menggunakan f-string
# Tips: {:.2f} digunakan untuk membatasi angka desimal hanya 2 di belakang koma
print("\n--- HASIL ---")
print(f"Berat Badan     : {berat} kg")
print(f"Tinggi Badan    : {tinggi} m")
print(f"Skor BMI Anda   : {bmi:.2f}")