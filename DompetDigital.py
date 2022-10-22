import random
import os

listmenu = ["1. TOP UP GAME", "2. TAGIHAN RUMAH", "3. ISI PULSA"]
listtopupgame = ["\n1. Mobile Legends", "2. PUBGM"]
listtagihanrumah = ["\n1. PLN", "2. PDAM", "3. WIFI"]
listisipulsa = ["\n1. Telkomsel", "2. XL"]
saldo = 300000

def pengurangan(transaksi):
    total = print('Sisa uang Anda : Rp', saldo - transaksi)
    return total

os.system('cls')
print('SELAMAT DATANG DI APLIKASI DOMPET DIGITAL UNILA\n\n')
passku = input('Silahkan masukkan password Anda untuk melanjutkan : ')

if passku == 'unila':
    print('Password anda benar\n')

    try :
        os.system('cls')
        print('SELAMAT DATANG DI APLIKASI DOMPET DIGITAL UNILA\n\n')
        print("\t\t\t\tSaldo anda :", saldo)
        for i in range (0, len(listmenu)):
            print(listmenu[i])

        pilih = int(input("\nSilahkan pilih menu yang tersedia (WAJIB ANGKA!) : "))
        pilih != 1 or 2 or 3
     
        if pilih == 1:
            try :
                os.system('cls')
                for i in range (0, len(listtopupgame)):
                    print(listtopupgame[i])
        
                pilih1 = int(input("\nSilahkan pilih menu yang tersedia (WAJIB ANGKA!) : "))
                pilih1 != 1 or 2

                if pilih1 == 1:
                    os.system('cls')
                    pilihtopup = int(input("Silahkan masukan jumlah diamond yang ingin anda dapatkan (WAJIB ANGKA!) : "))
                    pilihtopup = pilihtopup*1000
                    print('\nTotal harga diamond yang anda keluarkan adalah : Rp.', pilihtopup)
                    pengurangan(pilihtopup)
                elif pilih1 == 2:
                    os.system('cls')
                    pilihtopup = int(input("Silahkan masukan jumlah diamond yg ingin anda dapatkan (WAJIB ANGKA!) : "))                 
                    pilihtopup = pilihtopup*2000
                    print('\nTotal harga diamond yang anda keluarkan adalah : Rp.', pilihtopup)
                    pengurangan(pilihtopup)
                else:
                    print('Maaf pilihan menu tidak tersedia')               
            except (ValueError, TypeError):
                print("Maaf Anda memasukan input yang salah")

        elif pilih == 2:
            try :
                os.system('cls')
                for i in range (0, len(listtagihanrumah)):
                    print(listtagihanrumah[i])
        
                pilih2 = int(input("\nSilahkan pilih menu yang tersedia (WAJIB ANGKA!) : "))
                pilih2 != 1 or 2 or 3

                if pilih2 == 1:
                    os.system('cls')
                    noPLN = int(input('Masukkan nomor pelanggan : '))
                    print('\nnomor token anda adalah : ',random.randint(1000,9999))
                    pengurangan(50000)
                elif pilih2 == 2:
                    os.system('cls')
                    noPDAM = int(input('Masukkan nomor pelanggan : '))
                    print('\nnomor token anda adalah : ',random.randint(1000,9999))
                    pengurangan(50000)
                elif pilih2 == 3:
                    os.system('cls')
                    noWIFI = int(input('Masukkan nomor pelanggan : '))
                    print('\nnomor token anda adalah : ',random.randint(1000,9999))
                    pengurangan(150000)
                else:
                    print('Maaf pilihan menu tidak tersedia')  
            except (ValueError, TypeError):
                print("Maaf Anda memasukan input yang salah")
        
        elif pilih == 3:
            try :
                os.system('cls')
                for i in range (0, len(listisipulsa)):
                    print(listisipulsa[i])
        
                pilih3 = int(input('\nSilahkan pilih menu yang tersedia (WAJIB ANGKA!) : '))
                pilih3 != 1 or 2

                if pilih3 == 1:
                    os.system('cls')
                    nomorHp = int(input('Masukkan nomor Hp\t\t: '))
                    nominal = int(input('Masukkan nominal isi pulsa\t: '))
                    if nominal < 10000:
                        print('Nominal harus minimal Rp10.000')
                    else:
                        pengurangan(nominal)
                elif pilih3 == 2:
                    os.system('cls')
                    nomorHp = int(input('Masukkan nomor Hp\t\t: '))
                    nominal = int(input('Masukkan nominal isi pulsa\t: '))
                    if nominal < 5000:
                        print('Nominal harus minimal Rp5.000')
                    else:
                        pengurangan(nominal)
                else:
                    print('Maaf pilihan menu tidak tersedia')     
            except (ValueError, TypeError):
                print('Maaf Anda memasukan input yang salah')             
        
        else:
            print('Maaf pilihan menu tidak tersedia')
    except (ValueError, TypeError):
        print('Maaf Anda memasukan input yang salah')
else:
    if passku.isupper():
        print('Password menggunakan huruf kecil')
    else:
        print('Password Anda salah') 
