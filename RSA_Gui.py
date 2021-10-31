from tkinter import *
from tkinter import filedialog
import RSA

def RSA_Windows():
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

    def generateKey(p,q,e):
        publick, privat = RSA.bangkitKunci(int(p),int(q),int(e))
        label3 = Label(main, text = "Key Public dan Privat nya")
        label3.pack()
        publick = Label(main, text = publick)
        publick.pack()
        privat =  Label(main, text = privat)
        privat.pack()

    def Encrypht(Text,e,n):
        publick = [int(e),int(n)]
        c = RSA.encriptRSA(Text,publick)
        Label2 = Label(main, text = "Ini Chiper text nya:")
        Label2.pack()
        chiper = Label(main, text= c)
        chiper.pack()

    def Decrypht(Text,d,n):
        privat = [int(d),int(n)]
        p = RSA.dekirpRSA(Text,privat)
        Label1 = Label(main, text = "Ini Plain text nya:")
        Label1.pack()
        plain = Label(main, text= p)
        plain.pack()


    Judul = Label(main,text="Algoritma RSA")
    label = Label(main, text = "Masukan Text")
    entry = Entry(main,width=30)

    openFile = Button(main, text="Pilih File", command=pilihFile)


    label2 = Label(main, text = "Masukan nilai p")
    entry2 = Entry(main,width=30)

    label3 = Label(main, text = "Masukan nilai q")
    a = Entry(main)
    label4 = Label(main, text = "Masukan nilai e")
    b = Entry(main)

    label5 = Label(main, text = "Masukan kunci publick")
    label6 = Label(main, text = "Masukan nilai e")
    e1 = Entry(main)
    label7 = Label(main, text = "Masukan nilai n")
    n1 = Entry(main)

    label8 = Label(main, text = "Masukan kunci privat")
    label9 = Label(main, text = "Masukan nilai d")
    e2 = Entry(main)
    label10 = Label(main, text = "Masukan nilai n")
    n2 = Entry(main)


    button1 = Button(main, text="Generate Key", command=lambda : generateKey(entry2.get(),a.get(),b.get()))
    button2 = Button(main, text="Enckrip", command=lambda : Encrypht(entry.get(),e1.get(),n1.get()))
    button3 = Button(main, text="Decrip", command=lambda : Decrypht(entry.get(),e2.get(),n2.get()))

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
    entry2.pack(ipady=5)
    entry2.place(x=10,y=120)
    label3.pack()
    label3.place(x=10,y=140)
    a.pack()
    a.place(x=10,y=160)
    label4.pack()
    label4.place(x=10,y=180)
    b.pack()
    b.place(x=10,y=200)
    button1.pack()
    button1.place(x=10,y=220)

    label5.pack()
    label5.place(x=10,y=260)
    label6.pack()
    label6.place(x=10,y=280)
    e1.pack()
    e1.place(x=10,y=300)
    label7.pack()
    label7.place(x=10,y=320)
    n1.pack()
    n1.place(x=10,y=340)
    button2.pack()
    button2.place(x=10,y=360)

    label8.pack()
    label8.place(x=10,y=400)
    label9.pack()
    label9.place(x=10,y=420)
    e2.pack()
    e2.place(x=10,y=440)
    label10.pack()
    label10.place(x=10,y=460)
    n2.pack()
    n2.place(x=10,y=480)
    button3.pack()
    button3.place(x=10,y=500)


    main.mainloop()