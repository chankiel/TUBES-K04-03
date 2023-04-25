from fungsi import *
import random
from time import *
import os

def login(username,pw,arr_user):
    indx = firstIndx(username, arr_user, 0)
    if indx == -1:
        print("Username tidak terdaftar!")
    else:
        if pw == arr_user[indx][1]:
            print("Selamat datang, "+username+"!\nMasukkan command \"help\" untuk daftar command yang dapat kamu panggil.")
            return arr_user[indx][2]
        else:
            print("Password salah!")
    return ''

def summonjin(arr_user):    
    arr_temp = ['','Pengumpul','Pembangun']
    print('''Jenis jin yang dapat dipanggil:
(1) Pengumpul - Bertugas mengumpulkan bahan bangunan
(2) Pembangun - Bertugas membangun candi''')

    while True:
        nomor = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
        if nomor ==1 or nomor == 2:
            print("Memilih jin \""+arr_temp[nomor]+"\".")
            break
        else:
            print("Tidak ada jenis jin bernomor \""+str(nomor)+"\"!")
    while True:
        username = input("Masukkan username jin: ")
        if firstIndx(username, arr_user, 0) == -1:
            break
        else:
            print("Username \""+username+"\" sudah diambil!")
    while True:
        pw = input("Masukkan password jin: ")
        if len(pw)>=5 and len(pw)<=25:
            break
        else:
            print("Password panjangnya harus 5-25 karakter!")
    penambah([username,pw,arr_temp[nomor]],arr_user)
    print('''Mengumpulkan sesajen...
Menyerahkan sesajen...
Membacakan mantra...''')
    print("Jin",username,"berhasil dipanggil!")
    
def hapusjin(arr_user,arr_candi):
    user = input("Masukkan username jin :")
    indx = firstIndx(user, arr_user, 0)
    if indx != -1:
        valid = input("Apakah anda yakin ingin menghapus jin dengan username "+user+" (Y/N)?")
        if valid == "Y":
            hapusSemuaCandi(arr_candi, 1, user)
            arr_user[indx] = ['','','']
    else:
        print("Tidak ada jin dengan username tersebut.")
            
def ubahjin(arr_user):
    user = input("Masukkan username jin : ")
    indx = firstIndx(user, arr_user, 0)
    if indx == -1:
        print("Tidak ada jin dengan username tersebut")
    else:
        role = arr_user[indx][2]
        if role=="Pengumpul":
            valid = input("Jin ini bertipe \"Pengumpul\". Yakin ingin mengubah ke tipe \"Pembangun\" (Y/N)?")
            if valid=="Y":
                arr_user[indx][2] = "Pembangun"
                print("Jin telah berhasil diubah.")
        elif role=='Pembangun':
            valid = input("Jin ini bertipe \"Pembangun\". Yakin ingin mengubah ke tipe \"Pengumpul\" (Y/N)?")    
            if valid=="Y":
                arr_user[indx][2] = "Pengumpul"
                print("Jin telah berhasil diubah.")
        else:
            print("Hanya Jin yang dapat diubah tipenya!")
    
def kumpul(arr_user,arr_bahan):
    pasir = random.randint(0,5)
    batu = random.randint(0,5)
    air = random.randint(0,5)
    print("Jin menemukan",pasir,"pasir,",batu,"batu, dan",air,"air.")
    arr_bahan[0][2] += pasir
    arr_bahan[1][2] += batu
    arr_bahan[2][2] += air

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

def bangun(arr_bahan,arr_candi,pembuat):
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

def batchbangun(arr_user,arr_bahan,arr_candi):
    jmlh_jin = count(arr_user, 2, "Pembangun")
    if jmlh_jin != 0:
        temp = time()
        total = jumlah_bahan(temp, jmlh_jin)
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
            temp = kurang_bahan(arr_bahan, total)
            print("Bangun gagal. Kurang",temp[0],"pasir,",temp[1],"batu, dan",temp[2],"air.")
    else:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")

