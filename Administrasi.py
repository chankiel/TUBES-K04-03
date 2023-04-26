from commands import *
import os

def login(username: str,pw: str,arr_user: list[list[str]]) -> str:
    indx = firstIndx(username, arr_user, 0)
    if indx == -1:
        print("\nUsername tidak terdaftar!")
    else:
        if pw == arr_user[indx][1]:
            print("\nSelamat datang, "+username+"!\nMasukkan command \"help\" untuk daftar command yang dapat kamu panggil.")
            return arr_user[indx][2]
        else:
            print("\nPassword salah!")
    return ''

def undo(stack_user: list[list[str]],stack_candi: list[list[any]],arr_user: list[list[str]],arr_candi: list[list[any]]) -> None:
    indx_user = lastIndx('', stack_user, 0) + 1
    indx_candi = lastIndx('', stack_candi, 0) + 1
    if stack_user[indx_user][0] == 99999:
        print("Stack kosong, tidak bisa melakukan undo.")
    else:
        pembuat = stack_user[indx_user][0]
        if firstIndx(pembuat, arr_user, 0) == -1:
            penambah(stack_user[indx_user], arr_user)
        stack_user[indx_user] = ['','','']

        while stack_candi[indx_candi][1] == pembuat:
            if count(arr_candi, 0, '') != 0:
                indx = firstIndx('', arr_candi, 0)
                stack_candi[indx_candi][0] = indx+1
                arr_candi[indx] = stack_candi[indx_candi]
            stack_candi[indx_candi] = ['','','','','']
            indx_candi += 1
        
        print("Undo berhasil dilakukan, Jin \""+pembuat+"\" telah kembali!")

def save(arr_candi: list[list[any]], arr_bahan: list[list[any]], arr_user: list[list[str]], stack_candi: list[list[any]], stack_user: list[list[any]]) -> None:
    folder = input("\nMasukkan nama folder: ")
    print("\nSaving...")
    if not os.path.isdir("ExternalFile/save"):
        os.makedirs("ExternalFile/save")
        print("\nMembuat folder save...")
    path = os.path.join("ExternalFile/save",folder)
    if not os.path.isdir(path):
        os.makedirs(path)
        print("Membuat folder save/"+folder+"...")

    path_file = os.path.join(path,"user.csv") #ExternalFile/save/save2504/user.csv
    salinKeCSV(path_file, arr_user,'user')

    path_file = os.path.join(path,"bahan_bangunan.csv")
    salinKeCSV(path_file, arr_bahan,'bahan')

    path_file = os.path.join(path,"candi.csv")
    salinKeCSV(path_file, arr_candi,'candi')

    kosongStack(stack_candi, stack_user)
    print("\nBerhasil menyimpan data di folder save/"+folder+"!")

def keluar(arr_candi: list[list[any]],arr_bahan: list[list[any]],arr_user: list[list[str]], stack_candi: list[list[any]], stack_user: list[list[any]]) -> None:
    while True:
        valid = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
        if valid=='N' or valid=='n' or valid=="y" or valid=='Y':
            break
    if valid=='Y' or valid=="y":
        save(arr_candi, arr_bahan, arr_user, stack_candi, stack_user)
    exit()

def proses_bandung(perintah: str,arr_bahan: list[list[any]],arr_candi: list[list[any]],arr_user: list[list[str]],stack_user: list[list[str]], stack_candi: list[list[any]]) -> None:
    if perintah=="summonjin":
        summonjin(arr_user)
    elif perintah=="hapusjin":
        hapusjin(arr_user, arr_candi, stack_user, stack_candi)
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
    elif perintah=="undo":
        undo(stack_user, stack_candi, arr_user, arr_candi)
    else:
        print("Bandung tidak dapat melakukan command tersebut.")

def proses_roro(perintah: str,arr_candi: list[list[any]]) -> None:
    if perintah=="hancurkancandi":
        hancurkancandi(arr_candi)
    elif perintah=="ayamberkokok":
        ayamberkokok(arr_candi)
    elif perintah=="help":
        ket_help(2)
    elif perintah=="laporanjin":
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso")
    elif perintah=="laporancandi":
        print("Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso")
    else:
        print("Roro tidak dapat melakukan command tersebut.")

def proses_pembangun(perintah: str,pembuat: str,arr_bahan: list[list[any]],arr_candi: list[list[any]],arr_user: list[list[str]]) -> None:
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

def proses_pengumpul(perintah: str,arr_bahan: list[list[any]]) -> None:
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

def ket_help(jenis: str) -> None:
    if jenis==0:
        print('''=========== HELP ===========
1. login
   Untuk masuk menggunakan akun
2. save
   Untuk menyimpan progress manajerial candi
3. exit
   Untuk keluar dari program dan kembali ke terminal''')
    elif jenis==1:
        print('''=========== HELP ===========
1. logout
   Untuk keluar dari akun yang digunakan sekarang
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
   Memberikan laporan yang berisi tentang candi
9. undo
   Membatalkan hapus jin dan mengembalikan jin nya beserta candi yang dibangunnya
10.save
   Untuk menyimpan progress manajerial candi
11.exit
   Untuk keluar dari program dan kembali ke terminal ''')
    elif jenis==2:
        print('''=========== HELP ===========
1. logout
   Untuk keluar dari akun yang diguunakan sekarang 
2. hancurkancandi
   Untuk menghancurkan satu candi
2. ayamberkokok
   Untuk memeriksa jumlah candi yang berhasil dibangun dan menentukan pemenangnya
3. save
   Untuk menyimpan progress manajerial candi
4. exit
   Untuk keluar dari program dan kembali ke terminal''')
    elif jenis==3:
        print('''=========== HELP ===========
1. logout
   Untuk keluar dari akun yang digunakan sekarang
2. bangun
   Untuk membangun sebuah candi
3. save
   Untuk menyimpan progress manajerial candi
4. exit
   Untuk keluar dari program dan kembali ke terminal''')
    else:
        print('''=========== HELP ===========
1. logout
   Untuk keluar dari akun yang digunakan sekarang
2. kumpul
   Untuk mengumpulkan baha-bahan candi, yakni pasir,batu,dan air
3. save
   Untuk menyimpan progress manajerial candi
4. exit
   Untuk keluar dari program dan kembali ke terminal''')