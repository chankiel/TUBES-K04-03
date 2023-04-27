from commands import *

def summonjin(arr_user: list[list[str]]) -> None:    
    if count(arr_user, 0, '') != 0: #Menghitung jumlah baris pada data_user yang kosong (slot jin)
        arr_temp = ['','jin_pengumpul','jin_pembangun']
        print('''Jenis jin yang dapat dipanggil:
(1) Pengumpul - Bertugas mengumpulkan bahan bangunan
(2) Pembangun - Bertugas membangun candi''')

        while True:
            nomor = int(input("\nMasukkan nomor jenis jin yang ingin dipanggil: "))
            if nomor==1:
                print("\nMemilih jin \"Pengumpul\".")
            elif nomor==2:
                print("\nMemilih jin \"Pembangun\".")
            else:
                print("\nTidak ada jenis jin bernomor \""+str(nomor)+"\"!")
                continue
            break
        while True:
            username = input("\nMasukkan username jin: ")
            if firstIndx(username, arr_user, 0) == -1:
                break
            else:
                print("\nUsername \""+username+"\" sudah diambil!")
        while True:
            pw = input("\nMasukkan password jin: ")
            if len(pw)>=5 and len(pw)<=25:
                break
            else:
                print("\nPassword panjangnya harus 5-25 karakter!")
        penambah([username,pw,arr_temp[nomor]],arr_user)
        print('''\nMengumpulkan sesajen...
Menyerahkan sesajen...
Membacakan mantra...''')
        print("\nJin",username,"berhasil dipanggil!")
    else:
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")

def hapusjin(arr_user: list[list[str]],arr_candi: list[list[any]], stack_user: list[list[str]], stack_candi: list[list[any]]) -> None:
    user = input("Masukkan username jin :")
    indx = firstIndx(user, arr_user, 0)
    if indx != -1:
        while True:
            valid = input("Apakah anda yakin ingin menghapus jin dengan username "+user+" (Y/N)? ")
            if valid=="Y" or valid =="N":
                break
            print("Input hanya berupa \"Y\" atau \"N\"!")
        if valid == "Y":
            penambahStack(stack_user, arr_user[indx])
            hapusSemuaCandi(arr_candi, 1, user, stack_candi)
            arr_user[indx] = ['','','']
            print("\nJin telah berhasil dihapus dari alam gaib.")
        else:
            print("\nJin batal dihapus dari alam gaib.")
    else:
        print("\nTidak ada jin dengan username tersebut.")
            
def ubahjin(arr_user: list[list[str]]) -> None:
    user = input("Masukkan username jin : ")
    indx = firstIndx(user, arr_user, 0)
    if indx == -1:
        print("\nTidak ada jin dengan username tersebut")
    else:
        role = arr_user[indx][2]
        if role=="jin_pengumpul":
            while True:
                valid = input("Jin ini bertipe \"Pengumpul\". Yakin ingin mengubah ke tipe \"Pembangun\" (Y/N)? ")
                if valid=="Y" or valid=="N":
                    break
                print("Input hanya berupa \"Y\" atau \"N\"!")
            if valid=="Y":
                arr_user[indx][2] = "jin_pembangun"
                print("Jin telah berhasil diubah.")
            else:
                print("Ubah jin dibatalkan.")
        elif role=='jin_pembangun':
            while True:
                valid = input("Jin ini bertipe \"Pembangun\". Yakin ingin mengubah ke tipe \"Pengumpul\" (Y/N)? ")
                if valid=="Y" or valid=="N":
                    break
                print("Input hanya berupa \"Y\" atau \"N\"!")
            if valid=="Y":
                arr_user[indx][2] = "jin_pengumpul"
                print("Jin telah berhasil diubah.")
            else:
                print("Ubah jin dibatalkan.")
        else:
            print("\nHanya Jin yang dapat diubah tipenya!")

def laporanjin(arr_user: list[list[None]],arr_candi: list[list[any]],arr_bahan: list[list[any]]) -> None:
    total_jin = 100 - count(arr_user, 0, '')
    print("\n> Total Jin:",total_jin)

    total_pengumpul = count(arr_user,2,"jin_pengumpul")
    print("> Total Jin Pengumpul:",total_pengumpul)

    total_pembangun = total_jin-total_pengumpul
    print("> Total Jin Pembangun:",total_pembangun)
    if total_pembangun == 0 and count(arr_candi, 0, '') == 100:
        print("> Jin Terajin: -\n> Jin Termalas: -")
    else:
        list_bangun = listKerja(arr_user, arr_candi)
        print("> Jin Terajin: "+findTerajin(list_bangun))
        print("> Jin Termalas: "+findTermalas(list_bangun))
    print("> Jumlah Pasir: "+str(arr_bahan[0][2])+" unit")
    print("> Jumlah Air: "+str(arr_bahan[2][2])+" unit")
    print("> Jumlah Batu: "+str(arr_bahan[1][2])+" unit")