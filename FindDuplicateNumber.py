listbaru = []
temp = []
def findmorethan2duplicatenumber(array):
    for i in range(0, len(array)):
        for j in range(0, len(array)):
            if array[i] == array[j]:
                listbaru.append(array[j])
                break
    jumlah()
    return listbaru

def jumlah(): 
    angkaygdicari = int(input('Masukkan angka yang ingin anda cari jumlah pengulangannya : '))  

    for i in range(0, len(listbaru)):
        if angkaygdicari == listbaru[i]:
            temp.append(listbaru[i])
    
    jumlahnya = len(temp)
    
    print(f'Angka {angkaygdicari} diulang sebanyak {jumlahnya} kali')

 

print('\n')    
findmorethan2duplicatenumber([int(x) for x in input("Masukkan angka list : ").split()])
