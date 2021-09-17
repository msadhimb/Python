from tkinter import*

class GBK:

    def __init__(self):
        self.first()

    def first(self):
        self.gunbatker = ['gunting' , 'batu', 'kertas']

        self.label1 = Label(root, text='Selamat Datang digame Gunting Batu Kertas \n Game ini hanya bisa dimainkan oleh 2 orang \n silahkan klik tombol Mulai untuk memulai permainan \n')
        self.label1.grid(column=0, row=0, columnspan=3)

        self.button1 = Button(root, text='Mulai', padx=40, pady=20, command=lambda: self.second())
        self.button1.grid(column=1, row=1 )

    def second(self):
        self.button1.grid_forget()

        self.entry1 =Entry(root, width=35, borderwidth=5)
        self.entry1.grid(column=1, row=2)
        self.entry1.insert(0, 'Masukkan Nickname Player 1')

        self.button2 = Button(root, text='Enter', padx=20, pady=10, command=lambda: self.nickname())
        self.button2.grid(column=1, row=3)

    def nickname(self):
        self.entry1.grid_forget()
        self.button2.grid_forget()

        self.nickname1 = self.entry1.get()

        self.label2 = Label(root, text='Nickname untuk player 1 telah ditetapkan.')
        self.label2.grid(column=1, row=1)

        self.entry2 =Entry(root, width=35, borderwidth=5)
        self.entry2.grid(column=1, row=2)
        self.entry2.insert(0, 'Masukkan Nickname Player 2')

        self.button2 = Button(root, text='Enter', padx=20, pady=10, command=lambda: self.third())
        self.button2.grid(column=1, row=3)

    def third(self):
        global database

        self.label2.grid_forget()
        self.entry2.grid_forget()
        self.button2.grid_forget()
        
        self.nickname2 = self.entry2.get()

        database = ['gunting', 'batu', 'kertas']

        self.button3 = Button(root, text='Gunting', padx=20, pady=10, command=lambda: self.gunting())
        self.button3.grid(column=0, row=2)

        self.button4 = Button(root, text='Batu', padx=20, pady=10, command=lambda: self.batu())
        self.button4.grid(column=1, row=2)

        self.button5 = Button(root, text='Kertas', padx=20, pady=10, command=lambda: self.kertas())
        self.button5.grid(column=2, row=2)

    def gunting(self):
        global data
        data = 'gunting'

        self.canvas1 = Canvas(root, width=165, height=200)
        self.image1 = PhotoImage(file='C:\\Users\\adhim\\Downloads\\gunting.png')
        self.canvas1.create_image(0,0, anchor = NW, image=self.image1)

        self.button3.grid_forget()
        self.button4.grid_forget()
        self.button5.grid_forget()

        self.button3 = Button(root, text='Gunting', padx=20, pady=10, command=lambda: self.guntingclone())
        self.button3.grid(column=0, row=2)

        self.button4 = Button(root, text='Batu', padx=20, pady=10, command=lambda: self.batuclone())
        self.button4.grid(column=1, row=2)

        self.button5 = Button(root, text='Kertas', padx=20, pady=10, command=lambda: self.kertasclone())
        self.button5.grid(column=2, row=2)

        self.label4 = Label(root, text='Player 1 telah memilih')
        self.label4.grid(column=1, row=1)

    def batu(self):
        global data
        data = 'batu'

        self.canvas1 = Canvas(root, width=165, height=200)
        self.image1 = PhotoImage(file='C:\\Users\\adhim\\Downloads\\batu.png')
        self.canvas1.create_image(0,0, anchor = NW, image=self.image1)

        self.button3.grid_forget()
        self.button4.grid_forget()
        self.button5.grid_forget()

        self.button3 = Button(root, text='Gunting', padx=20, pady=10, command=lambda: self.guntingclone())
        self.button3.grid(column=0, row=2)

        self.button4 = Button(root, text='Batu', padx=20, pady=10, command=lambda: self.batuclone())
        self.button4.grid(column=1, row=2)

        self.button5 = Button(root, text='Kertas', padx=20, pady=10, command=lambda: self.kertasclone())
        self.button5.grid(column=2, row=2)

        self.label4 = Label(root, text='Player 1 telah memilih')
        self.label4.grid(column=1, row=1)

    def kertas(self):
        global data
        data = 'kertas'

        self.canvas1 = Canvas(root, width=165, height=200)
        self.image1 = PhotoImage(file='C:\\Users\\adhim\\Downloads\\kertas.png')
        self.canvas1.create_image(0,0, anchor = NW, image=self.image1)

        self.button3.grid_forget()
        self.button4.grid_forget()
        self.button5.grid_forget()

        self.button3 = Button(root, text='Gunting', padx=20, pady=10, command=lambda: self.guntingclone())
        self.button3.grid(column=0, row=2)

        self.button4 = Button(root, text='Batu', padx=20, pady=10, command=lambda: self.batuclone())
        self.button4.grid(column=1, row=2)

        self.button5 = Button(root, text='Kertas', padx=20, pady=10, command=lambda: self.kertasclone())
        self.button5.grid(column=2, row=2)

        self.label4 = Label(root, text='Player 1 telah memilih')
        self.label4.grid(column=1, row=1)

    def guntingclone(self):
        dataclone = 'gunting'

        self.label4.grid_forget()
        self.canvas1.grid(column=0, row=3)   

        self.button3.grid_forget()
        self.button4.grid_forget()
        self.button5.grid_forget()

        self.canvas2 = Canvas(root, width=165, height=200)
        self.canvas2.grid(column=2, row=3)   
        self.image2 = PhotoImage(file='C:\\Users\\adhim\\Downloads\\gunting.png')
        self.canvas2.create_image(0,0, anchor = NW, image=self.image2)

        self.canvas3 = Canvas(root, width=165, height=200)
        self.canvas3.grid(column=1, row=3)   
        self.image3 = PhotoImage(file='C:\\Users\\adhim\\Downloads\\versus.png')
        self.canvas3.create_image(0,0, anchor = NW, image=self.image3)

        if data == database[0] and dataclone == database[0]:
            self.label3 = Label(root, text='Seri')
            self.label3.grid(column=1, row=4)
        elif data == database[1] and dataclone == database[0]:
            self.label3 = Label(root, text=f'{self.nickname1} menang')
            self.label3.grid(column=1, row=4)
        elif data == database[2] and dataclone == database[0]:
            self.label3 = Label(root, text=f'{self.nickname2} menang')
            self.label3.grid(column=1, row=4)
        
        self.button6 = Button(root, text='Mulai lagi', padx=20, pady=10, command=lambda: self.startover())
        self.button6.grid(column=1, row=5)

    def batuclone(self):
        dataclone1 = 'batu'

        self.label4.grid_forget()
        self.canvas1.grid(column=0, row=3)   

        self.button3.grid_forget()
        self.button4.grid_forget()
        self.button5.grid_forget()

        self.canvas2 = Canvas(root, width=165, height=200)
        self.canvas2.grid(column=2, row=3)   
        self.image2 = PhotoImage(file='C:\\Users\\adhim\\Downloads\\batu.png')
        self.canvas2.create_image(0,0, anchor = NW, image=self.image2)

        self.canvas3 = Canvas(root, width=165, height=200)
        self.canvas3.grid(column=1, row=3)   
        self.image3 = PhotoImage(file='C:\\Users\\adhim\\Downloads\\versus.png')
        self.canvas3.create_image(0,0, anchor = NW, image=self.image3)

        if data == database[0] and dataclone1 == database[1]:
            self.label3 = Label(root, text=f'{self.nickname2} menang')
            self.label3.grid(column=1, row=4)
        elif data == database[1] and dataclone1 == database[1]:
            self.label3 = Label(root, text='Seri')
            self.label3.grid(column=1, row=4)
        elif data == database[2] and dataclone1 == database[1]:
            self.label3 = Label(root, text=f'{self.nickname1} menang')
            self.label3.grid(column=1, row=4)

        self.button6 = Button(root, text='Mulai lagi', padx=20, pady=10, command=lambda: self.startover())
        self.button6.grid(column=1, row=5)

    def kertasclone(self):
        dataclone2 = 'kertas'

        self.label4.grid_forget()
        self.canvas1.grid(column=0, row=3)   

        self.button3.grid_forget()
        self.button4.grid_forget()
        self.button5.grid_forget()

        self.canvas2 = Canvas(root, width=165, height=200)
        self.canvas2.grid(column=2, row=3)   
        self.image2 = PhotoImage(file='C:\\Users\\adhim\\Downloads\\kertas.png')
        self.canvas2.create_image(0,0, anchor = NW, image=self.image2)

        self.canvas3 = Canvas(root, width=165, height=200)
        self.canvas3.grid(column=1, row=3)   
        self.image3 = PhotoImage(file='C:\\Users\\adhim\\Downloads\\versus.png')
        self.canvas3.create_image(0,0, anchor = NW, image=self.image3)

        if data == database[0] and dataclone2 == database[2]:
            self.label3 = Label(root, text=f'{self.nickname1} menang')
            self.label3.grid(column=1, row=4)
        elif data == database[1] and dataclone2 == database[2]:
            self.label3 = Label(root, text=f'{self.nickname2} menang')
            self.label3.grid(column=1, row=4)
        elif data == database[2] and dataclone2 == database[2]:
            self.label3 = Label(root, text='Seri')
            self.label3.grid(column=1, row=4)
        
        self.button6 = Button(root, text='Mulai lagi', padx=20, pady=10, command=lambda: self.startover())
        self.button6.grid(column=1, row=5)

    def startover(self):
        self.canvas1.grid_forget()
        self.canvas2.grid_forget()
        self.canvas3.grid_forget()
        self.label3.grid_forget()
        self.button6.grid_forget()
        self.first()

if __name__=='__main__':
    root = Tk()

    app = GBK()

    mainloop()