bilangan = int(input("Masukan bilangan = "))
list_bilangan = [i for i in range(2, bilangan+1)]
print(list_bilangan)
print("-"* 50)

bilangan_prima = []

for a in list_bilangan:
    mod = 1
    for b in range(2, a):
        if(a % b == 0):
            mod = 0
    if mod == 1:
        bilangan_prima.append(a)
print(bilangan_prima)
