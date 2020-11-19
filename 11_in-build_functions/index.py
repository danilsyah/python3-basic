# belajar function bawaan dari python

# abs() -> membuat number selalu menjadi positif
print(abs(-21))
print(abs(24))

# bool() selain dari berisi none atau 0 maka me-return True
print(bool(0)) #False
print(bool(12)) #True
print(bool(None)) #False

# function dir untuk mengecek method apa saja yang tersedia pada variabel
print(dir("hello"))

sent = "hello"
print(sent.upper())
# menggunakan method help untuk menjelaskan pengertian method
help(sent.upper)
help(sent.replace)

print(sent.replace("h","a"))

# method eval()
sent = 'print("Hi")'
eval(sent)
exec(sent)
print(eval("2*3")) #6

# parsing / konversi data type
a = 10
b = 321.003
print(str(a))
print(float(a))
print(int(b))
print(bool(b))
print(bool(0))
print(bool(None))
