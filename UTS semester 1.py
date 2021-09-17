#1
def permen(a):
    gula= 1 * a
    permen = 17 * gula
    plastik = permen // 7
    sisapermen = permen % plastik

    print('Jumlah plastik yang akan dijual : ', plastik, 'plastik')
    print('Sisa permen yang tidak dapat dikemas : ', sisapermen, 'buah')


#2
def susuformula():
    kodebarang = input('Masukkan kode barang : ')
    ukuran = int(input('Masukkan ukuran barang (gram) : '))
    jumlah = int(input('Masukkan jumlah barang : '))
    print('\n')

    if kodebarang == 'A':
        if ukuran == 250:
            if jumlah <= 3:
                print('Merk produk ini adalah Dancow')
                print('Ukuran produk ini adalah 250 gram')
                print('Total harga yang perlu anda bayar adalah : Rp', 30000 * jumlah)
            else:
                print('Merk produk ini adalah Dancow')
                print('Ukuran produk ini adalah 250 gram')
                print('Total harga yang perlu anda bayar adalah : Rp',int(30000 - (10/100 * 30000)) * jumlah)
        elif ukuran == 500:
            if jumlah <= 3:
                print('Merk produk ini adalah Dancow')
                print('Ukuran produk ini adalah 500 gram')
                print('Total harga yang perlu anda bayar adalah : Rp', 55000 * jumlah)
            else:
                print('Merk produk ini adalah Dancow')
                print('Ukuran produk ini adalah 500 gram')
                print('Total harga yang perlu anda bayar adalah : Rp',int(55000 - (10/100 * 55000)) * jumlah)
        elif ukuran >= 500:
            if jumlah <= 3:
                print('Merk produk ini adalah Dancow')
                print('Ukuran produk ini adalah lebih dari 500 gram')
                print('Total harga yang perlu anda bayar adalah : Rp', 95000 * jumlah)
            else:
                print('Merk produk ini adalah Dancow')
                print('Ukuran produk ini adalah lebih dari 500 gram')
                print('Total harga yang perlu anda bayar adalah : Rp',int(95000 - (10/100 * 95000)) * jumlah)
        else:
            print('Ukuran yang anda cari tidak tersedia')

    elif kodebarang == 'B':
        if ukuran == 250:
            if jumlah <= 3:
                print('Merk produk ini adalah Morinaga')
                print('Ukuran produk ini adalah 250 gram')
                print('Total harga yang perlu anda bayar adalah : Rp', 85000 * jumlah)
            else:
                print('Merk produk ini adalah Morinaga')
                print('Ukuran produk ini adalah 250 gram')
                print('Total harga yang perlu anda bayar adalah : Rp',int(85000 - (20/100 * 85000)) * jumlah)
        elif ukuran == 500:
            if jumlah <= 3:
                print('Merk produk ini adalah Morinaga')
                print('Ukuran produk ini adalah 500 gram')
                print('Total harga yang perlu anda bayar adalah : Rp', 160000 * jumlah)
            else:
                print('Merk produk ini adalah Morinaga')
                print('Ukuran produk ini adalah 500 gram')
                print('Total harga yang perlu anda bayar adalah : Rp',int(160000 - (20/100 *160000)) * jumlah)
        elif ukuran >= 500:
            if jumlah <= 3:
                print('Merk produk ini adalah Morinaga')
                print('Ukuran produk ini adalah lebih dari 500 gram')
                print('Total harga yang perlu anda bayar adalah : Rp', 280000 * jumlah)
            else:
                print('Merk produk ini adalah Morinaga')
                print('Ukuran produk ini adalah lebih dari 500 gram')
                print('Total harga yang perlu anda bayar adalah : Rp',int(280000 - (20/100 * 280000)) * jumlah)
        else:
            print('Ukuran yang anda cari tidak tersedia')

    elif kodebarang == 'C':
        if ukuran == 250:
            if jumlah <= 3:
                print('Merk produk ini adalah Bebelac')
                print('Ukuran produk ini adalah 250 gram')
                print('Total harga yang perlu anda bayar adalah : Rp', 110000 * jumlah)
            else:
                print('Merk produk ini adalah Bebelac')
                print('Ukuran produk ini adalah 250 gram')
                print('Total harga yang perlu anda bayar adalah : Rp',int(110000 - (25/100 * 110000)) * jumlah)
        elif ukuran == 500:
            if jumlah <= 3:
                print('Merk produk ini adalah Bebelac')
                print('Ukuran produk ini adalah 500 gram')
                print('Total harga yang perlu anda bayar adalah : Rp', 200000 * jumlah)
            else:
                print('Merk produk ini adalah Bebelac')
                print('Ukuran produk ini adalah 500 gram')
                print('Total harga yang perlu anda bayar adalah : Rp',int(200000 - (25/100 * 200000)) * jumlah)
        elif ukuran >= 500:
            if jumlah <= 3:
                print('Merk produk ini adalah Bebelac')
                print('Ukuran produk ini adalah lebih dari 500 gram')
                print('Total harga yang perlu anda bayar adalah : Rp', 390000 * jumlah)
            else:
                print('Merk produk ini adalah Bebelac')
                print('Ukuran produk ini adalah lebih dari 500 gram')
                print('Total harga yang perlu anda bayar adalah : Rp',int(390000 - (25/100 * 390000)) * jumlah)
        else:
            print('Ukuran yang anda cari tidak tersedia')

    elif kodebarang == 'D':
        if ukuran == 250:
            if jumlah <= 3:
                print('Merk produk ini adalah SGM')
                print('Ukuran produk ini adalah 250 gram')
                print('Total harga yang perlu anda bayar adalah : Rp', 25000 * jumlah)
            else:
                print('Merk produk ini adalah SGM')
                print('Ukuran produk ini adalah 250 gram')
                print('Total harga yang perlu anda bayar adalah : Rp',int(25000 - (10/100 * 25000)) * jumlah)
        elif ukuran == 500:
            if jumlah <= 3:
                print('Merk produk ini adalah SGM')
                print('Ukuran produk ini adalah 500 gram')
                print('Total harga yang perlu anda bayar adalah : Rp', 45000 * jumlah)
            else:
                print('Merk produk ini adalah SGM')
                print('Ukuran produk ini adalah 500 gram')
                print('Total harga yang perlu anda bayar adalah : Rp',int(45000 - (10/100 * 45000)) * jumlah)
        elif ukuran >= 500:
            if jumlah <= 3:
                print('Merk produk ini adalah SGM')
                print('Ukuran produk ini adalah lebih dari 500 gram')
                print('Total harga yang perlu anda bayar adalah : Rp', 85000 * jumlah)
            else:
                print('Merk produk ini adalah SGM')
                print('Ukuran produk ini adalah lebih dari 500 gram')
                print('Total harga yang perlu anda bayar adalah : Rp',int(85000 - (10/100 * 85000)) * jumlah)
        else:
            print('Ukuran yang anda cari tidak tersedia')

    elif kodebarang == 'E':
        if ukuran == 250:
            if jumlah <= 3:
                print('Merk produk ini adalah Lactogrow')
                print('Ukuran produk ini adalah 250 gram')
                print('Total harga yang perlu anda bayar adalah : Rp', 9500000 * jumlah)
            else:
                print('Merk produk ini adalah Lactogrow')
                print('Ukuran produk ini adalah 250 gram')
                print('Total harga yang perlu anda bayar adalah : Rp',int(9500000 - (25/100 * 9500000)) * jumlah)
        elif ukuran == 500:
            if jumlah <= 3:
                print('Merk produk ini adalah Lactogrow')
                print('Ukuran produk ini adalah 500 gram')
                print('Total harga yang perlu anda bayar adalah : Rp', 175000 * jumlah)
            else:
                print('Merk produk ini adalah Lactogrow')
                print('Ukuran produk ini adalah 500 gram')
                print('Total harga yang perlu anda bayar adalah : Rp',int(175000 - (25/100 * 175000)) * jumlah)    
        elif ukuran >= 500:
            if jumlah <= 3:
                print('Merk produk ini adalah Lactogrow')
                print('Ukuran produk ini adalah lebih dari 500 gram')
                print('Total harga yang perlu anda bayar adalah : Rp', 315000 * jumlah)
            else:
                print('Merk produk ini adalah Lactogrow')
                print('Ukuran produk ini adalah lebih dari 500 gram')
                print('Total harga yang perlu anda bayar adalah : Rp',int(315000 - (25/100 * 315000)) * jumlah)
        else:
            print('Ukuran yang anda cari tidak tersedia')

    else:
        print('Kode yang anda masukkan salah.')


#3
def looping(angka):
    for x in range(1, angka + 1):
        print("\n")
        for i in range(1, x + 1):
            if x == i:
                hasil = x * i
                print(x,end=' = ')
                print(hasil, end= ' ')
            else:
                print(x,end=' + ')
        
    

# print('\t\tSoal UTS \n')
# print('\tSoal nomor 1','\n')        
# permen(int(input('Masukkan jumlah Gula : ')))
# print('\n')
# print('\tSoal nomor 2','\n')
# susuformula()
# print('\n')
print('\tSoal nomor 3','\n')
looping(int(input('Masukkan angka : ')))
print('\n')