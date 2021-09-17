from tkinter import *

temp = [0]
akses = {
    'Muhamad Salman Adhim Baqy' : temp, 
    'Ilham Maulana Putra' : temp, 
    'Daffa Radhitya Pratama Wina Putra' : temp, 
    'Akbar Priyo Santosa' : temp, 
    'Muhammad Syaifur Rohman' : temp
}

class ATM():

    def __init__(self):
        self.mainframe()

    def mainframe(self):
        self.tulisan1 = Label(root, text="Selamat Datang \n Karena tidak ada kartu yang bisa dibaca maka \n Masukkan nama lengkap anda \n") #menampilkan tulisan di tkinter
        self.layar = Entry(root, width=50, borderwidth=5) #tempat menginputkan nama di tkinter

        self.layar.grid(column=3, row=1)
        self.tulisan1.grid(column=3, row=0) 
        #grid untuk mengatur posisi dan memunculkan Label dan Entry

        self.layar.insert(0, "Masukkan nama lengkap anda (ex. Salman Adhim)...")

        self.enter = Button(root, text='enter' , padx=40, pady=20, command=lambda: self.login(namaku=self.layar.get())) #menampilkan sebuah tombol dengan perintah jika diklik maka menjalankan fungsi login()
        self.enter.grid(column=3, row=4) #grid untuk mengatur posisi dan memunculkan Button

    def login(self,namaku):
        if namaku in akses:
            self.layar.grid_remove()
            self.enter.grid_remove()
            self.tulisan1.grid_remove()
            # menghapus grid

            self.tulisan1 = Label(root, text="Selamat Datang \n Selamat bertransaksi menggunakan ATM kami.")
            self.tulisan1.grid(column=3, row=0)

            self.secframe()

            self.button()
        
            print(f'\n Nama = {self.layar.get()}') 
        else:
            self.layar.grid_forget()
            self.tulisan2 = Label(root, text="Nama anda tidak terdaftar didatabase kami")
            self.tulisan2.grid(column=3, row=2)
            self.enter.grid_remove()

        self.namaku = namaku

    def secframe(self):
        # membuat label untuk petunjuk button mana yang akan dipilih
        self.opsi = Label(root, text="- 100.000")
        self.opsi.grid(column=1, row=1 )
        self.opsi2 = Label(root, text="- 200.000")
        self.opsi2.grid(column=1, row=2 )
        self.opsi3 = Label(root, text="- 300.000")
        self.opsi3.grid(column=1, row=3 )
        self.opsi4 = Label(root, text="- 500.000")
        self.opsi4.grid(column=1, row=4 )
        self.opsi5 = Label(root, text="Transfer -")
        self.opsi5.grid(column=4, row=1 )
        self.opsi6 = Label(root, text="Cek Saldo -")
        self.opsi6.grid(column=4, row=2 )
        self.opsi9 = Label(root, text="Setor Tunai -")
        self.opsi9.grid(column=4, row=3 )
        self.opsi7 = Label(root, text="Cancel -")
        self.opsi7.grid(column=4, row=4 )

    def button(self):
        # membuat button berjumlah 8 selayaknya yang ada di atm dunia nyata
        self.angka1 = Button(root, text=1, padx=40, pady=20, command=lambda: self.opsi1())
        self.angka2 = Button(root, text=2, padx=40, pady=20, command=lambda: self.opsi22())
        self.angka3 = Button(root, text=3, padx=40, pady=20, command=lambda: self.opsi33())
        self.angka4 = Button(root, text=4, padx=40, pady=20, command=lambda: self.opsi44())
        self.angka5 = Button(root, text=5, padx=40, pady=20, command=lambda: self.sebelumtransfer())
        self.angka6 = Button(root, text=6, padx=40, pady=20, command=lambda: self.ceksaldo())
        self.angka7 = Button(root, text=7, padx=40, pady=20, command=lambda: self.setor())
        self.angka8 = Button(root, text=8, padx=40, pady=20, command=lambda: self.exit())

        self.angka1.grid(column=0, row=1 )
        self.angka2.grid(column=0, row=2 )
        self.angka3.grid(column=0, row=3 )
        self.angka4.grid(column=0, row=4 )

        self.angka5.grid(column=5, row=1 )
        self.angka6.grid(column=5, row=2 )
        self.angka7.grid(column=5, row=3 )
        self.angka8.grid(column=5, row=4 )

    def back(self):
        self.yess.grid_remove()
        self.noo.grid_remove()
        self.tulisan2.grid_remove()
        self.yess.grid_remove()
        self.noo.grid_remove()
        self.secframe()
        self.button()

    def backfromtakemoney(self):
        self.satu1.grid_remove()
        self.satu2.grid_remove()
        self.satu3.grid_remove()
        self.satu4.grid_remove()
        self.satu5.grid_remove()
        self.satu6.grid_remove()
        self.satu7.grid_remove()
        self.satu8.grid_remove()
        self.angka9.grid_remove()

        self.button()
        self.secframe()
        self.opsi8.grid_forget()
        self.tulisan2.grid_remove()
        self.input3.grid_forget()
        self.tulisan2.grid_remove()
        self.tf.grid_remove()

    def exit(self):
        self.opsi.grid_remove()
        self.opsi2.grid_remove()
        self.opsi3.grid_remove()
        self.opsi4.grid_remove()
        self.opsi5.grid_remove()
        self.opsi6.grid_remove()
        self.opsi7.grid_remove()
        self.opsi9.grid_remove()           
        # menghapus grid pada secframe

        self.tulisan4 = Label(root, text="Apakah Anda ingin keluar ?")
        self.tulisan4.grid(column=3, row=1)

        self.angka1.grid_remove()
        self.angka2.grid_remove()
        self.angka3.grid_remove()
        self.angka4.grid_remove()
        self.angka5.grid_remove()
        self.angka6.grid_remove()
        self.angka7.grid_remove()
        self.angka8.grid_remove()

        self.satu1 = Button(root, text=1, padx=40, pady=20)
        self.satu2 = Button(root, text=2, padx=40, pady=20)
        self.satu3 = Button(root, text=3, padx=40, pady=20)
        self.satu4 = Button(root, text=4, padx=40, pady=20)
        self.satu5 = Button(root, text=5, padx=40, pady=20)
        self.satu6 = Button(root, text=6, padx=40, pady=20)
        self.satu7 = Button(root, text=7, padx=40, pady=20)
        self.satu8 = Button(root, text=8, padx=40, pady=20)

        self.satu1.grid(column=0, row=1 )
        self.satu3.grid(column=0, row=3 )
        self.satu4.grid(column=0, row=4 )
        self.satu5.grid(column=5, row=1 )
        self.satu7.grid(column=5, row=3 )
        self.satu8.grid(column=5, row=4 )
        self.yes = Button(root, text=2, padx=40, pady=20, command=lambda: self.exityes())
        self.no = Button(root, text=6, padx=40, pady=20, command=lambda: self.back())
        self.yess = Label(root, text="- Ya")
        self.noo = Label(root, text="Tidak -")

        self.yes.grid(column=0, row=2)
        self.no.grid(column=5, row=2)
        self.yess.grid(column=2, row=2)
        self.noo.grid(column=4, row=2)

        self.tulisan2.grid_remove()

    def exityes(self):
        self.satu1.grid_remove()
        self.satu2.grid_remove()
        self.satu3.grid_remove()
        self.satu4.grid_remove()
        self.satu5.grid_remove()
        self.satu6.grid_remove()
        self.satu7.grid_remove()
        self.satu8.grid_remove()
        self.yes.grid_remove()
        self.no.grid_remove()
        self.yess.grid_remove()
        self.noo.grid_remove()
        self.tulisan4.grid_remove()

        self.mainframe()
        self.angka9.grid_remove()

    def opsi1(self):
        for x in temp:
                if x > 100000:
                    x -= 100000
                    temp.append(x)
                    del(temp[0])
                    self.tulisan2 = Label(root, text=f"Silahkan ambil uang anda \nSisa saldo anda adalah {x}")
                    self.tulisan2.grid(column=3, row=2)
                    self.opsi.grid_remove()
                    self.opsi2.grid_remove()
                    self.opsi3.grid_remove()
                    self.opsi4.grid_remove()
                    self.opsi5.grid_remove()
                    self.opsi6.grid_remove()
                    self.opsi7.grid_remove()
                    self.opsi9.grid_remove()

                    self.angka1.grid_remove()
                    self.angka2.grid_remove()
                    self.angka3.grid_remove()
                    self.angka4.grid_remove()
                    self.angka5.grid_remove()
                    self.angka6.grid_remove()
                    self.angka7.grid_remove()

                    self.satu1 = Button(root, text=1, padx=40, pady=20)
                    self.satu2 = Button(root, text=2, padx=40, pady=20)
                    self.satu3 = Button(root, text=3, padx=40, pady=20)
                    self.satu4 = Button(root, text=4, padx=40, pady=20)
                    self.satu5 = Button(root, text=5, padx=40, pady=20)
                    self.satu6 = Button(root, text=6, padx=40, pady=20)
                    self.satu7 = Button(root, text=7, padx=40, pady=20)
                    self.satu8 = Button(root, text=8, padx=40, pady=20)

                    self.satu1.grid(column=0, row=1 )
                    self.satu2.grid(column=0, row=2 )
                    self.satu3.grid(column=0, row=3 )
                    self.satu4.grid(column=0, row=4 )
                    self.satu5.grid(column=5, row=1 )
                    self.satu6.grid(column=5, row=2 )
                    self.satu7.grid(column=5, row=3 )
                    self.satu8.grid(column=5, row=4 )

                    self.angka8.grid_remove()
                    self.angka9 = Button(root, text=8, padx=40, pady=20, command=lambda: self.backfromtakemoney())
                    self.angka9.grid(column=5, row=4 )

                    self.opsi8 =Label(root, text="Back -")
                    self.opsi8.grid(column=4, row=4)

                    print(f'\n {self.layar.get()} telah mengambil uang sejumlah {x}\n')
                else:
                    self.tulisan2 = Label(root, text="Saldo anda tidak mencukupi \n Silahkan melakukan setor tunai \n ATM kami mengharuskan untuk saldo atm minimal 50.000 untuk riba")
                    self.tulisan2.grid(column=3, row=2)
                    self.opsi.grid_remove()
                    self.opsi2.grid_remove()
                    self.opsi3.grid_remove()
                    self.opsi4.grid_remove()
                    self.opsi5.grid_remove()
                    self.opsi6.grid_remove()
                    self.opsi7.grid_remove()
                    self.opsi9.grid_remove()

                    self.angka1.grid_remove()
                    self.angka2.grid_remove()
                    self.angka3.grid_remove()
                    self.angka4.grid_remove()
                    self.angka5.grid_remove()
                    self.angka6.grid_remove()
                    self.angka7.grid_remove()

                    self.satu1 = Button(root, text=1, padx=40, pady=20)
                    self.satu2 = Button(root, text=2, padx=40, pady=20)
                    self.satu3 = Button(root, text=3, padx=40, pady=20)
                    self.satu4 = Button(root, text=4, padx=40, pady=20)
                    self.satu5 = Button(root, text=5, padx=40, pady=20)
                    self.satu6 = Button(root, text=6, padx=40, pady=20)
                    self.satu7 = Button(root, text=7, padx=40, pady=20)
                    self.satu8 = Button(root, text=8, padx=40, pady=20)

                    self.satu1.grid(column=0, row=1 )
                    self.satu2.grid(column=0, row=2 )
                    self.satu3.grid(column=0, row=3 )
                    self.satu4.grid(column=0, row=4 )
                    self.satu5.grid(column=5, row=1 )
                    self.satu6.grid(column=5, row=2 )
                    self.satu7.grid(column=5, row=3 )
                    self.satu8.grid(column=5, row=4 )

                    self.angka8.grid_remove()
                    self.angka9 = Button(root, text=8, padx=40, pady=20, command=lambda: self.backfromtakemoney())
                    self.angka9.grid(column=5, row=4 )

                    self.opsi8 =Label(root, text="Back -")
                    self.opsi8.grid(column=4, row=4)

    def opsi22(self):
        for x in temp:
                if x > 200000:
                    x -= 200000
                    temp.append(x)
                    del(temp[0])
                    self.tulisan2 = Label(root, text=f"Silahkan ambil uang anda \nSisa saldo anda adalah {x}")
                    self.tulisan2.grid(column=3, row=2)
                    self.opsi.grid_remove()
                    self.opsi2.grid_remove()
                    self.opsi3.grid_remove()
                    self.opsi4.grid_remove()
                    self.opsi5.grid_remove()
                    self.opsi6.grid_remove()
                    self.opsi7.grid_remove()
                    self.opsi9.grid_remove()

                    self.angka1.grid_remove()
                    self.angka2.grid_remove()
                    self.angka3.grid_remove()
                    self.angka4.grid_remove()
                    self.angka5.grid_remove()
                    self.angka6.grid_remove()
                    self.angka7.grid_remove()

                    self.satu1 = Button(root, text=1, padx=40, pady=20)
                    self.satu2 = Button(root, text=2, padx=40, pady=20)
                    self.satu3 = Button(root, text=3, padx=40, pady=20)
                    self.satu4 = Button(root, text=4, padx=40, pady=20)
                    self.satu5 = Button(root, text=5, padx=40, pady=20)
                    self.satu6 = Button(root, text=6, padx=40, pady=20)
                    self.satu7 = Button(root, text=7, padx=40, pady=20)
                    self.satu8 = Button(root, text=8, padx=40, pady=20)

                    self.satu1.grid(column=0, row=1 )
                    self.satu2.grid(column=0, row=2 )
                    self.satu3.grid(column=0, row=3 )
                    self.satu4.grid(column=0, row=4 )
                    self.satu5.grid(column=5, row=1 )
                    self.satu6.grid(column=5, row=2 )
                    self.satu7.grid(column=5, row=3 )
                    self.satu8.grid(column=5, row=4 )

                    self.angka8.grid_remove()
                    self.angka9 = Button(root, text=8, padx=40, pady=20, command=lambda: self.backfromtakemoney())
                    self.angka9.grid(column=5, row=4 )

                    self.opsi8 =Label(root, text="Back -")
                    self.opsi8.grid(column=4, row=4)

                    print(f'\n {self.layar.get()} telah mengambil uang sejumlah {x}\n')
                else:
                    self.tulisan2 = Label(root, text="Saldo anda tidak mencukupi \n Silahkan melakukan setor tunai \n ATM kami mengharuskan untuk saldo atm minimal 50.000 untuk riba")
                    self.tulisan2.grid(column=3, row=2)
                    self.opsi.grid_remove()
                    self.opsi2.grid_remove()
                    self.opsi3.grid_remove()
                    self.opsi4.grid_remove()
                    self.opsi5.grid_remove()
                    self.opsi6.grid_remove()
                    self.opsi7.grid_remove()
                    self.opsi9.grid_remove()

                    self.angka1.grid_remove()
                    self.angka2.grid_remove()
                    self.angka3.grid_remove()
                    self.angka4.grid_remove()
                    self.angka5.grid_remove()
                    self.angka6.grid_remove()
                    self.angka7.grid_remove()

                    self.satu1 = Button(root, text=1, padx=40, pady=20)
                    self.satu2 = Button(root, text=2, padx=40, pady=20)
                    self.satu3 = Button(root, text=3, padx=40, pady=20)
                    self.satu4 = Button(root, text=4, padx=40, pady=20)
                    self.satu5 = Button(root, text=5, padx=40, pady=20)
                    self.satu6 = Button(root, text=6, padx=40, pady=20)
                    self.satu7 = Button(root, text=7, padx=40, pady=20)
                    self.satu8 = Button(root, text=8, padx=40, pady=20)

                    self.satu1.grid(column=0, row=1 )
                    self.satu2.grid(column=0, row=2 )
                    self.satu3.grid(column=0, row=3 )
                    self.satu4.grid(column=0, row=4 )
                    self.satu5.grid(column=5, row=1 )
                    self.satu6.grid(column=5, row=2 )
                    self.satu7.grid(column=5, row=3 )
                    self.satu8.grid(column=5, row=4 )

                    self.angka8.grid_remove()
                    self.angka9 = Button(root, text=8, padx=40, pady=20, command=lambda: self.backfromtakemoney())
                    self.angka9.grid(column=5, row=4 )
                    
                    self.opsi8 =Label(root, text="Back -")
                    self.opsi8.grid(column=4, row=4)

    def opsi33(self):
        for x in temp:
                if x > 300000:
                    x -= 300000
                    temp.append(x)
                    del(temp[0])
                    self.tulisan2 = Label(root, text=f"Silahkan ambil uang anda \nSisa saldo anda adalah {x}")
                    self.tulisan2.grid(column=3, row=2)
                    self.opsi.grid_remove()
                    self.opsi2.grid_remove()
                    self.opsi3.grid_remove()
                    self.opsi4.grid_remove()
                    self.opsi5.grid_remove()
                    self.opsi6.grid_remove()
                    self.opsi7.grid_remove()
                    self.opsi9.grid_remove()

                    self.angka1.grid_remove()
                    self.angka2.grid_remove()
                    self.angka3.grid_remove()
                    self.angka4.grid_remove()
                    self.angka5.grid_remove()
                    self.angka6.grid_remove()
                    self.angka7.grid_remove()

                    self.satu1 = Button(root, text=1, padx=40, pady=20)
                    self.satu2 = Button(root, text=2, padx=40, pady=20)
                    self.satu3 = Button(root, text=3, padx=40, pady=20)
                    self.satu4 = Button(root, text=4, padx=40, pady=20)
                    self.satu5 = Button(root, text=5, padx=40, pady=20)
                    self.satu6 = Button(root, text=6, padx=40, pady=20)
                    self.satu7 = Button(root, text=7, padx=40, pady=20)
                    self.satu8 = Button(root, text=8, padx=40, pady=20)

                    self.satu1.grid(column=0, row=1 )
                    self.satu2.grid(column=0, row=2 )
                    self.satu3.grid(column=0, row=3 )
                    self.satu4.grid(column=0, row=4 )
                    self.satu5.grid(column=5, row=1 )
                    self.satu6.grid(column=5, row=2 )
                    self.satu7.grid(column=5, row=3 )
                    self.satu8.grid(column=5, row=4 )

                    self.angka8.grid_remove()
                    self.angka9 = Button(root, text=8, padx=40, pady=20, command=lambda: self.backfromtakemoney())
                    self.angka9.grid(column=5, row=4 )

                    self.opsi8 =Label(root, text="Back -")
                    self.opsi8.grid(column=4, row=4)

                    print(f'\n {self.layar.get()} telah mengambil uang sejumlah {x}\n')
                else:
                    self.tulisan2 = Label(root, text="Saldo anda tidak mencukupi \n Silahkan melakukan setor tunai \n ATM kami mengharuskan untuk saldo atm minimal 50.000 untuk riba")
                    self.tulisan2.grid(column=3, row=2)
                    self.opsi.grid_remove()
                    self.opsi2.grid_remove()
                    self.opsi3.grid_remove()
                    self.opsi4.grid_remove()
                    self.opsi5.grid_remove()
                    self.opsi6.grid_remove()
                    self.opsi7.grid_remove()
                    self.opsi9.grid_remove()

                    self.angka1.grid_remove()
                    self.angka2.grid_remove()
                    self.angka3.grid_remove()
                    self.angka4.grid_remove()
                    self.angka5.grid_remove()
                    self.angka6.grid_remove()
                    self.angka7.grid_remove()

                    self.satu1 = Button(root, text=1, padx=40, pady=20)
                    self.satu2 = Button(root, text=2, padx=40, pady=20)
                    self.satu3 = Button(root, text=3, padx=40, pady=20)
                    self.satu4 = Button(root, text=4, padx=40, pady=20)
                    self.satu5 = Button(root, text=5, padx=40, pady=20)
                    self.satu6 = Button(root, text=6, padx=40, pady=20)
                    self.satu7 = Button(root, text=7, padx=40, pady=20)
                    self.satu8 = Button(root, text=8, padx=40, pady=20)

                    self.satu1.grid(column=0, row=1 )
                    self.satu2.grid(column=0, row=2 )
                    self.satu3.grid(column=0, row=3 )
                    self.satu4.grid(column=0, row=4 )
                    self.satu5.grid(column=5, row=1 )
                    self.satu6.grid(column=5, row=2 )
                    self.satu7.grid(column=5, row=3 )
                    self.satu8.grid(column=5, row=4 )

                    self.angka8.grid_remove()
                    self.angka9 = Button(root, text=8, padx=40, pady=20, command=lambda: self.backfromtakemoney())
                    self.angka9.grid(column=5, row=4 )
                    
                    self.opsi8 =Label(root, text="Back -")
                    self.opsi8.grid(column=4, row=4)

    def opsi44(self):
        for x in temp:
                if x > 500000:
                    x -= 500000
                    temp.append(x)
                    del(temp[0])
                    self.tulisan2 = Label(root, text=f"Silahkan ambil uang anda \nSisa saldo anda adalah {x}\n")
                    self.tulisan2.grid(column=3, row=2)
                    self.opsi.grid_remove()
                    self.opsi2.grid_remove()
                    self.opsi3.grid_remove()
                    self.opsi4.grid_remove()
                    self.opsi5.grid_remove()
                    self.opsi6.grid_remove()
                    self.opsi7.grid_remove()
                    self.opsi9.grid_remove()

                    self.angka1.grid_remove()
                    self.angka2.grid_remove()
                    self.angka3.grid_remove()
                    self.angka4.grid_remove()
                    self.angka5.grid_remove()
                    self.angka6.grid_remove()
                    self.angka7.grid_remove()

                    self.satu1 = Button(root, text=1, padx=40, pady=20)
                    self.satu2 = Button(root, text=2, padx=40, pady=20)
                    self.satu3 = Button(root, text=3, padx=40, pady=20)
                    self.satu4 = Button(root, text=4, padx=40, pady=20)
                    self.satu5 = Button(root, text=5, padx=40, pady=20)
                    self.satu6 = Button(root, text=6, padx=40, pady=20)
                    self.satu7 = Button(root, text=7, padx=40, pady=20)
                    self.satu8 = Button(root, text=8, padx=40, pady=20)

                    self.satu1.grid(column=0, row=1 )
                    self.satu2.grid(column=0, row=2 )
                    self.satu3.grid(column=0, row=3 )
                    self.satu4.grid(column=0, row=4 )
                    self.satu5.grid(column=5, row=1 )
                    self.satu6.grid(column=5, row=2 )
                    self.satu7.grid(column=5, row=3 )
                    self.satu8.grid(column=5, row=4 )

                    self.angka8.grid_remove()
                    self.angka9 = Button(root, text=8, padx=40, pady=20, command=lambda: self.backfromtakemoney())
                    self.angka9.grid(column=5, row=4 )

                    self.opsi8 =Label(root, text="Back -")
                    self.opsi8.grid(column=4, row=4)

                    print(f'\n {self.layar.get()} telah mengambil uang sejumlah {x}\n')
                else:
                    self.tulisan2 = Label(root, text="Saldo anda tidak mencukupi \n Silahkan melakukan setor tunai \n ATM kami mengharuskan untuk saldo atm minimal 50.000 untuk riba")
                    self.tulisan2.grid(column=3, row=2)
                    self.opsi.grid_remove()
                    self.opsi2.grid_remove()
                    self.opsi3.grid_remove()
                    self.opsi4.grid_remove()
                    self.opsi5.grid_remove()
                    self.opsi6.grid_remove()
                    self.opsi7.grid_remove()
                    self.opsi9.grid_remove()

                    self.angka1.grid_remove()
                    self.angka2.grid_remove()
                    self.angka3.grid_remove()
                    self.angka4.grid_remove()
                    self.angka5.grid_remove()
                    self.angka6.grid_remove()
                    self.angka7.grid_remove()

                    self.satu1 = Button(root, text=1, padx=40, pady=20)
                    self.satu2 = Button(root, text=2, padx=40, pady=20)
                    self.satu3 = Button(root, text=3, padx=40, pady=20)
                    self.satu4 = Button(root, text=4, padx=40, pady=20)
                    self.satu5 = Button(root, text=5, padx=40, pady=20)
                    self.satu6 = Button(root, text=6, padx=40, pady=20)
                    self.satu7 = Button(root, text=7, padx=40, pady=20)
                    self.satu8 = Button(root, text=8, padx=40, pady=20)

                    self.satu1.grid(column=0, row=1 )
                    self.satu2.grid(column=0, row=2 )
                    self.satu3.grid(column=0, row=3 )
                    self.satu4.grid(column=0, row=4 )
                    self.satu5.grid(column=5, row=1 )
                    self.satu6.grid(column=5, row=2 )
                    self.satu7.grid(column=5, row=3 )
                    self.satu8.grid(column=5, row=4 )

                    self.angka8.grid_remove()
                    self.angka9 = Button(root, text=8, padx=40, pady=20, command=lambda: self.backfromtakemoney())
                    self.angka9.grid(column=5, row=4 )
                    
                    self.opsi8 =Label(root, text="Back -")
                    self.opsi8.grid(column=4, row=4)

    def sebelumtransfer(self):
        self.angka1.grid_remove()
        self.angka2.grid_remove()
        self.angka3.grid_remove()
        self.angka4.grid_remove()
        self.angka5.grid_remove()
        self.angka6.grid_remove()
        self.angka7.grid_remove()
        self.angka8.grid_remove()

        self.satu1 = Button(root, text=1, padx=40, pady=20)
        self.satu2 = Button(root, text=2, padx=40, pady=20)
        self.satu3 = Button(root, text=3, padx=40, pady=20)
        self.satu4 = Button(root, text=4, padx=40, pady=20)
        self.satu5 = Button(root, text=5, padx=40, pady=20)
        self.satu6 = Button(root, text=6, padx=40, pady=20)
        self.satu7 = Button(root, text=7, padx=40, pady=20)
        self.satu8 = Button(root, text=8, padx=40, pady=20)

        self.satu1.grid(column=0, row=1 )
        self.satu2.grid(column=0, row=2 )
        self.satu3.grid(column=0, row=3 )
        self.satu4.grid(column=0, row=4 )
        self.satu5.grid(column=5, row=1 )
        self.satu6.grid(column=5, row=2 )
        self.satu7.grid(column=5, row=3 )
        self.satu8.grid(column=5, row=4 )

        self.tf = Entry(root, width=70, borderwidth=5)
        self.enter1 = Button(root, text='enter' , padx=40, pady=20, command=lambda: self.transfer(namaygditf=self.tf.get()))

        self.enter1.grid(column=3, row=5)
        self.tf.grid(column=3, row=1)

        self.tf.insert(0, "Masukkan nama lengkap pengguna yang ingin anda transfer")

        self.opsi.grid_remove()
        self.opsi2.grid_remove()
        self.opsi3.grid_remove()
        self.opsi4.grid_remove()
        self.opsi5.grid_remove()
        self.opsi6.grid_remove()
        self.opsi7.grid_remove()
        self.opsi9.grid_remove()
        
    def transfer(self, namaygditf):
        if namaygditf in akses:
            self.enter1.grid_remove()
            self.input3 = Entry(root, width=50, borderwidth=5)
            self.enter2 = Button(root, text='enter' , padx=40, pady=20, command=lambda: self.nominal21(uangygditransfer=self.input3.get()))

            self.input3.grid(column=3, row=2)
            self.enter2.grid(column=3, row=5)

            self.input3.insert(0, "Masukkan nominal yang ingin anda transfer...")
        else:
            print("\n")
            print("\tNama pengguna tidak terdaftar di database kami.")

    def nominal21(self,uangygditransfer):
            for x in temp:
                if x > int(uangygditransfer):
                    x -= int(uangygditransfer)
                    temp.append(x)
                    del(temp[0])

                    self.enter2.grid_remove()

                    self.tulisan2 =Label(root, text=f"Sisa saldo anda saat ini adalah {x}")
                    self.tulisan2.grid(column=3, row=3)

                    self.angka8.grid_remove()
                    self.angka9 = Button(root, text=8, padx=40, pady=20, command=lambda: self.backfromtakemoney())
                    self.angka9.grid(column=5, row=4 )

                    self.opsi8 =Label(root, text="Back -")
                    self.opsi8.grid(column=4, row=4)
                    print(f'\n {self.layar.get()} mentransferkan uang kepada {self.tf.get()} sejumlah {int(uangygditransfer)}\n')
                else:
                    self.tulisan2 =Label(root, text="Saldo anda tidak mencukupi untuk melakukan transaksi \n Silahkan melakukan setor tunai \n ATM kami mengharuskan untuk saldo atm minimal 50.000 untuk riba.")
                    self.tulisan2.grid(column=3, row=3)

                    print("\n")
                    print("\tSaldo anda tidak mencukupi.")
                    print("===========================")
                    print("\tSilahkan melakukan setor tunai.")
                    print("\tATM kami mengharuskan untuk saldo atm minimal 50.000 untuk riba.")

                    self.enter2.grid_remove()
                    self.angka8.grid_remove()
                    self.angka9 = Button(root, text=8, padx=40, pady=20, command=lambda: self.backfromtakemoney())
                    self.angka9.grid(column=5, row=4 )

                    self.opsi8 =Label(root, text="Back -")
                    self.opsi8.grid(column=4, row=4)

    def ceksaldo(self):
        self.angka1.grid_remove()
        self.angka2.grid_remove()
        self.angka3.grid_remove()
        self.angka4.grid_remove()
        self.angka5.grid_remove()
        self.angka6.grid_remove()
        self.angka7.grid_remove()
        self.angka8.grid_remove()

        self.satu1 = Button(root, text=1, padx=40, pady=20)
        self.satu2 = Button(root, text=2, padx=40, pady=20)
        self.satu3 = Button(root, text=3, padx=40, pady=20)
        self.satu4 = Button(root, text=4, padx=40, pady=20)
        self.satu5 = Button(root, text=5, padx=40, pady=20)
        self.satu6 = Button(root, text=6, padx=40, pady=20)
        self.satu7 = Button(root, text=7, padx=40, pady=20)
        self.satu8 = Button(root, text=8, padx=40, pady=20)

        self.satu1.grid(column=0, row=1 )
        self.satu2.grid(column=0, row=2 )
        self.satu3.grid(column=0, row=3 )
        self.satu4.grid(column=0, row=4 )
        self.satu5.grid(column=5, row=1 )
        self.satu6.grid(column=5, row=2 )
        self.satu7.grid(column=5, row=3 )
        self.satu8.grid(column=5, row=4 )

        self.opsi.grid_remove()
        self.opsi2.grid_remove()
        self.opsi3.grid_remove()
        self.opsi4.grid_remove()
        self.opsi5.grid_remove()
        self.opsi6.grid_remove()
        self.opsi7.grid_remove()
        self.opsi9.grid_remove()

        for x in temp:
            self.tulisan2 =Label(root, text=f"Saldo anda saat ini adalah {x}")
            self.tulisan2.grid(column=3, row=2)
            print("\n")
            print(f'\n saldo {self.layar.get()} berjumlah {x}\n')

            self.opsi8 =Label(root, text="Back -")
            self.opsi8.grid(column=4, row=4)

            self.angka9 = Button(root, text='8', padx=40, pady=20, command=lambda: self.backfromtakemoney())
            self.angka9.grid(column=5, row=4 )


    def setor(self):
        self.angka1.grid_remove()
        self.angka2.grid_remove()
        self.angka3.grid_remove()
        self.angka4.grid_remove()
        self.angka5.grid_remove()
        self.angka6.grid_remove()
        self.angka7.grid_remove()
        self.angka8.grid_remove()

        self.satu1 = Button(root, text=1, padx=40, pady=20)
        self.satu2 = Button(root, text=2, padx=40, pady=20)
        self.satu3 = Button(root, text=3, padx=40, pady=20)
        self.satu4 = Button(root, text=4, padx=40, pady=20)
        self.satu5 = Button(root, text=5, padx=40, pady=20)
        self.satu6 = Button(root, text=6, padx=40, pady=20)
        self.satu7 = Button(root, text=7, padx=40, pady=20)
        self.satu8 = Button(root, text=8, padx=40, pady=20)

        self.satu1.grid(column=0, row=1 )
        self.satu2.grid(column=0, row=2 )
        self.satu3.grid(column=0, row=3 )
        self.satu4.grid(column=0, row=4 )
        self.satu5.grid(column=5, row=1 )
        self.satu6.grid(column=5, row=2 )
        self.satu7.grid(column=5, row=3 )
        self.satu8.grid(column=5, row=4 )

        self.opsi.grid_remove()
        self.opsi2.grid_remove()
        self.opsi3.grid_remove()
        self.opsi4.grid_remove()
        self.opsi5.grid_remove()
        self.opsi6.grid_remove()
        self.opsi7.grid_remove()
        self.opsi9.grid_remove()

        self.input4 = Entry(root, width=50, borderwidth=5)
        self.input4.grid(column=3, row=1)

        self.angka9 = Button(root, text='Setor', padx=40, pady=20, command=lambda: self.setor2(saldo=self.input4.get()))
        self.angka9.grid(column=3, row=3 )

    def setor2(self,saldo):
        self.input4.grid_remove()
        self.angka9.grid_remove()
        for i in temp:
            i += int(saldo)
            temp.append(i)
            del(temp[0])

            print(f'\n {self.layar.get()} telah menyetorkan uang sejumlah {i}\n')
            self.tulisan2 =Label(root, text=f"Jumlah saldo anda saat ini adalah {i}")
            self.tulisan2.grid(column=3, row=2)

            self.opsi8 =Label(root, text="Back -")
            self.opsi8.grid(column=4, row=4)

            self.angka9 = Button(root, text='8', padx=40, pady=20, command=lambda: self.backfromtakemoney())
            self.angka9.grid(column=5, row=4 )

if __name__ == '__main__':
    root = Tk()

    app = ATM()

    root.mainloop()
