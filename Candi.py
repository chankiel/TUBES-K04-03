from commands import *
import time
from typing import List, Union

def kumpul(arr_bahan: List[List[Union[int,str]]]) -> None:
    bahan = [0,0,0]
    seeds = time.time()
    for i in range(3):
        bahan[i] = randomm(i, seeds) % 6
    print("Jin menemukan",bahan[0],"pasir,",bahan[1],"batu, dan",bahan[2],"air.")
    for i in range(3):
        arr_bahan[i][2] += bahan[i]

def batchkumpul(arr_user: List[List[str]],arr_bahan: List[List[Union[int,str]]]) -> None:
    jmlh_jin = count(arr_user, 2, "jin_pengumpul")
    if jmlh_jin != 0:
        bahan = [0,0,0]
        seeds = time.time()
        indx = 0
        for i in range(jmlh_jin):
            for j in range(3):
                bahan[j] += randomm(indx, seeds) % 6
                indx += 1
        for i in range(3):
            arr_bahan[i][2] += bahan[i]

        print("Mengerahkan",jmlh_jin,"jin untuk mengumpulkan bahan.")
        print("Jin menemukan total",bahan[0],"pasir,",bahan[1],"batu, dan",bahan[2],"air.")
    else:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")

def bangun(arr_bahan: List[List[Union[int,str]]],arr_candi: List[List[Union[int,str]]],pembuat: str) -> None:
    seeds = time.time()
    bahan = [0,0,0]
    for i in range(3):
        bahan[i] = (randomm(i, seeds) % 5) + 1

    if (arr_bahan[0][2] >= bahan[0] and arr_bahan[1][2] >= bahan[1] and arr_bahan[2][2] >= bahan[2]):
        sisa_candi = count(arr_candi, 0, '')
        if sisa_candi != 0:
            # Jika jumlah candi kurang dari 100, candi dicatat ke data candi
            # Jika sudah lebih dari 100, dianggap tidak ada pembangunan candi tapi bahan tetap dikurangi
            indx = firstIndx('', arr_candi, 0)
            arr_candi[indx] = [indx+1,pembuat,bahan[0],bahan[1],bahan[2]]
            sisa_candi -= 1
        for i in range(3):
            arr_bahan[i][2] -= bahan[i]

        print("Candi berhasil dibangun.")
        print("Sisa candi yang perlu dibangun:",sisa_candi)
    else:
        print("Bahan bangunan tidak mencukupi.\nCandi tidak bisa dibangun.")

def batchbangun(arr_user: List[List[str]],arr_bahan: List[List[Union[int,str]]],arr_candi: List[List[Union[int,str]]]) -> None:
    jmlh_jin = count(arr_user, 2, "jin_pembangun")
    if jmlh_jin != 0:
        seeds = time.time()
        totalPerlu = [0,0,0]
        indx = 0
        for i in range(jmlh_jin):
            for j in range(3):
                totalPerlu[j] += (randomm(indx, seeds) % 5) + 1
                indx += 1

        sisa_candi = count(arr_candi, 0, '')
        terbangun = 0
        if (arr_bahan[0][2] >= totalPerlu[0] and arr_bahan[1][2] >= totalPerlu[1] and arr_bahan[2][2] >= totalPerlu[2]):
            index = 0
            bahan = [0,0,0]
            for i in range(jmlh_jin):
                for j in range(3):
                    bahan[j] = (randomm(index, seeds) % 5) + 1
                    index += 1
                if sisa_candi != 0:
                    # Jika jumlah candi kurang dari 100, candi dicatat ke data candi
                    # Jika sudah lebih dari 100, dianggap tidak ada pembangunan candi tapi bahan tetap dikurangi
                    indx = firstIndx('', arr_candi, 0)+1
                    jin = pemilih(arr_user, i+1, "jin_pembangun", 2, 0)
                    penambah([indx,jin,bahan[0],bahan[1],bahan[2]], arr_candi)
                    sisa_candi -= 1
                    terbangun += 1

            for i in range(3):
                arr_bahan[i][2] -= totalPerlu[i]

            print("Mengerahkan",jmlh_jin,"jin untuk membangun candi dengan total bahan",totalPerlu[0],"pasir,",totalPerlu[1],"batu, dan",totalPerlu[2],"air.")
            print("Jin berhasil membangun total",terbangun,"candi.")
        else:
            totalKurang = jumlah_kurang(arr_bahan, totalPerlu)
            print("Bangun gagal. Kurang",totalKurang[0],"pasir,",totalKurang[1],"batu, dan",totalKurang[2],"air.")
    else:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")

def laporancandi(arr_candi: List[List[Union[int,str]]]) -> None:
    jmlh_candi = 100-count(arr_candi, 0, '')
    print("\n> Total Candi:",jmlh_candi)
    if jmlh_candi != 0:
        # Total bahan yang digunakan hanya pada candi yang tercatat
        print("> Total Pasir yang digunakan:",totalTerpakai(arr_candi, 2))
        print("> Total Batu yang digunakan:",totalTerpakai(arr_candi, 3))
        print("> Total Air yang digunakan:",totalTerpakai(arr_candi, 4))

        info_candi = candiTer(arr_candi, "Termahal")
        print("> ID Candi Termahal: "+str(info_candi[0])+" (Rp "+str(info_candi[1])+")")
        info_candi = candiTer(arr_candi, "Termurah")
        print("> ID Candi Termurah: "+str(info_candi[0])+" (Rp "+str(info_candi[1])+")")
    else:
        print("> Total Pasir yang digunakan: 0")
        print("> Total Batu yang digunakan: 0")
        print("> Total Air yang digunakan: 0")
        print("> ID Candi Termahal: -")
        print("> ID Candi Termurah: -")

def hancurkancandi(arr_candi: List[List[Union[int,str]]]) -> None:
    id = int(input("Masukkan ID candi: "))
    if arr_candi[id-1][0]=="":
        print("\nTidak ada candi dengan ID tersebut.")
    else:
        while True:
            valid = input("Apakah anda yakin ingin menghancurkan candi ID: "+str(id)+" (Y/N)?")
            if valid=='Y' or valid=='N':
                break
            print("Input hanya berupa \"Y\" atau \"N\"!")
        if valid=='Y':
            arr_candi[id-1] = ['','','','','']
            print("\nCandi telah berhasil dihancurkan.")
        else:
            print("Candi gagal dihancurkan")
        

def ayamberkokok(arr_candi: List[List[Union[int,str]]]) -> None:
    print("Kukuruyuk.. Kukuruyuk..")
    jmlh_candi = 100-count(arr_candi, 0, '')
    print("\nJumlah Candi:",jmlh_candi)
    if(jmlh_candi<100):
        print("\nSelamat, Roro Jonggrang memenangkan permainan!\n")
        print("\n*Bandung Bondowoso angry noise*\nRoro Jonggrang dikutuk menjadi candi.")
    else:
        print("\nYah, Bandung Bondowoso memenangkan permainan!")
    exit()