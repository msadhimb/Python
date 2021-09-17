from getpass import getpass

def aturan():
    print("\tGunting Batu Kertas \n")
    print("Game ini bisa dimainkan dengan dua orang")
    print("Silahkan memilih antara gunting, batu atau kertas")
    print("Tulis jawaban anda dibawah \n")

def permainan():
    nick1 = input('Masukkan nickname player 1 = ')
    nick2 = input('Masukkan nickname player 2 = ')
    print(nick1, 'dan', nick2, 'silahkan menyiapkan jawaban')
    jawaban1 = getpass('Masukkan jawaban player 1 ')
    jawaban2 = getpass('Masukkan jawaban player 2 ')
    database = ['gunting' , 'batu', 'kertas']
    if jawaban1 == database[0] and jawaban2 == database[1]:
        print(nick2, "menang")
    elif jawaban1 == database[1] and jawaban2 == database[0]:
        print(nick1, "menang")
    elif jawaban1 == database[1] and jawaban2 == database[2]:
        print(nick2, "menang")
    elif jawaban1 == database[2] and jawaban2 == database[1]:
        print(nick1, "menang")
    elif jawaban1 == database[2] and jawaban2 == database[0]:
        print(nick2, "menang")
    elif jawaban1 == database[0] and jawaban2 == database[2]:
        print(nick1, "menang")
    else:
        print("Ikuti permainan sesuai perintah")    

def main():
    aturan()
    permainan()

main()


