def tambah(a, b): return a + b
def kurang(a, b): return a - b
def kali(a, b): return a * b
def bagi(a, b): return a / b

print("===== Calculator =====")
print("1. Sum\n2. Substract\n3. Multiply\n4. Divide")

option = int(input("Choose the operation (1-4): "))
a = int(input("Input 1st number = "))
b = int(input("Input 2nd number = "))

if option == 1:
    print("Result: ", tambah(a,b))
elif option == 2:
    print("Result: ", kurang(a,b))
elif option == 3:
    print("Result: ", kali(a,b))
elif option == 4:
    print("Result: ", bagi(a,b))