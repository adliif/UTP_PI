def pengurangan(transaksi):
    total = print('Sisa uang Anda : Rp', saldo - transaksi)
    return total

listmenu = ["1. TOP UP GAME", "2. TAGIHAN RUMAH", "3. ISI PULSA"]
listtopupgame = ["1. Mobile Legends", "2. PUBGM"]
listtagihanrumah = ["1. PLN", "2. PDAM", "3. WIFI"]
listisipulsa = ["1. Telkomsel", "2. XL"]
saldo = 300000

print('SELAMAT DATANG DI APLIKASI DOMPET DIGITAL \n\n')
passku = input('Silahkan masukkan password Anda untuk melanjutkan : ')

if passku == 'unila':
    print('Password anda benar\n')

    try :
        for i in range (0, len(listmenu)):
            print(listmenu[i])

        pilih = int(input("Silahkan pilih menu yang tersedia (WAJIB ANGKA!) : "))
        pilih != 1 or 2 or 3
     
        if pilih == 1:
            try :
                for i in range (0, len(listtopupgame)):
                    print(listtopupgame[i])
        
                pilih1 = int(input("Silahkan pilih menu yang tersedia (WAJIB ANGKA!) : "))
                pilih1 != 1 or 2

                if pilih1 == 1:
                    pilihtopup = int(input("SILAHKAN MASUKAN JUMLAH UANG YG INGIN ANDA GUNAKAN : \n(WAJIB ANGKA!)\nJAWAB : "))
                elif pilih1 == 2:
                    pilihtopup = int(input("SILAHKAN MASUKAN JUMLAH UANG YG INGIN ANDA GUNAKAN : \n(WAJIB ANGKA!)\nJAWAB : "))
                else:
                    print('Maaf pilihan menu tidak tersedia')               
            except (ValueError, TypeError):
                print("Maaf Anda memasukan input yang salah")

        elif pilih == 2:
            try :
                for i in range (0, len(listtagihanrumah)):
                    print(listtagihanrumah[i])
        
                pilih2 = int(input("Silahkan pilih menu yang tersedia (WAJIB ANGKA!) : "))
                pilih2 != 1 or 2 or 3

                if pilih2 == 1:
                    noPLN = int(input('Masukkan nomor pelanggan : '))
                    pengurangan(50000)
                elif pilih2 == 2:
                    noPDAM = int(input('Masukkan nomor pelanggan : '))
                    pengurangan(50000)
                elif pilih2 == 3:
                    noWIFI = int(input('Masukkan nomor pelanggan : '))
                    pengurangan(150000)
                else:
                    print('Maaf pilihan menu tidak tersedia')  
            except (ValueError, TypeError):
                print("Maaf Anda memasukan input yang salah")
        
        elif pilih == 3:
            try :
                for i in range (0, len(listisipulsa)):
                    print(listisipulsa[i])
        
                pilih3 = int(input('Silahkan pilih menu yang tersedia (WAJIB ANGKA!) : '))
                pilih3 != 1 or 2

                if pilih3 == 1:
                    nomorHp = int(input('Masukkan nomor Hp\t: '))
                    nominal = int(input('Masukkan nominal isi pulsa\t: '))
                    if nominal < 10000:
                        print('Nominal harus minimal Rp10.000')
                    else:
                        pengurangan(nominal)
                elif pilih3 == 2:
                    nomorHp = int(input('Masukkan nomor Hp\t: '))
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