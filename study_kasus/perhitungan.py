def tambah(a,b):
    return a + b

def kurang(a,b):
    return a - b

def kali(a,b):
    return a * b

def bagi(a,b):
    return a / b


print("--- Program operator aritmatika ---")
print("1. tambah")
print("2. kurang")
print("3. kali")
print("4. bagi")
menu = int(input("Input pilihan operator = "))
bil1 = int(input("input bil pertama = "))
bil2 = int(input("input bil kedua = "))

if menu == 1:
    hasil = tambah(bil1,bil2)
    print(f"hasil dari penjumlahan {bil1} + {bil2} = {hasil}")
elif menu == 2:
    hasil = kurang(bil1, bil2)
    print(f"hasil dari pengurangan {bil1} - {bil2} = {hasil}")
elif menu == 3:
    hasil = kali(bil1, bil2)
    print(f"hasil dari perkalian {bil1} x {bil2} = {hasil}")
else:
    hasil = bagi(bil1, bil2)
    print(f"hasil dari pembagian {bil1} / {bil2} = {hasil}")
