import random

def read_csv(filename,arr):
    judul = False
    with open(filename,'r') as file:
        i = 0
        for line in file:
            if judul==False:
                judul=True
                continue
            arr[i] = (line.rstrip()).split(';')

            if filename=="candi.csv":
                arr[i][0] = int(arr[i][0])
                for j in range(2,5):
                    arr[i][j] = int(arr[i][j])

            elif filename=="bahan_bangunan.csv":
                arr[i][2] =  int(arr[i][2])

            i+=1

def isMember(x,arr,column):
    indx = -1
    i = 0
    while arr[i][0] != 99999:
        if arr[i][column] == x:
            return i
        i+=1

def inisialisasi(jenis):
    if jenis=="user":
        matrix = [['' for i in range(3)] for j in range(103)]
        matrix[102][0] = 99999
        read_csv("user.csv", matrix)
    elif jenis=="bahan":
        matrix = [['' for i in range(3)] for j in range(4)]
        matrix[3][0] = 99999
        matrix[0][0] = "pasir"
        matrix[1][0] = "batu"
        matrix[2][0] = "air"
        matrix[0][2] = matrix[1][2] = matrix[2][2] = 0
        read_csv("bahan_bangunan.csv", matrix)
    else:
        matrix = [['' for i in range(5)] for j in range(101)]
        matrix[100][0] = 99999
        read_csv("candi.csv", matrix)
    return matrix

def count(arr,column,x):
    jumlah = 0
    i = 0
    while arr[i][0] != 99999:
        if arr[i][column] == x:
            jumlah += 1
        i+=1
    return jumlah

data_user = inisialisasi("user")
data_bahan = inisialisasi("bahan")
data_candi = inisialisasi("candi")

def ubahjin(arr):
    user = input("Masukkan username jin : ")
    indx = isMember(user,arr,0)
    if indx == -1:
        print("Tidak ada jin dengan username tersebut")
    else:
        role = arr[indx][2]
        if role=="Pengumpul":
            valid = input("Jin ini bertipe \"Pengumpul\". Yakin ingin mengubah ke tipe \"Pembangun\" (Y/N)?")
            if valid=="Y":
                arr[indx][2] = "Pembangun"
                print("Jin telah berhasil diubah.")
        else:
            valid = input("Jin ini bertipe \"Pembangun\". Yakin ingin mengubah ke tipe \"Pengumpul\" (Y/N)?")    
            if valid=="Y":
                arr[indx][2] = "Pengumpul"
                print("Jin telah berhasil diubah.")

def kumpul(arr_user,arr_bahan):
    temp = isMember("Pengumpul", arr_user, 2)
    if temp != -1:
        pasir = random.randint(0,5)
        batu = random.randint(0,5)
        air = random.randint(0,5)
        print("Jin menemukan",pasir,"pasir,",batu,"batu, dan",air,"air.")
        arr_bahan[0][2] += pasir
        arr_bahan[1][2] += batu
        arr_bahan[2][2] += air
    else:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")  

def batchkumpul(arr_user,arr_bahan):
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

def pemilih(arr_user,pilih,item,kolom_cari,kolom_return):
    i = 0
    temp = 0
    while arr_user[i][0] != 99999:
        if arr_user[i][kolom_cari] == item:
            temp += 1
        if temp == pilih:
            if kolom_return == -1:
                return i
            return arr_user[i][kolom_return]
        i+=1

def bangun(arr_bahan,arr_user,arr_candi,pembuat):
    pasir = random.randint(0,5)
    batu = random.randint(0,5)
    air = random.randint(0,5)

    if (arr_bahan[0][2] >= pasir and arr_bahan[1][2] >= batu and arr_bahan[2][2] >= air):
        temp = count(arr_candi, 0, '')
        if temp != 0:
            indx = isMember('', arr_candi, 0)
            arr_candi[indx] = [indx+1,pembuat,pasir,batu,air]
            temp -= 1
        arr_bahan[0][2] -= pasir
        arr_bahan[1][2] -= batu
        arr_bahan[2][2] -= air
        print("Candi berhasil dibangun.")
        print("Sisa candi yang perlu dibangun:",temp)
    else:
        print("Bahan bangunan tidak mencukupi.\nCandi tidak bisa dibangun.")
