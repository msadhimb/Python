def tahunkabisat(tahun):
    habis_dibagi_4 = tahun % 4 == 0
    habis_dibagi_100 = tahun % 100 == 0
    habis_dibagi_400 = tahun % 400 == 0

    if habis_dibagi_400 or (habis_dibagi_4 and not habis_dibagi_100):
        print(f'{tahun} adalah tahun kabisat.')
    else:
        print(f'{tahun} adalah bukan tahun kabisat.')

print('\n')
tahunkabisat(int(input('Masukkan tahun : ')))
print('\n')