saldo = 1_000_000  # saldo awal

while True:
    print("\n=== ATM Sederhana ===")
    print("1. Cek Saldo")
    print("2. Setor Uang")
    print("3. Tarik Uang")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("Saldo anda:", saldo)
    elif pilihan == "2":
        setor = int(input("Jumlah setor: "))
        saldo += setor
        print("Setor berhasil. Saldo sekarang:", saldo)
    elif pilihan == "3":
        tarik = int(input("Jumlah tarik: "))
        if tarik <= saldo:
            saldo -= tarik
            print("Tarik berhasil. Saldo sekarang:", saldo)
        else:
            print("Saldo tidak cukup!")
    elif pilihan == "4":
        print("Terima kasih, sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid!")
