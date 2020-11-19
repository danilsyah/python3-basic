# belajar list
shopList = ['Apples','Oranges','Bananas','Cheese']
print(shopList);
print(shopList[0])
print(shopList[0:3])

# menambahkan data list di akhir index
shopList.append("Manggo")
print(shopList)

# ganti value list sesuai index
shopList[2] = 'durian'
print(shopList)

# delete value
del shopList[2]
print(shopList)

# menggabungkan 2 list
shopList2 = ["udin","danil","nufika","haykal"]
print(shopList + shopList2)

# membuat data list menjadi double
print(shopList * 2)

# mencari nilai list tertinggi
listNum = [2,44,4,31,23]
print(max(listNum))
# mencari nilai list terkecil
print(min(listNum))