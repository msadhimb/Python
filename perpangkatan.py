def perpangkatan():
    angka1 = int(input('Masukkan angka : '))
    angka2 = int(input('Masukkan angka untuk pangkat : '))

    j = angka1
    for i in range(1,angka2):
        hasil = j * angka1
        j = hasil
        
    print('Hasil dari',angka1 , 'pangkat', angka2, 'adalah', hasil)

def perpangkatanTanpaAlgoritma():
    angka1 = int(input('Masukkan angka : '))
    angka2 = int(input('Masukkan angka untuk pangkat : '))

    print('Hasil dari',angka1 , 'pangkat', angka2, 'adalah', angka1 ** angka2)

print('\n')
perpangkatan()
print('\n')
perpangkatanTanpaAlgoritma()
print('\n')