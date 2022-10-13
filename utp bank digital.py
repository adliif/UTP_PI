from ctypes import sizeof
from operator import length_hint


saldo = 10000000
def pengurangan (transaksi):
    total = print ('SISA UANG ANDA ADALAH : ', saldo - transaksi)
    return total

listmenu = ["1. TOP UP GAME","2. TAGIHAN RUMAH","3. ISI PULSA"]
listtopupgame = ["1. Mobile Legends","2. PUBGM"]
listtagihanrumah = ["1. LISTRIK","2. PDAM","3. TELEPON RUMAH","4. WI-FI"]
listisipulsa = ["1. TELKOMSEL","2. TRI","3. INDOSAT","4. XL"]

print('SELAMAT DATANG DI APLIKASI DOMPET DIGITAL \n\n')
passku = input('Silahkan masukkan password Anda untuk melanjutkan : ')

if passku == 'unila':
    print('password anda benar\n')

    try :
        for i in range (0, len(listmenu)):
            print(listmenu[i])

        pilih = int(input("SILAHKAN PILIH MENU YANG TERSEDIA : \n(WAJIB ANGKA!)\nJAWAB : "))
        pilih != 1 or 2 or 3
        if pilih == 1:
            try :
                for i in range (0, len(listtopupgame)):
                    print(listtopupgame[i])
        
                pilih1 = int(input("SILAHKAN PILIH MENU YANG TERSEDIA : \n(WAJIB ANGKA!)\nJAWAB : "))
                pilih != 1 or 2

                if pilih1 == 1:
                    pilihtopup = int(input("SILAHKAN MASUKAN JUMLAH UANG YG INGIN ANDA GUNAKAN : \n(WAJIB ANGKA!)\nJAWAB : "))
                    




        elif pilih == 2:
            print('p')
        elif pilih == 3:
            print('p')
        else:
            print('maaf pilihan tak tersedia')
    except (ValueError, TypeError):
        print("maaf anda memasukan input yang salah")
    else:
        print('jawaban anda : ', pilih)
    finally:
        print('ini selalu tereksekusi')



else:
    if passku.isupper():
        print('perhatikan tanda kapital')
    else:
        print('password anda salah')
    