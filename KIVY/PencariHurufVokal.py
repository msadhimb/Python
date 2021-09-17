from kivy.lang import Builder
from kivymd.app import MDApp

class Hurufvokal(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file("csskivy.kv")

    def eek(self):
        huruf_vokal = ['a', 'i', 'u', 'e', 'o']
        id_text = ['satu', 'dua', 'tiga', 'empat', 'lima', 'enam']

        #membuat print untuk menunjukan jumlah karakter
        print(f'\nJUMLAH KARAKTER DARI "{self.root.ids.text.text}" ADALAH {len(self.root.ids.text.text)}')
        self.root.ids.text2.text = f'\nJUMLAH KARAKTER DARI "{self.root.ids.text.text}" ADALAH {len(self.root.ids.text.text)}'

        #menampilkan jumlah huruf vokal
        print(f'\nJUMLAH HURUF VOKAL DARI "{self.root.ids.text.text}" ADALAH {self.root.ids.text.text.count("a") + self.root.ids.text.text.count("i") + self.root.ids.text.text.count("u") + self.root.ids.text.text.count("e") + self.root.ids.text.text.count("o")} \n')
        self.root.ids.text3.text = f'\nJUMLAH HURUF VOKAL DARI "{self.root.ids.text.text}" ADALAH {self.root.ids.text.text.count("a") + self.root.ids.text.text.count("i") + self.root.ids.text.text.count("u") + self.root.ids.text.text.count("e") + self.root.ids.text.text.count("o")} \n'
        #membuat loop untuk mengeluarkan indeks huruf vokal
        for i in range(0,len(huruf_vokal)):
            for j in range(0, len(id_text)):
                #menampilkan detail huruf vokal
                print(huruf_vokal[i], 'sejumlah', self.root.ids.text.text.count(huruf_vokal[i]))
                self.root.ids.id_text[j].text = f'{huruf_vokal[i]} sejumlah {self.root.ids.text.text.count(huruf_vokal[i])}'

Hurufvokal().run()