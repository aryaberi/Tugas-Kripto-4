from tkinter import *
from tkinter import filedialog

import RSA
def RSA_Windows():
   def generate_key():
      hide_all_frame()
      generate_key_frame.pack(fill=BOTH, expand=1)
      label2 = Label(generate_key_frame, text = "Masukan nilai p").pack()
      entry2 = Entry(generate_key_frame,width=30)
      entry2.pack()

      label3 = Label(generate_key_frame, text = "Masukan nilai q").pack()
      a = Entry(generate_key_frame)
      a.pack()
      label4 = Label(generate_key_frame, text = "Masukan nilai e").pack()
      b = Entry(generate_key_frame)
      b.pack()
      button1 = Button(generate_key_frame, text="Generate Key", command=lambda : generateKey(entry2.get(),a.get(),b.get())).pack()

   def encrypht():
      hide_all_frame()
      Encrypht_frame.pack(fill=BOTH, expand=1)
      label = Label(Encrypht_frame, text = "Masukan Text").pack()
      entry = Entry(Encrypht_frame,width=30)
      entry.pack()
      openFile = Button(Encrypht_frame, text="Pilih File", command=pilihFile).pack()
      label5 = Label(Encrypht_frame, text = "Masukan kunci publick").pack
      label6 = Label(Encrypht_frame, text = "Masukan nilai e").pack()
      e1 = Entry(Encrypht_frame)
      e1.pack()
      label7 = Label(Encrypht_frame, text = "Masukan nilai n").pack()
      n1 = Entry(Encrypht_frame)
      n1.pack()
      button2 = Button(Encrypht_frame, text="Enckrip", command=lambda : Encrypht(entry.get(),e1.get(),n1.get())).pack()

   def decrypht():
      hide_all_frame()
      Decrypht_key_frame.pack(fill=BOTH, expand=1)
      label = Label(Decrypht_key_frame, text = "Masukan Text").pack()
      entry = Entry(Decrypht_key_frame,width=30)
      entry.pack()
      label8 = Label(Decrypht_key_frame, text = "Masukan kunci privat").pack()
      label9 = Label(Decrypht_key_frame, text = "Masukan nilai d").pack()
      e2 = Entry(Decrypht_key_frame)
      e2.pack()
      label10 = Label(Decrypht_key_frame, text = "Masukan nilai n").pack()
      n2 = Entry(Decrypht_key_frame)
      n2.pack()
      button3 = Button(Decrypht_key_frame, text="Decrip", command=lambda : Decrypht(entry.get(),e2.get(),n2.get())).pack()


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

   def generateKey(p,q,e):
      publick, privat = RSA.bangkitKunci(int(p),int(q),int(e))
      label3 = Label(generate_key_frame, text = "Key Public dan Privat nya")
      label3.pack()
      publick = Label(generate_key_frame, text = publick)
      publick.pack()
      privat =  Label(generate_key_frame, text = privat)
      privat.pack()

   def Encrypht(Text,e,n):
      publick = [int(e),int(n)]
      c = RSA.encriptRSA(Text,publick)
      Label2 = Label(Encrypht_frame, text = "Ini Chiper text nya:")
      Label2.pack()
      chiper = Label(Encrypht_frame, text= c)
      chiper.pack()

   def Decrypht(Text,d,n):
      privat = [int(d),int(n)]
      p = RSA.dekirpRSA(Text,privat)
      Label1 = Label(Decrypht_key_frame, text = "Ini Plain text nya:")
      Label1.pack()
      plain = Label(Decrypht_key_frame, text= p)
      plain.pack()


   root = Tk()
   menubar = Menu(root)
   filemenu = Menu(menubar, tearoff=0)
   filemenu.add_command(label="Generate Key", command=generate_key)
   filemenu.add_command(label="Encrypht", command=encrypht)
   filemenu.add_command(label="Decrypht", command=decrypht)
   menubar.add_cascade(label="RSA", menu=filemenu)

   generate_key_frame = Frame(root,width=400,height=400)
   Encrypht_frame = Frame(root,width=400,height=400)
   Decrypht_key_frame = Frame(root,width=400,height=400)

   root.config(menu=menubar)
   root.mainloop()