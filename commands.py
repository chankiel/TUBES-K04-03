import time
import math
from typing import List, Union

def read_csv(filename: str,arr: List[List[Union[int,str]]],jenis: str) -> None:
    # Membaca CSV dan menyalinnya ke matriks
    judul = False
    with open(filename,'r') as file:
        i = 0
        for line in file:
            if judul==False:
                judul=True
                continue
            isi = splitStr(line.rstrip(), ';')

            # Untuk data candi, pengisian data dari CSV disesuaikan dengan index baris matriks
            # Jadi jika terdapat data dgn id 1 langsung 3, maka pada index 1 (id 2) diisi kosong
            if jenis=="candi":
                while i+1 < int(isi[0]):
                    arr[i] = ['','','','','']
                    i+=1
            arr[i] = isi
            # Untuk data candi dan data bahan, type casting ke integer utk data angka
            # Untuk data candi, kolom 0(id), 2(pasir), 3(batu), 4(air)
            # Untuk data bahan, kolom 2(jumlah)
            if jenis=="candi":
                arr[i][0] = int(arr[i][0])
                for j in range(2,5):
                    arr[i][j] = int(arr[i][j])

            elif jenis=="bahan":
                arr[i][2] =  int(arr[i][2])

            i+=1

def firstIndx(item: Union[int,str],arr: List[List[Union[int,str]]],column: int) -> int:
    # Mengembalikan indeks baris pertama ditemukannya "item" di kolom "column" pada matriks "arr"
    # Jika tidak ketemu, mengembalikan -1 
    indx = -1
    i = 0
    while arr[i][0] != 99999:
        if arr[i][column] == item:
            return i
        i+=1
    return indx

def lastIndx(item: Union[int,str],arr: List[List[Union[int,str]]],column: int) -> int:
    # Mengembalikan indeks baris terakhir ditemukannya "item" di kolom "column" pada matriks "arr"
    # Jika tidak ketemu, mengembalikan -1 
    indx = -1
    i = 0
    while arr[i][0] != 99999:
        if arr[i][column] == item:
            indx = i
        i+=1
    return indx

def inisialisasi(jenis: str,filename: str) -> List[List[Union[int,str]]]:
    # Menginisialisasi ukuran maksimum matriks dan mengembalikan matriks
    # yang telah diisi dengan isi CSV
    if jenis=="user":
        matrix = [['' for i in range(3)] for j in range(103)]
        matrix[102][0] = 99999
        read_csv(filename, matrix, jenis)
    elif jenis=="bahan":
        matrix = [['' for i in range(3)] for j in range(4)]
        matrix[3][0] = 99999
        matrix[0] = ['pasir','Untuk merekatkan material pembangunan candi',0]
        matrix[1] = ["batu","Sebagai material pembangunan candi",0]
        matrix[2] = ["air","Untuk mengencerkan bahan pembangunan candi",0]
        read_csv(filename, matrix, jenis)
    else:
        matrix = [['' for i in range(5)] for j in range(101)]
        matrix[100][0] = 99999
        read_csv(filename, matrix, jenis)
    return matrix

def penambahStack(stack: List[List[Union[int,str]]],item: List[Union[int,str]]) -> None:
    # Menambahkan "item" pada stack, pengisian dilakukan pada indeks paling bawah yang kosong
    indx = lastIndx('', stack, 0)
    stack[indx] = item

def count(arr: List[List[Union[int,str]]],column: int,item: Union[int,str]) -> int:
    # Mengembalikan jumlah kemunculan "item" di kolom "column" pada matriks "arr" 
    jumlah = 0
    i = 0
    while arr[i][0] != 99999:
        if arr[i][column] == item:
            jumlah += 1
        i+=1
    return jumlah

def pemilih(arr: List[List[Union[int,str]]],pilih: int,item: Union[int,str],kolom_cari: int,kolom_return: int) -> Union[int,str]:
    # Mengembalikan isi "kolom_return" ditemukannya "item" ke "pilih" dari atas pada kolom "kolom_cari" di matriks "arr"
    # Contoh: Return "username" jin dengan role "Pembangun" ke 3 dari atas
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

def penambah(item: Union[int,str],arr: List[List[Union[int,str]]]) -> None:
    # Menambahkan "item" pada baris paling atas matriks "arr" yang kosong
    i = 0
    while arr[i][0] != 99999:
        if arr[i][0] == '':
            arr[i] = item
            break
        i += 1

def jumlah_kurang(bahanPunya: List[List[Union[int,str]]],bahanPerlu: List[int]) -> List[int]:
    # Mengembalikan jumlah bahan yang kurang untuk batchbangun
    bahanKurang = [0,0,0]
    for i in range(3):
        if bahanPunya[i][2] < bahanPerlu[i]:
            bahanKurang[i] = bahanPerlu[i] - bahanPunya[i][2]
    return bahanKurang

def findTerajin(arr_bangun: List[List[Union[int,str]]]) -> str:
    # Mengembalikan jin terajin
    maks = -1
    user = ''
    i = 0
    while arr_bangun[i][0] != 99999:
        if arr_bangun[i][0] != '':
            if arr_bangun[i][1] > maks:
                maks = arr_bangun[i][1]
                user = arr_bangun[i][0]
            elif arr_bangun[i][1] == maks:
                # Mengambil user dengan leksikografis terkecil
                if arr_bangun[i][0] < user:
                    user = arr_bangun[i][0]
        i+=1
        
    return user

