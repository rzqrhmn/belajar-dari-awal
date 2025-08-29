def celcius_ke_fahrenheit(c):
    return (c * 9/5) + 32
def fahrenheit_ke_celcius(f):
    return (f - 32) * 5/9

print("===Konversi Suhu===")
print("1. Celcius ke Fahrenheit")
print("2. Fahrenheit ke Celcius")

pilih = int(input("Pilih (1/2): "))
suhu = float(input("Masukan suhu: "))

if pilih == 1:
    print("Hasil: ", celcius_ke_fahrenheit(suhu), "°F")
elif pilih == 2:
    print("Hasil: ", fahrenheit_ke_celcius(suhu), "°C")
else:
    print("Pilihan tdak valid")