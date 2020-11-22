total_harga = 0
menu = 0
while menu != 6:
    print("+----------------Menu Makanan--------------+")
    print("1. Nasi goreng = Rp. 15.000")
    print("2. Baso = Rp. 13.000")
    print("3. Mie Ayam = Rp. 14.000")
    print("4. Teh Obeng = Rp. 5000")
    print("5. Es jeruk = Rp. 7000")
    print("6. bayar")
    menu = int(input("pilih menu = "))
    if menu == 1:
        harga = 15000
    elif menu == 2:
        harga = 13000
    elif menu == 3:
        harga = 14000
    elif menu == 4:
        harga = 5000
    elif menu == 5:
        harga = 7000
    elif menu == 6:
        continue

    total_harga = total_harga + harga
    print(f"total harga = {total_harga}")
else:
    print("-----Pembayaran------")
    print(f"total harga = {total_harga}")
    bayar = int(input("Masukan pembayaran = "))
    kembalian = bayar - total_harga
    print(f"kembalian = {kembalian}")

