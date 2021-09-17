def bilprim():
    input1 = int(input('Masukkan angka : '))

    if input1 >= 3:
        if input1 % 2 == 0:
            print(input1, 'BUKAN angka PRIMA.')
        else:
            print(input1, 'adalah angka PRIMA.')
    elif input1 in range (1,3):
        print(input1, 'adalah angka PRIMA.')
    else:
        print(input1, 'BUKAN angka PRIMA.')

bilprim()