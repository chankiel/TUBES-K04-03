from commands import *
import random
import time

def kumpul(arr_bahan: list[list[any]]) -> None:
    pasir = random.randint(0,5)
    batu = random.randint(0,5)
    air = random.randint(0,5)
    print("Jin menemukan",pasir,"pasir,",batu,"batu, dan",air,"air.")
    arr_bahan[0][2] += pasir
    arr_bahan[1][2] += batu
    arr_bahan[2][2] += air

def batchkumpul(arr_user: list[list[str]],arr_bahan: list[list[any]]) -> None:
    jmlh_jin = count(arr_user, 2, "Pengumpul")
    if jmlh_jin != 0:
        pasir = 0
        batu = 0
        air = 0
        for i in range(jmlh_jin):
            pasir += random.randint(0, 5)
            batu += random.randint(0, 5)
            air += random.randint(0, 5)
        arr_bahan[0][2] += pasir
        arr_bahan[1][2] += batu
        arr_bahan[2][2] += air

        print("Mengerahkan",jmlh_jin,"jin untuk mengumpulkan bahan.")
        print("Jin menemukan total",pasir,"pasir,",batu,"batu, dan",air,"air.")
    else:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")

def bangun(arr_bahan: list[list[any]],arr_candi: list[list[any]],pembuat: str) -> None:
    pasir = random.randint(0,5)
    batu = random.randint(0,5)
    air = random.randint(0,5)

    if (arr_bahan[0][2] >= pasir and arr_bahan[1][2] >= batu and arr_bahan[2][2] >= air):
        temp = count(arr_candi, 0, '')
        if temp != 0:
            indx = firstIndx('', arr_candi, 0)
            arr_candi[indx] = [indx+1,pembuat,pasir,batu,air]
            temp -= 1
        arr_bahan[0][2] -= pasir
        arr_bahan[1][2] -= batu
        arr_bahan[2][2] -= air

        print("Candi berhasil dibangun.")
        print("Sisa candi yang perlu dibangun:",temp)
    else:
        print("Bahan bangunan tidak mencukupi.\nCandi tidak bisa dibangun.")

def batchbangun(arr_user: list[list[str]],arr_bahan: list[list[any]],arr_candi: list[list[any]]) -> None:
    jmlh_jin = count(arr_user, 2, "Pembangun")
    if jmlh_jin != 0:
        temp = time.time()
        total = jumlah_perlu(temp, jmlh_jin)
        random.seed(temp)
        sisa_candi = count(arr_candi, 0, '')
        terbangun = 0
        if (arr_bahan[0][2] >= total[0] and arr_bahan[1][2] >= total[1] and arr_bahan[2][2] >= total[2]):
            for i in range(jmlh_jin):
                pasir = random.randint(0,5)
                batu = random.randint(0, 5)
                air = random.randint(0, 5)
                if sisa_candi != 0:
                    indx = firstIndx('', arr_candi, 0)+1
                    jin = pemilih(arr_user, i+1, "Pembangun", 2, 0)
                    penambah([indx,jin,pasir,batu,air], arr_candi)
                    sisa_candi -= 1
                    terbangun += 1

            arr_bahan[0][2] -= total[0]
            arr_bahan[1][2] -= total[1]
            arr_bahan[2][2] -= total[2]

            print("Mengerahkan",jmlh_jin,"jin untuk membangun candi dengan total bahan",total[0],"pasir,",total[1],"batu, dan",total[2],"air.")
            print("Jin berhasil membangun total",terbangun,"candi.")
        else:
            temp = jumlah_kurang(arr_bahan, total)
            print("Bangun gagal. Kurang",temp[0],"pasir,",temp[1],"batu, dan",temp[2],"air.")
    else:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")

def laporancandi(arr_candi: list[list[any]]) -> None:
    jmlh_candi = 100-count(arr_candi, 0, '')
    print("\n> Total Candi:",jmlh_candi)
    if jmlh_candi != 0:
        print("> Total Pasir yang digunakan:",totalTerpakai(arr_candi, 2))
        print("> Total Batu yang digunakan:",totalTerpakai(arr_candi, 3))
        print("> Total Air yang digunakan:",totalTerpakai(arr_candi, 4))

        candi = CandiTer(arr_candi, "Termahal")
        print(f"> ID Candi Termahal: "+str(candi[0])+" (Rp "+str(candi[1])+")")
        candi = CandiTer(arr_candi, "Termurah")
        print(f"> ID Candi Termurah: "+str(candi[0])+" (Rp "+str(candi[1])+")")
    else:
        print("> Total Pasir yang digunakan: 0")
        print("> Total Batu yang digunakan: 0")
        print("> Total Air yang digunakan: 0")
        print("> ID Candi Termahal: -")
        print("> ID Candi Termurah: -")

def hancurkancandi(arr_candi: list[list[any]]) -> None:
    id = int(input("Masukkan ID candi: "))
    if arr_candi[id-1][0]=="":
        print("\nTidak ada candi dengan ID tersebut.")
    else:
        valid = input("Apakah anda yakin ingin menghancurkan candi ID: "+str(id)+" (Y/N)?")
        if valid=='Y':
            arr_candi[id-1] = ['','','','','']
            print("\nCandi telah berhasil dihancurkan.")

def ayamberkokok(arr_candi: list[list[any]]) -> None:
    print("Kukuruyuk.. Kukuruyuk..")
    jmlh_candi = 100-count(arr_candi, 0, '')
    print("\nJumlah Candi:",jmlh_candi)
    if(jmlh_candi<100):
        print("\nSelamat, Roro Jonggrang memenangkan permainan!\n")
        print("\n*Bandung Bondowoso angry noise*\nRoro Jonggrang dikutuk menjadi candi.")
    else:
        print("\nYah, Bandung Bondowoso memenangkan permainan!")
    exit()