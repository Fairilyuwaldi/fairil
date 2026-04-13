print("===KONVERSI SUHU CELCIUS KE FAHRENHEIT===")

# meminta input
celcius = float(input(": masukan suhu dalam derajat celsius: "))

# proses matematika
# rumus: (9/5 * Celcius) + 32
fahrenheit = (9/5 * celcius) + 32

# output
print("\n-- HASIL KONVERSI --")
print(f"suhu awal :{celcius} C")
print(f"Fahrenheit :{fahrenheit} F")