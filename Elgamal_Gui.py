from tkinter import *
from tkinter import filedialog
import Elgamal

def Elgamal_windows():
    main = Tk()
    main.geometry('500x450+10+200')
    label3 = Label(main)
    
    def pilihFile():
        global f_content
        main.filename = filedialog.askopenfilename(initialdir="/c",title="Pilih file")
        with open(main.filename,'r') as f:
            f_content = f.read()
        fileLabel=Label(main,text=main.filename)
        fileLabel.pack()

    def generateKey(p,g,x):
        publick, privat = Elgamal.bangkitKunci(int(p),int(g),int(x))
        label3 = Label(main, text = "Key Public dan Privat nya")
        label3.pack()
        publick = Label(main, text = publick)
        publick.pack()
        privat =  Label(main, text = privat)
        privat.pack()

    def Encrypht(teks,k,y,g,p):
        publick = [int(y),int(g),int(p)]
        c = Elgamal.enkripsi(teks,int(k),publick)
        Label2 = Label(main, text = "Ini Chiper text nya:")
        Label2.pack()
        chiper = Label(main, text= c)
        chiper.pack()

    def Decrypht(Text,x,p):
        privat = [int(x),int(p)]
        temp = []
        count = 0
        c = ''
        print(len(p))
        for x in Text:
           count += 1
           if(count < len(p)):
             c += x        
           elif(count == len(p)):
             c += x
             temp.append(int(c))
             count = 0
             c = ''

        p = Elgamal.decripsi(temp,privat)
        Label1 = Label(main, text = "Ini Plain text nya:")
        Label1.pack()
        plain = Label(main, text= p)
        plain.pack()


    Judul = Label(main,text="Algoritma Elgamal")
    label = Label(main, text = "Masukan Text")
    entry = Entry(main,width=30)

    openFile = Button(main, text="Pilih File", command=pilihFile)


    label2 = Label(main, text = "Masukan nilai p")
    p = Entry(main,width=30)

    label3 = Label(main, text = "Masukan nilai g")
    g = Entry(main)
    label4 = Label(main, text = "Masukan nilai x")
    x = Entry(main)


    label5 = Label(main, text = "Masukan kunci publick")
    label6 = Label(main, text = "Masukan nilai k")
    k1 = Entry(main)
    label7 = Label(main, text = "Masukan nilai y")
    y1 = Entry(main)
    label8 = Label(main, text = "Masukan nilai g")
    g1 = Entry(main)
    label9 = Label(main, text = "Masukan nilai p")
    p1 = Entry(main)


    label10 = Label(main, text = "Masukan kunci privat")
    label11 = Label(main, text = "Masukan nilai x")
    x2 = Entry(main)
    label12 = Label(main, text = "Masukan nilai p")
    p2 = Entry(main)


    button1 = Button(main, text="Generate Key", command=lambda : generateKey(p.get(),g.get(),x.get()))
    button2 = Button(main, text="Enckrip", command=lambda : Encrypht(entry.get(),k1.get(),y1.get(),g1.get(),p1.get()))
    button3 = Button(main, text="Decrip", command=lambda : Decrypht(entry.get(),x2.get(),p2.get()))

    Judul.pack
    Judul.place(x=10,y=10)
    label.pack()
    label.place(x=10,y=40)
    entry.pack(ipady=5)
    entry.place(x=10,y=60)
    openFile.pack()
    openFile.place(x=10,y=80)
    label2.pack()
    label2.place(x=10,y=100)
    p.pack(ipady=5)
    p.place(x=10,y=120)
    label3.pack()
    label3.place(x=10,y=140)
    g.pack()
    g.place(x=10,y=160)
    label4.pack()
    label4.place(x=10,y=180)
    x.pack()
    x.place(x=10,y=200)
    button1.pack()
    button1.place(x=10,y=220)

    label5.pack()
    label5.place(x=10,y=260)
    label6.pack()
    label6.place(x=10,y=280)
    k1.pack()
    k1.place(x=10,y=300)
    label7.pack()
    label7.place(x=10,y=320)
    y1.pack()
    y1.place(x=10,y=340)
    label8.pack()
    label8.place(x=10,y=360)
    g1.pack()
    g1.place(x=10,y=380)
    label9.pack()
    label9.place(x=10,y=400)
    p1.pack()
    p1.place(x=10,y=420)
    button2.pack()
    button2.place(x=10,y=440)

    label10.pack()
    label10.place(x=10,y=480)
    label11.pack()
    label11.place(x=10,y=500)
    x2.pack()
    x2.place(x=10,y=520)
    label12.pack()
    label12.place(x=10,y=540)
    p2.pack()
    p2.place(x=10,y=560)
    button3.pack()
    button3.place(x=10,y=580)


    main.mainloop()