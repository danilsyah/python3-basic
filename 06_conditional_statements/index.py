age = 9
isMarried = True

if(age > 18):
    if (isMarried):
        status = "menikah"
    else:
        status = "single"

    print(f'umur anda {age} : sudah dewasa dan {status}')
elif(age >=10 and age <= 18):
    print(f'umur anda {age} anda masih remaja')
else:
    print(f'umur anda {age} masih kecil')

if(age >= 18 or isMarried == True):
    print("anda sudah menikah")
else:
    print("anda masih bocah")