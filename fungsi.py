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

def Pembangun(arr_user,arr_candi):
    arr = [['' for i in range(3)] for j in range(101)]
    arr[100][0] = 99999
    i_user = 0
    i_arr = 0
    while arr_user[i_user][0] != 99999:
        if arr_user[i_user][2] == "Pembangun":
            arr[i_arr][0] = arr_user[i_user][0]
            arr[i_arr][1] = count(arr_candi, 1, arr[i_arr][0])
            arr[i_arr][2] = "Pembangun"
            i_arr += 1
        i_user += 1
    return arr

def firstIndx(x,arr,column):
    indx = -1
    i = 0
    while arr[i][0] != 99999:
        if arr[i][column] == x:
            return i
        i+=1
    return indx

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

def pemilih(arr,pilih,item,kolom_cari,kolom_return):
    i = 0
    temp = 0
    while arr[i][0] != 99999:
        if arr[i][kolom_cari] == item:
            temp += 1
        if temp == pilih:
            if kolom_return == -1:
                return i
            return arr[i][kolom_return]
        i+=1

def penambah(item,arr):
    i = 0
    while arr[i][0] != 99999:
        if arr[i][0] == '':
            arr[i] = item
            break
        i += 1

def jumlah_bahan(seeds,jmlh):
    arr = [0,0,0]
    random.seed(seeds)
    for i in range(jmlh):
        arr[0] += random.randint(0,5)
        arr[1] += random.randint(0,5)
        arr[2] += random.randint(0,5)
    return arr

def kurang_bahan(punya,perlu):
    kurang = [0,0,0]
    for i in range(3):
        if punya[i][2] < perlu[i]:
            kurang[i] = perlu[i] - punya[i][2]
    return kurang

        
def findTerajin(arr):
    maks = -1
    user = ''
    i = 0
    while arr[i][0] != 99999:
        if arr[i][0] != '':
            if arr[i][1] > maks:
                maks = arr[i][1]
                user = arr[i][0]
            elif arr[i][1] == maks:
                if arr[i][0] < user:
                    user = arr[i][0]
        i+=1
        
    return user

def findTermalas(arr):
    minn = 100 
    user = ''
    i = 0
    while arr[i][0] != 99999:
        if arr[i][0] != '':
            if arr[i][1] < minn:
                minn = arr[i][1]
                user = arr[i][0]
            elif arr[i][1] == minn:
                if arr[i][0] > user:
                    user = arr[i][0]
        i+=1
        
    return user

def jumlahcandi(arr_candi):
    return 100-count(arr_candi, 0, '')

def totalBahan(arr_candi,jenis):
    i = 0
    total = 0
    while arr_candi[i][0] != 99999:
        if arr_candi[i][0] != '':
            total += arr_candi[i][jenis]
        i += 1
    return total

def CandiTer(arr_candi,jenis):
    if jenis=="Termahal":
        temp = 0
    else:
        temp = float('inf')

    i = 0
    indx = -1
    hargaPc = [10000,15000,7500]
    while arr_candi[i][0] != 99999:
        if arr_candi[i][0] != '':
            harga = 0
            for j in range(2,5):
                harga += hargaPc[j-2]
            if jenis=="Termahal":
                if harga > temp:
                    temp = harga
                    indx = i+1
            else:
                if harga < temp:
                    temp = harga
                    indx = i+1
        i+=1
    return [indx,temp]

def hapusSmua(arr_candi,kategori,cek):
    i = 0
    while arr_candi[i][0] != 99999:
        if arr_candi[i][kategori] == cek:
            arr_candi[i] = ['','','','','']
        i += 1