def laporanjin(arr_user,arr_candi,arr_bahan):
    total_jin = 100 - count(arr_user, 0, '')
    print("Total Jin:",total_jin)

    total_pengumpul = count(arr_user,2,"Pengumpul")
    print("Total Jin Pengumpul:",total_pengumpul)

    total_pembangun = total_jin-total_pengumpul
    print("Total Jin Pembangun:",total_pembangun)
    if total_pembangun == 0 and count(arr_candi, 0, '') == 100:
        print("Jin Terajin: -\nJin Termalas: -")
    else:
        list_bangun = listKerja(arr_user, arr_candi)
        print("Jin Terajin: "+findTerajin(list_bangun))
        print("Jin Termalas: "+findTermalas(list_bangun))
    print("Jumlah Pasir: "+str(+arr_bahan[0][2])+" unit")
    print("Jumlah Air: "+str(arr_bahan[2][2])+" unit")
    print("Jumlah Batu: "+str(arr_bahan[1][2])+" unit")

def listKerja(arr_user,arr_candi):
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
        if arr_user[i][2] == "Pembangun":
            if firstIndx(arr_user[i][0], list_bangun, 0) == -1:
                penambah([arr_user[i][0],0], list_bangun)    
        i += 1
    return list_bangun

def laporancandi(arr_candi):
    jmlh_candi = 100-count(arr_candi, 0, '')
    print("Total Candi:",jmlh_candi)
    if jmlh_candi != 0:
        print("Total Pasir yang digunakan:",totalBahan(arr_candi, 2))
        print("Total Batu yang digunakan:",totalBahan(arr_candi, 3))
        print("Total Air yang digunakan:",totalBahan(arr_candi, 4))

        candi = CandiTer(arr_candi, "Termahal")
        print(f"ID Candi Termahal: "+str(candi[0])+" (Rp "+str(candi[1])+")")
        candi = CandiTer(arr_candi, "Termurah")
        print(f"ID Candi Termurah: "+str(candi[0])+" (Rp "+str(candi[1])+")")
    else:
        print("Total Pasir yang digunakan: 0")
        print("Total Batu yang digunakan: 0")
        print("Total Air yang digunakan: 0")
        print("ID Candi Termahal: -")
        print("ID Candi Termurah: -")

def hancurkancandi(arr_candi):
    id = int(input("Masukkan ID candi: "))
    if arr_candi[id-1][0]=="":
        print("Tidak ada candi dengan ID tersebut.")
    else:
        valid = input("Apakah anda yakin ingin menghancurkan candi ID: "+str(id)+" (Y/N)?")
        if valid=='Y':
            arr_candi[id-1] = ['','','','','']
            print("Candi telah berhasil dihancurkan.")

def ayamberkokok(arr_candi):
    print("Kukuruyuk.. Kukuruyuk..")
    jmlh_candi = 100-count(arr_candi, 0, '')
    print("Jumlah Candi:",jmlh_candi)
    if(jmlh_candi<100):
        print("Selamat, Roro Jonggrang memenangkan permainan!\n")
        print("*Bandung Bondowoso angry noise*\nRoro Jonggrang dikutuk menjadi candi.")
    else:
        print("Yah, Bandung Bondowoso memenangkan permainan!")

