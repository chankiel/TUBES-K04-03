from commands import *
from Administrasi import *
from Candi import *
from Jin import *
import argparse
import os

# Menerima Argument Load
parser = argparse.ArgumentParser()
parser.add_argument('folder')
args = parser.parse_args()
folder = args.folder
if folder is None:
    print("Tidak ada nama folder yang diberikan!")
    print("Usage: python main.py <nama_folder>")
    exit()
else:
    path = os.path.join('ExternalFile',args.folder) 
    if os.path.isdir(path)==True:
        print("Selamat datang di program \"Manajerial Candi\"\nMasukkan command \"help\" untuk daftar command yang dapat kamu panggil.")
    else:
        print("Folder \""+args.folder+"\" tidak ditemukan.")
        exit()

# Load CSV ke Matrix
path_file = os.path.join(path,"user.csv") #ExternalFile/Inisial/user.csv
data_user = inisialisasi("user", path_file)

path_file = os.path.join(path,"bahan_bangunan.csv")
data_bahan = inisialisasi("bahan", path_file)

path_file = os.path.join(path,"candi.csv")
data_candi = inisialisasi("candi", path_file)

# Inisialisasi Stack utk Undo
stack_user = [['' for i in range(3)] for j in range(101)]
stack_user[100][0] = 99999

stack_candi = [['' for i in range(5)] for j in range(10001)]
stack_candi[10000][0] = 99999

# Program Utama
while True:
    perintah = input(">>>")
    if perintah=="login":
        username = input("Username: ")
        password = input("Password: ")

        status = login(username, password, data_user)
        if status != '':
            while True:
                perintah = input("\n>>>")
                if perintah=="login":
                    print("Login gagal!\nAnda telah login dengan username "+username+", silahkan lakukan \"logout\" sebelum melakukan login kembali.")
                elif perintah=="logout":
                    break
                elif perintah=="exit":
                    keluar(data_candi, data_bahan, data_user, stack_candi, stack_user)
                elif perintah=="save":
                    save(data_candi, data_bahan, data_user, stack_candi, stack_user)
                elif status == "bandung_bondowoso":
                    proses_bandung(perintah, data_bahan, data_candi, data_user, stack_user, stack_candi)
                elif status == "roro_jonggrang":
                    proses_roro(perintah, data_candi)
                elif status == "Pembangun":
                    proses_pembangun(perintah, username, data_bahan, data_candi, data_user)
                else:
                    proses_pengumpul(perintah, data_bahan)
    elif perintah=="logout":
        print("Logout gagal!\nAnda belum login, silahkan login terlebih dahulu sebelum melakukan logout.")
    elif perintah=="exit":
        keluar(data_candi, data_bahan, data_user, stack_candi, stack_user)
    elif perintah=="save":
        save(data_candi, data_bahan, data_user, stack_candi, stack_user)
    elif perintah=="help":
        ket_help(0)
    else:
        print("Masukkan command yang valid!")