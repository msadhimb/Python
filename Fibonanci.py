# Menghitung fibonanci tanpa rekursif

print('\n')
jumlah_angka = int(input('Masukkan jumlah deret : '))
fibo = [0, 1]

for i in range(2, jumlah_angka):
    angka1 = fibo[i - 2]
    angka2 = fibo[i - 1]
    nextnum = angka1 + angka2
    fibo.append(nextnum)
    
for x in fibo:
    print(x, end=' ')

# print('\n')

# Menghitung fibonanci dengan rekursif

# def fibrekursif(x):
#     if x < 1:
#         return[x]

#     deretke = fibrekursif(x - 1)
#     angka1 = deretke[-2] if len(deretke) > 2 else 0
#     angka2 = deretke[-1] if len(deretke) > 2 else 1

#     return deretke + [angka1 + angka2]

# x=int(input('Masukkan jumlah deret : ') )

# print(fibrekursif(x))
