list_bilangan = []
bilangan = int(input("masukan bilangan = "))

for i in range(1, bilangan + 1):
    list_bilangan.append(i)

for i in list_bilangan:
    if i % 2 == 0:
        print(f"{i} = bilangan genap")
    else :
        print(f"{i} = bilangan ganjil")