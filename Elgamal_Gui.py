from tkinter import *
from tkinter import filedialog

import Elgamal
def Elgamal_windows():
   def generate_key():
      hide_all_frame()
      generate_key_frame.pack(fill=BOTH, expand=1)
      label2 = Label(generate_key_frame, text = "Masukan nilai p").pack()
      p = Entry(generate_key_frame,width=30)
      p.pack()

      label3 = Label(generate_key_frame, text = "Masukan nilai g").pack()
      g = Entry(generate_key_frame)
      g.pack()
      label4 = Label(generate_key_frame, text = "Masukan nilai x").pack()
      x = Entry(generate_key_frame)
      x.pack()
      button1 = Button(generate_key_frame, text="Generate Key", command=lambda : generateKey(p.get(),g.get(),x.get())).pack()
   
   def encrypht():
      hide_all_frame()
      Encrypht_frame.pack(fill=BOTH, expand=1)
      label = Label(Encrypht_frame, text = "Masukan Text").pack()
      entry = Entry(Encrypht_frame,width=30)
      entry.pack()
      label5 = Label(Encrypht_frame, text = "Masukan kunci publick").pack()
      label6 = Label(Encrypht_frame, text = "Masukan nilai k").pack()
      k1 = Entry(Encrypht_frame)
      k1.pack()
      label7 = Label(Encrypht_frame, text = "Masukan nilai y").pack()
      y1 = Entry(Encrypht_frame)
      y1.pack()
      label8 = Label(Encrypht_frame, text = "Masukan nilai g").pack()
      g1 = Entry(Encrypht_frame)
      g1.pack()
      label9 = Label(Encrypht_frame, text = "Masukan nilai p").pack()
      p1 = Entry(Encrypht_frame)
      p1.pack()
      button2 = Button(Encrypht_frame, text="Enckrip", command=lambda : Encrypht(entry.get(),k1.get(),y1.get(),g1.get(),p1.get())).pack()
   
   def decrypht():
      hide_all_frame()
      Decrypht_key_frame.pack(fill=BOTH, expand=1)
      label = Label(Decrypht_key_frame, text = "Masukan Text").pack()
      entry = Entry(Decrypht_key_frame,width=30)
      entry.pack()
      label10 = Label(Decrypht_key_frame, text = "Masukan kunci privat").pack()
      label11 = Label(Decrypht_key_frame, text = "Masukan nilai x").pack()
      x2 = Entry(Decrypht_key_frame)
      x2.pack()
      label12 = Label(Decrypht_key_frame, text = "Masukan nilai p").pack()
      p2 = Entry(Decrypht_key_frame)
      p2.pack()
      button3 = Button(Decrypht_key_frame, text="Decrip", command=lambda : Decrypht(entry.get(),x2.get(),p2.get())).pack()

   def hide_all_frame():
      for widget in generate_key_frame.winfo_children():
         widget.destroy()
      for widget in Encrypht_frame.winfo_children():
         widget.destroy()
      for widget in Decrypht_key_frame.winfo_children():
         widget.destroy()
      
      generate_key_frame.pack_forget()
      Encrypht_frame.pack_forget()
      Decrypht_key_frame.pack_forget()   
      
   def pilihFile():
        global f_content
        root.filename = filedialog.askopenfilename(initialdir="/c",title="Pilih file")
        with open(root.filename,'r') as f:
            f_content = f.read()
        fileLabel=Label(root,text=root.filename)
        fileLabel.pack()

   def generateKey(p,g,x):
        publick, privat = Elgamal.bangkitKunci(int(p),int(g),int(x))
        label3 = Label(generate_key_frame, text = "Key Public dan Privat nya")
        label3.pack()
        publick = Label(generate_key_frame, text = publick)
        publick.pack()
        privat =  Label(generate_key_frame, text = privat)
        privat.pack()

   def Encrypht(teks,k,y,g,p):
        publick = [int(y),int(g),int(p)]
        count = 0
        C = ""
        N = len(p)/2
        print(N)
        temp = []
        for i in range(len(teks)):
           count += 1
           if(i == len(teks)-1 or count == N):
              C+= teks[i]
              c = Elgamal.enkripsi(C,int(k),publick)
              temp.append(c)
              count =0
              C = ""
           elif(count < N):
              C+= teks[i]
        Label2 = Label(Encrypht_frame, text = "Ini Chiper text nya:")
        Label2.pack()
        chiper = Label(Encrypht_frame, text= temp)
        chiper.pack()
   def Decrypht(Text,x,p):
      privat = [int(x),int(p)]
      count = 0
      C = ""
      N = len(Text)-1
      temp=[]
      temp2 = []
      temp3 = []
      for i in range(len(Text)):
         count += 1
         if(i == N or count == len(p) and Text[i] != "*"):
            C += Text[i]
            temp.append(int(C))
            C =""
            count = 0
         elif(Text[i] == "*"):
            temp.append(int(C))
            C =""
            count = 0
         elif(count < len(p)):
            C += Text[i]

      print(temp)
      Z = len(temp)-1
      for x in temp:
         count += 1
         if(i == Z or count == 2 ):
            temp3.append(x)
            print("ini temp3 nya",temp3)
            p = Elgamal.decripsi(temp3,privat)
            temp2.append(p)
            temp3.clear()
            count = 0
         elif(count < 2):
            temp3.append(x)
            print("temp3",temp3)

      
      Label1 = Label(Decrypht_key_frame, text = "Ini Plain text nya:")
      Label1.pack()
      plain = Label(Decrypht_key_frame, text= temp2)
      plain.pack()




   root = Tk()
   menubar = Menu(root)
   filemenu = Menu(menubar, tearoff=0)
   filemenu.add_command(label="Generate Key", command=generate_key)
   filemenu.add_command(label="Encrypht", command=encrypht)
   filemenu.add_command(label="Decrypht", command=decrypht)
   menubar.add_cascade(label="Elgamal", menu=filemenu)

   generate_key_frame = Frame(root,width=400,height=400)
   Encrypht_frame = Frame(root,width=400,height=400)
   Decrypht_key_frame = Frame(root,width=400,height=400)

   root.config(menu=menubar)
   root.mainloop()

 