def ket_help(jenis):
    if jenis==0:
        print('''=========== HELP ===========
1. login
   Untuk masuk menggunakan akun
2. exit
   Untuk keluar dari program dan kembali ke terminal''')
    elif jenis==1:
        print('''=========== HELP ===========
1. logout
   Untuk masuk menggunakan akun
2. summonjin
   Untuk memanggil jin
3. hapusjin
   Untuk menghapus jin
4. ubahjin
   Untuk mengubah tipe jin
5. batchkumpul
   Untuk mengerahkan seluruh jin pembangun untuk membangun masing-masing 1 candi
6. batchbangun
   Untuk mengerahkan seluruh jin pengumpul untuk mengumpulkan bahan
7. laporanjin
   Memberikan laporan yang berisi tentang jin
8. laporancandi
   Memberikan laporan yang berisi tentang candi''')
    elif jenis==2:
        print('''=========== HELP ===========
1. hancurkancandi
   Untuk menghancurkan satu candi
2. ayamberkokok
   Untuk memeriksa jumlah candi yang berhasil dibangun dan menentukan pemenangnya''')
    elif jenis==3:
        print('''=========== HELP ===========
1. bangun
   Untuk membangun sebuah candi''')
    else:
        print('''=========== HELP ===========
1. kumpul
   Untuk mengumpulkan baha-bahan candi, yakni pasir,batu,dan air''')

def save(arr_candi,arr_bahan,arr_user):
    folder = input("Masukkan nama folder: ")
    print("Saving...")
    if not os.path.isdir("ExternalFile/save"):
        os.makedirs("ExternalFile/save")
        print("Membuat folder save...")
    path = os.path.join("ExternalFile/save",folder)
    if not os.path.isdir(path):
        os.makedirs(path)
        print("Membuat folder save/"+folder+"...")

    path_file = os.path.join(path,"user.csv")
    salinKeCSV(path_file, arr_user,'user')

    path_file = os.path.join(path,"bahan_bangunan.csv")
    salinKeCSV(path_file, arr_bahan,'bahan')

    path_file = os.path.join(path,"candi.csv")
    salinKeCSV(path_file, arr_candi,'candi')

    print("Berhasil menyimpan data di folder save/"+folder+"!")

def keluar(arr_candi,arr_bahan,arr_user):
    while True:
        valid = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
        if valid=='N' or valid=='n' or valid=="y" or valid=='Y':
            break
    if valid=='Y' or valid=="y":
        save(arr_candi, arr_bahan, arr_user)
    exit()

def proses_bandung(perintah,arr_bahan,arr_candi,arr_user):
    if perintah=="summonjin":
        summonjin(arr_user)
    elif perintah=="hapusjin":
        hapusjin(arr_user, arr_candi)
    elif perintah=="ubahjin":
        ubahjin(arr_user)
    elif perintah=="batchkumpul":
        batchkumpul(arr_user, arr_bahan)
    elif perintah=="batchbangun":
        batchbangun(arr_user, arr_bahan, arr_candi)
    elif perintah=="laporanjin":
        laporanjin(arr_user, arr_candi, arr_bahan)
    elif perintah=="laporancandi":
        laporancandi(arr_candi)
    elif perintah=="help":
        ket_help(1)
    else:
        print("Bandung tidak dapat melakukan command tersebut.")

def proses_roro(perintah,arr_candi):
    if perintah=="hancurkancandi":
        hancurkancandi(arr_candi)
    elif perintah=="ayamberkokok":
        ayamberkokok(arr_candi)
    elif perintah=="help":
        ket_help(2)
    else:
        print("Roro tidak dapat melakukan command tersebut.")

def proses_pembangun(perintah,pembuat,arr_bahan,arr_candi,arr_user):
    if perintah=="bangun":
        bangun(arr_bahan, arr_candi, pembuat)
    elif perintah=="help":
        ket_help(3)
    elif perintah=="laporanjin":
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso")
    elif perintah=="laporancandi":
        print("Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso")
    else:
        print("Jin Pembangun tidak bisa melakukan command tersebut.")

def proses_pengumpul(perintah,arr_bahan):
    if perintah=="kumpul":
        kumpul(arr_bahan)
    elif perintah=="laporanjin":
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso")
    elif perintah=="laporancandi":
        print("Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso")
    elif perintah=="help":
        ket_help(4)
    else:
        print("Jin pengumpul tidak dapat melakukan command tersebut")