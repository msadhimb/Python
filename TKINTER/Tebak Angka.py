from tkinter import*
import random

class TebakAngka():

    def __init__(self):
        # memanggil method code()
        self.code()

    def code(self):
        self.label1 = Label(root, text='Selamat Datang digame tebak angka \n Disini kami(komputer) akan memilih sebuah angka \n dari 1 sampai 100, tugas anda adalah menebak angka berapa itu. \n')
        self.label1.pack()

        self.button1 = Button(root, text='Mulai', padx=20, pady=10, command=lambda: self.mainframe()) # membuat button Mulai
        self.button1.pack() # menampilkan button Mulai

    def mainframe(self):
        self.button1.pack_forget()

        self.label2 = Label(root, text='Baik \n Kami telah mendapatkan angkanya. \n Mulailah untuk menebak. \n')
        self.label2.pack()

        self.entry1 = Entry(root, width=50, borderwidth=5) # membuat sebuah box untuk menginput
        self.entry1.insert(0, 'Masukkan angka yang akan anda pilih disini.') # memasukkan text pada box input1
        self.entry1.pack() # menampilkan input1

        self.angka=random.randint(1,100)

        self.button2 = Button(root, text='Enter', padx=20, pady=10, command=lambda: self.game(angkaku=self.entry1.get()))
        self.button2.pack()
        
        print('\n') # menampilkan di terminal
        print('Kami telah mendapatkan angka, silahkan menebak angka berapa. Mulai dari 1 - 100.\n')

    def mainframeclone(self):
        self.button1.pack_forget()
        self.entry1.pack_forget()
        self.button2.pack_forget()

        self.entry2 = Entry(root, width=50, borderwidth=5) # membuat sebuah box untuk menginput
        self.entry2.insert(0, 'Masukkan angka yang akan anda pilih disini. \n') # memasukkan text pada box input1
        self.entry2.pack() # menampilkan input1

        self.angka=random.randint(1,100)

        self.button3 = Button(root, text='Enter', padx=20, pady=10, command=lambda: self.gameclone(angkaku=self.entry2.get()))
        self.button3.pack()
        
        print('\n') # menampilkan di terminal
        print('Kami telah mendapatkan angka, silahkan menebak angka berapa. Mulai dari 1 - 100.\n')

    def game(self, angkaku):
        self.mainframeclone()

        if int(angkaku) == self.angka:
            self.entry1.pack_forget()
            self.button2.pack_forget()
            self.entry2.pack_forget()
            self.button3.pack_forget()

            self.label3 = Label(root, text='Selamat anda benar. \n')
            self.label3.pack()

            self.button4 = Button(root, text='Mulai lagi', padx=20, pady=10, command=lambda: self.hapus())
            self.button4.pack()

            print(f'Selamat jawaban anda benar.{self.entry1.get()}\n')
                
        elif int(angkaku) < self.angka:
            self.label3 = Label(root, text='Angka ini terlalu kecil.')
            self.label3.pack()

            print(f"angka ini terlalu kecil.{self.entry1.get()} \n")

        elif int(angkaku) in range(self.angka, self.angka + 4):
            self.label3 = Label(root, text='Anda sudah mendekati.')
            self.label3.pack()

            print(f'Anda sudah mendekati.{self.entry1.get()} \n')

        else:
            self.label3 = Label(root, text='Angka ini terlalu besar.')
            self.label3.pack()

            print(f'angka ini terlalu besar.{self.entry1.get()} \n')
        

    def gameclone(self, angkaku):
        self.label3.pack_forget()

        if int(angkaku) == self.angka:
            self.entry1.pack_forget()
            self.button2.pack_forget()
            self.entry2.pack_forget()
            self.button3.pack_forget()

            self.label3 = Label(root, text='Selamat anda benar.\n')
            self.label3.pack()

            self.button4 = Button(root, text='Mulai lagi', padx=20, pady=10, command=lambda: self.hapus())
            self.button4.pack()

            print(f'Selamat jawaban anda benar.{self.entry2.get()}\n')
                
        elif int(angkaku) < self.angka:
            self.label3 = Label(root, text='Angka ini terlalu kecil.')
            self.label3.pack()

            print(f"angka ini terlalu kecil.{self.entry2.get()} \n")

        elif int(angkaku) in range(self.angka -4, self.angka + 4):
            self.label3 = Label(root, text='Anda sudah mendekati.')
            self.label3.pack()

            print(f'Anda sudah mendekati.{self.entry2.get()} \n')

        else:
            self.label3 = Label(root, text='Angka ini terlalu besar.')
            self.label3.pack()

            print(f'angka ini terlalu besar.{self.entry2.get()} \n')

    def hapus(self):
        # menghapus semua variable yang muncul di tkinter
        self.entry1.pack_forget()
        self.entry2.pack_forget()
        self.label1.pack_forget()
        self.label2.pack_forget()
        self.label3.pack_forget()
        self.button1.pack_forget()
        self.button2.pack_forget()
        self.button3.pack_forget()
        self.button4.pack_forget()

        # memanggil kembali code() dan memulai semua dari awal
        self.code()


#memanggil tkinter
if __name__=='__main__':
    root = Tk()

    app = TebakAngka()

    mainloop()