def findTermalas(arr_bangun: List[List[Union[int,str]]]) -> str:
    # Mengembalikan jin termalas
    minn = 101 
    user = ''
    i = 0
    while arr_bangun[i][0] != 99999:
        if arr_bangun[i][0] != '':
            if arr_bangun[i][1] < minn:
                minn = arr_bangun[i][1]
                user = arr_bangun[i][0]
            elif arr_bangun[i][1] == minn:
                # Mengambil user dengan leksikografis terbesar
                if arr_bangun[i][0] > user:
                    user = arr_bangun[i][0]
        i+=1
        
    return user

def totalTerpakai(arr_candi: List[List[Union[int,str]]],jenis: int) -> int:
    # Mengembalikan total bahan berjenis "jenis" yang terpakai untuk membuat candi
    # jenis: 2 (pasir), 3 (batu), 4 (air)
    i = 0
    total = 0
    while arr_candi[i][0] != 99999:
        if arr_candi[i][0] != '':
            total += arr_candi[i][jenis]
        i += 1
    return total

def candiTer(arr_candi: List[List[Union[int,str]]],jenis: str) -> List[int]:
    # Mengembalikan index dan harga candi Termahal/Termurah
    # Id dengan harga candi yang sama dipilih Id yang ditemukan pertama (baris teratas)
    if jenis=="Termahal":
        temp = 0
    else:
        temp = float('inf')

    i = 0
    hargaPc = [10000,15000,7500]
    while arr_candi[i][0] != 99999:
        if arr_candi[i][0] != '':
            harga = 0
            for j in range(2,5):
                harga += hargaPc[j-2]*arr_candi[i][j]
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

def hapusSemuaCandi(arr_candi: List[List[Union[int,str]]],kolom_cari: int,item: Union[int,str], stack_candi = List[List[Union[int,str]]]) -> None:
    # Menghapus semua candi yang berisi "item" pada kolom "kolom_cari" pada matriks candi "arr_candi"
    # Digunakan pada hapus jin, dimana menghapus semua candi milik jin tersebut pada matriks candi
    # dan menampungnya pada stack_candi
    i = 0
    while arr_candi[i][0] != 99999:
        if arr_candi[i][kolom_cari] == item:
            penambahStack(stack_candi, arr_candi[i])
            arr_candi[i] = ['','','','','']
        i += 1

def splitStr(string: str,delimiter: str) -> List[str]:
    # Fungsi split() buatan sendiri
    panjang = len(string)
    jmlh_delim = 0
    for i in range(panjang):
        if string[i] == delimiter:
            jmlh_delim += 1
    
    hasil = ['' for i in range(jmlh_delim+1)]
    indx = 0
    for i in range(panjang):
        if string[i] != delimiter:
            hasil[indx] += string[i]
        else:
            indx += 1
    
    return hasil

def salinKeCSV(filename: str,arr: List[List[Union[int,str]]],jenis: str) -> None:
    # Menyalin isi matriks ke file CSV
    with open(filename,'w') as f:
        if jenis == 'user':
            f.write("username;password;role")
        elif jenis == 'candi':
            f.write("id;pembuat;pasir;batu;air")
        else:
            f.write('nama;deskripsi;jumlah')

        i = 0
        while arr[i][0] != 99999:
            if arr[i][0] != '':
                string = '\n' + listToStrCSV(arr[i], jenis)
                f.write(string)
            i+=1

def listToStrCSV(arr: List[List[Union[int,str]]],jenis: str) -> str:
    # Kebalikan dari split, mengubah suatu array dan menggabungnya menjadi string
    # dengan delimiter ";"
    string = ''
    if jenis == "candi":
        jmlh_kolom = 5
    else:
        jmlh_kolom = 3

    for i in range(jmlh_kolom):
        string += str(arr[i])
        if i==jmlh_kolom-1:
            break
        string += ";"
    
    return string

def listKerja(arr_user: List[List[str]],arr_candi: List[List[Union[int,str]]]) -> List[List[Union[int,str]]]:
    # Menglist banyak candi yang dibangun untuk masing-masing jin
    # Untuk jin pengumpul dengan 0 candi dibangun, tidak dicatat
    list_bangun = [['' for i in range(2)]for j in range(101)]
    list_bangun[100][0] = 99999
    i = 0
    while arr_candi[i][0] != 99999:
        if arr_candi[i][0] != '':
            if firstIndx(arr_candi[i][1], list_bangun, 0) == -1:
                penambah([arr_candi[i][1],1], list_bangun)
            else:
                indx = firstIndx(arr_candi[i][1], list_bangun, 0)
                list_bangun[indx][1] += 1
        i+=1

    i = 2
    while arr_user[i][0] != 99999:
        # Mencatat untuk jin pembangun yang belum membangun candi
        if arr_user[i][2] == "jin_pembangun":
            if firstIndx(arr_user[i][0], list_bangun, 0) == -1:
                penambah([arr_user[i][0],0], list_bangun)    
        i += 1
    return list_bangun

def kosongStack(stack_candi: List[List[Union[int,str]]], stack_user: List[List[Union[int,str]]]) -> None:
    # Mengosongkan isi stack
    i = 0
    while stack_candi[i][0] != 99999:
        if stack_candi[i][0] != '':
            stack_candi[i] = ['','','','','']
        i+=1
    i = 0
    while stack_user[i][0] != 99999:
        if stack_user[i][0] != '':
            stack_user[i] = ['','','']
        i+=1

def randomm(x,seeds):
    if x == 0:
        return math.floor(seeds)
    return (randomm(x-1,seeds)*1103515245+12345)%(2**31)