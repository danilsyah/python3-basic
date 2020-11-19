students = {"danil":12, "razil":11, "haykal":43}
# mengakses dictionary
print(students)
print(students['danil'])
students['razil'] = 15
print(students['razil'])

# delete data
del students["razil"]
print(students)

# mendapatkan jumlah data
print(len(students))
print(type(students))