nilais = []

jml_siswa = int(input("masukan jumlah siswa = "))

for i in range(1, jml_siswa + 1):
    nilai = int(input(f"masukan nilai siswa ke {i} = "))
    nilais.append(nilai)

for i in nilais:
    nilai = i
    if nilai >= 90:
        grade = "A+"
    elif nilai >= 80:
        grade = "A"
    elif nilai >= 70:
        grade = "B"
    elif nilai >= 60:
        grade = "C"
    elif nilai >= 55:
        grade = "D"
    else:
        grade = "E"

    print(f"grade {nilai} = {grade} ")