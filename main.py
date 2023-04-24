from fungsi import *
from fungsionalitas import *
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('folder')
args = parser.parse_args()
folder = args.folder
if folder=='':
    print("Tidak ada nama folder yang diberikan!")
    exit()
else:
    path = os.path.join('ExternalFile',args.folder) 
    if os.path.isdir(path)==True:
        print("Selamat datang di program \"Manajerial Candi\"\nSilahkan masukkan command Anda")
    else:
        print("Folder \""+args.folder+"\" tidak ditemukan.")
        exit()

path_file = os.path.join(path,"user.csv")
data_user = inisialisasi("user", path_file)

path_file = os.path.join(path,"bahan_bangunan.csv")
data_bahan = inisialisasi("bahan", path_file)

path_file = os.path.join(path,"candi.csv")
data_candi = inisialisasi("candi", path_file)

data_pembangun = Pembangun(data_user, data_candi)

while True:
    perintah = input(">>>")
    if perintah=="login":
        username = input("Username: ")
        password = input("Password: ")

        status = login(username, password, data_user)
        if status != '':
            while True:
                perintah = input(">>>")
                if perintah=="login":
                    print("Login gagal!\nAnda telah login dengan username "+username+", silahkan lakukan \"logout\" sebelum melakukan login kembali.")
                elif perintah=="logout":
                    break
                elif perintah=="exit":
                    keluar(data_candi, data_bahan, data_user)
                elif perintah=="save":
                    save(data_candi, data_bahan, data_user)
                elif status == "bandung_bondowoso":
                    proses_bandung(perintah, data_bahan, data_candi, data_pembangun, data_user)
                elif status == "roro_jonggrang":
                    proses_roro(perintah, data_candi, data_pembangun)
                elif status == "Pembangun":
                    proses_pembangun(perintah, username, data_bahan, data_candi, data_pembangun, data_user)
                else:
                    proses_pengumpul(perintah, data_bahan)
    elif perintah=="logout":
        print("Logout gagal!\nAnda belum login, silahkan login terlebih dahulu sebelum melakukan logout.")
    elif perintah=="exit":
        keluar(data_candi, data_bahan, data_user)
    elif perintah=="save":
        save(data_candi, data_bahan, data_user)
    elif perintah=="help":
        ket_help(0)
    else:
        print("Masukkan command yang valid!")