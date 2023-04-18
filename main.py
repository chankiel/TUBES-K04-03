from fungsi import *
from fungsionalitas import *

data_user = inisialisasi("user")
data_bahan = inisialisasi("bahan")
data_candi = inisialisasi("candi")

data_pembangun = Pembangun(data_user,data_candi)

summonjin(data_pembangun, data_user)
bangun(data_bahan, data_user, data_candi, data_pembangun, "Kiel")
batchbangun(data_user, data_pembangun, data_bahan, data_candi)
print(data_user)
print(data_candi)
ayamberkokok(data_candi)
