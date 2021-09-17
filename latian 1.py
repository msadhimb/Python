# #1 bilangan ganjil genap
# x = int(input("Masukkan angka : "))
# if x % 2 == 0:
#     print("Bilangan ini adalah bilangan genap")
# else:
#     print("Bilangan ini adalah bilangan ganjil")

# #2 Swap
# x = int(input("Masukkan angka 1 : "))
# y = int(input("Masukkan angka 2 : "))
# if x > y :
#     print(y, x)

# #Usia Emas
# x = str(input("Masukkan nama anda : "))
# y = int(input("Masukkan usia anda : "))
# usiaemas = 2021 - y
# operasi = usiaemas + 50
# print("Nama anda adalah ", x, ", usia anda adalah ", y, ", anda berusia 50 tahun pada tahun ", operasi)

# #Pembagi
# def cari_faktor(angka):
#     faktor = []
#     for i in range (1, angka + 1):
#         if angka % i == 0:
#             faktor.append(i)
#     return faktor

# angka = int(input("Masukkan angka pembagi : "))
# faktor = cari_faktor(angka)
# print("Angka yang anda tulis adalah ", angka, ", dapat dibagi oleh angka ", faktor)

# #Faktor Persekutuan Terbesar (FPB) dan KPK
# def fpb(x, y):
#     if y == 0:
#         return x
#     else:
#         return fpb(y, x % y)

# def kpk(x, y):
#     return x * y // fpb(x, y)
    
# a = int(input("Masukkan angka 1 : "))
# b = int(input("Masukkan angka 2 : "))
# print("FPB dari ", a, " dan ", b, " adalah ", fpb(a, b))
# print("KPK dari ", a, " dan ", b, " adalah ", kpk(a, b))

# #Bilangan Prima
# def bilprima(x):
#     for i in range(2, x):
#         if x % i == 0:
#             return False    
#     return True

# def bilprima2(angka):
#     listku = []
#     for z in range(1, angka):
#         if bilprima(z):
#             listku.append(z)
#     return listku

# angka = int(input("Masukkan angka : "))
# print(bilprima2(angka))

# #Mencari bilangan terkecil dan terbesar dari list
# def insertionsort(b):
#     temp = 0
#     for i in range(1, len(b)):
#         temp = b[i]
#         j = i - 1
#         while j >= 0 and temp <= b[j]:
#             b[j + 1] = b[j]
#             j -= 1
#         b[j + 1] = temp
#     return b

# b = [int(x) for x in input("Masukkan list : ").split()]
# print("Nilai terkecil dari list tersebut adalah ", insertionsort(b)[0], " dan angka terbesarnya adalah ", insertionsort(b)[len(b)-1])

# #Irisan
# def irisan(listku1, listku2,):
#     listku3 = []
#     for i in listku1:
#         if i in listku2:
#             listku3.append(i)
#     return listku3

# listku1 = [int(x) for x in input("Masukkan list 1 : ").split()]
# listku2 = [int(x) for x in input("Masukkan list 2 : ").split()]
# listku3= []
# print("\n")
# print("Irisan dari list diatas adalah ", irisan(listku1, listku2))
# print("\n")

#Game gunting batu kertas
print("\tGunting Batu Kertas \n")
print("Game ini bisa dimainkan dengan dua orang")
print("Silahkan memilih antara gunting, batu atau kertas")
print("Tulis jawaban anda dibawah \n")
from getpass import getpass
user1 = input("Masukkan nickname player 1 : ")
user2 = input("Masukkan nickname player 2 : ")
database = ['gunting', 'batu', 'kertas']
print("\n")
input1 = getpass("Jawaban player 1 ")
input2 = getpass("Jawaban player 2 ")
if input1 == database[0] and input2 == database[1]:
    print(user2, "menang")
elif input1 == database[1] and input2 == database[0]:
    print(user1, "menang")
elif input1 == database[1] and input2 == database[2]:
    print(user2, "menang")
elif input1 == database[2] and input2 == database[1]:
    print(user1, "menang")
elif input1 == database[2] and input2 == database[0]:
    print(user2, "menang")
elif input1 == database[0] and input2 == database[2]:
    print(user1, "menang")
else:
    print("Ikuti permainan sesuai perintah")
print("\n")