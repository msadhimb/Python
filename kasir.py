import datetime

print("\t ====================================== ")
print("\t Salman Industries Cafe")
print("\t ====================================== ")
print("\t A. Kopi Susu Mix Tai ----- Rp 20.000")
print("\t B. Kopi Susu Mix Eek ----- Rp 30.000")
print("\t ====================================== ")

hargaa = []
abjadyangdipilih = []
menu1 = {
    'Kopi Susu Mix Tai': 20000
}
menu2 = {
   'Kopi Susu Mix Eek': 30000
}
    
abjad = {
    'a' : menu1,
    'b' : menu2
}
def kasir():
    global klik
    global jumlah
    klik = input('Masukkan abjad kopi yang anda pilih : ')
    jumlah = int(input('Masukkan jumlah kopi yang anda beli : '))
    klik.lower()

    if klik == 'a':
        if klik in abjad:
            abjadyangdipilih.append(klik)
            for i in abjad['a'].values():
                total = jumlah * i
                menu1['Kopi Susu Mix Tai'] = total
                hargaa.append(total)
                break
    elif klik == 'b':
        if klik in abjad:
            abjadyangdipilih.append(klik)
            for i in abjad['b'].values():
                total = jumlah * i
                menu2['Kopi Susu Mix Eek'] = total
                hargaa.append(total)
                break
    struk()

def struk():
    waktu = datetime.datetime.now()
    tahun = waktu.year
    bulan = waktu.month
    tanggal = waktu.day

    totalharga = sum(hargaa)
    cetakstruk = input("Cetak struk ? Ya / Tidak\n")

    if cetakstruk == 'ya':
        print('\n')
        print('======== Salman Industries Cafe ========')
        print(f'============== {tahun}-{bulan}-{tanggal} ===============')
        for x in abjadyangdipilih:
            for i, v in abjad[x].items():
                print(f'{i} x{jumlah}          {v}')
            
    else:
        kasir()

    # print('\n')
    # print('----------------------------------------')
    # print(f'Total                      {totalharga}')
    

kasir()
