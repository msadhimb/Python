import statistics
import math

# Mean
    #menghitung manual
def mean():
    angka= [int(x) for x in input("Masukkan nilai : ").split(',')]
    
    jumlahdata = sum(angka)
    banyaknilai = len(angka)
        
    ratarata = jumlahdata / banyaknilai

    print('Mean/rata rata dari angka tersebut adalah', ratarata)

    #menghitung otomatis
def meanAt():
    angka = [int(x) for x in input("Masukkan nilai : ").split(',')]
    print('Mean/rata rata dari angka tersebut adalah', statistics.mean(angka))

mean()
# Modus
    #menghitung manual
def modus():
    angka = [int(x) for x in input("Masukkan nilai : ").split(',')]
    temp = []
    mboh = {}

    for x in range(0, len(angka)):
        for j in range(x + 1, len(angka)):
            if angka[x] == angka[j]:
                temp.append(angka[x])
                temp.sort()
                break

    temp = list(dict.fromkeys(temp))

    for i in temp:
        jum = angka.count(i)
        mboh[i] = jum
    
    mboh = sorted(zip(mboh.values(), mboh.keys()))
    mboh = (dict(mboh))
    print('Modus dari angka tersebut adalah', list(mboh.values())[-1])

    #menghitung otomatis
def modusAt():
    angka = [int(x) for x in input('Masukkan angka : ').split(',')]
    print('Modus dari angka tersebut adalah', statistics.mode(angka))

# Median
    #menghitung manual
def median():
    angka = [int(x) for x in input("Masukkan nilai : ").split(',')]
    angka = sorted(angka)
    
    if len(angka) % 2 == 0:
        jum = len(angka) // 2
        angkatengah = (angka[jum - 1] + angka[jum]) / 2
        print('Median dari angka tersebut adalah', angkatengah)
    else:
        jum = len(angka) // 2
        print('Median dari angka tersebut adalah', angka[jum])

    #menghitung otomatis
def medianAt():
    angka = [int(x) for x in input('Masukkan nilai : ').split(',')]
    print('Median dari angka tersebut adalah', statistics.median(angka))

# Standar Deviasi / Simpangan Baku
    #menghitung manual
def simpanganbaku():
    angka = [int(x) for x in input('Masukkan nilai : ').split(',')]
    ratarata = statistics.mean(angka)
    temp = []

    for i in angka:
        s = (i - ratarata) ** 2
        temp.append(s)
        
    sigma = sum(temp)

    simpangan = math.sqrt(sigma/ratarata)
    print(simpangan)

    #menghitung otomatis
def simpanganbakuAt():
    angka = [int(x) for x in input("Masukkan nilai : ").split(',')]
    print('Simpangan baku dari angka tersebut adalah', statistics.pstdev(angka))

