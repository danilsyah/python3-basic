tup = ('oranges','apples','bananas')
print(tup)
print(type(tup))

# tipe data tuple tidak bisa tambah,edit, hapus data
print(tup[1:2])
print(tup[2])

tup2 = (12,44)
tup3 = tup + tup2
print(tup3)

# mencari jumlah data tuple
print(len(tup3))

tup4 = ('hai')
print(tup4 * 10)

# menghapus tuple
del tup
print(tup) #error karena variabel tiple tup sudah dihapus
