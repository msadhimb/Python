def pencariangkaterbesar():
    deret = [int(x) for x in input("Masukkan List untuk selection sort : ").split()]
    print(deret)
    deret.sort()
    print('Angka terbesar dari list tersebut adalah', deret[len(deret) - 1])

def b():
    deret = []
    angka1 = int(input('Mssukkan angka 1 : '))
    angka2 = int(input('Mssukkan angka 2 : '))
    angka3 = int(input('Mssukkan angka 3 : '))

    deret.append(angka1)
    deret.append(angka2)
    deret.append(angka3)

    deret.sort()

    print('Angka terkecil dari list tersebut adalah', deret[0])
    print('Angka tengah dari list tersebut adalah', deret[1])
    print('Angka terbesar dari list tersebut adalah', deret[2])

print('\n')
b()
print('\n')