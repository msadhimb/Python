def faktorial():
    angka1 = int(input('Masukkan angka : '))

    hasil = angka1
    for i in range(1, angka1):
        hasil *= i
    
    print(f'{angka1}!(faktorial) adalah {hasil}')

print('\n')
faktorial()
print('\n')