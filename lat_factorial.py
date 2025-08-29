def faktorial (n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*faktorial(n-1)

angka = int(input("Masukan angka: "))
print(f"Faktorial dari {angka} adalah {faktorial(angka)}")