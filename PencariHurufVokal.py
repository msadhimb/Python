def pencarihurufvokal(text):
    huruf_vokal = ['a', 'i', 'u', 'e', 'o']

    #membuat print untuk menunjukan jumlah karakter
    print(f'\nJUMLAH KARAKTER DARI "{text}" ADALAH {len(text)}')

    #menampilkan jumlah huruf vokal
    print(f'\nJUMLAH HURUF VOKAL DARI "{text}" ADALAH {text.count("a") + text.count("i") + text.count("u") + text.count("e") + text.count("o")} \n')
    
    #membuat loop untuk mengeluarkan indeks huruf vokal
    for i in range(0,len(huruf_vokal)):

        #menampilkan detail huruf vokal
        print(huruf_vokal[i], 'sejumlah', text.count(huruf_vokal[i]))




#membuat input teks dan membuat input teks menjadi huruf
print('\n')
pencarihurufvokal(input('Masukkan Kalimat : ').lower())
print('\n')