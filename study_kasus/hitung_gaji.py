class Gaji:
    def __init__(self, nama, gajiPokok, isMarried, golongan):
        self.nama = nama
        self.gajiPokok = gajiPokok
        self.isMarried = isMarried
        self.golongan = golongan

    def hitungTunjanganKeluarga(self):
        if self.isMarried is True :
            tunjanganKeluarga = self.gajiPokok * 0.25
        else :
            tunjanganKeluarga = 0

        return tunjanganKeluarga

    def hitungTunjanganJabatan(self):
        if self.golongan ==  "A":
            tunjanganJabatan = self.gajiPokok * 0.3
        elif self.golongan ==  "B":
            tunjanganJabatan = self.gajiPokok * 0.25
        else:
            tunjanganJabatan = self.gajiPokok * 0.15

        return tunjanganJabatan

    def hitungGaji(self):
        gaji = self.gajiPokok + self.hitungTunjanganKeluarga() + self.hitungTunjanganJabatan()
        print(f"nama : {self.nama} \n "
              f"gaji pokok : {self.gajiPokok} \n"
              f"Menikah : {self.isMarried} \n"
              f"golongan : {self.golongan} \n"
              f"Tunjangan keluarga : {self.hitungTunjanganKeluarga()} \n "
              f"Tunjangan jabatan : {self.hitungTunjanganJabatan()} \n"
              f"terima gaji : {gaji}")

nama = input("input nama pegawai : ")
gajiPokok = int(input("input gaji pokok : "))
isMarried = bool(int(input("menikah (1. Yes | 0. No ) ? : ")))
golongan = input("Golongan pilihan (A,B,C) : ")

p = Gaji(nama,gajiPokok,isMarried,golongan)
p.hitungGaji()