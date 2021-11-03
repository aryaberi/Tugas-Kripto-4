from tkinter import *
from tkinter import filedialog

import Pailler

def Pailler_Windows():
	def hideAllFrame():
		for widget in generateKeyFrame.winfo_children():
    		widget.destroy()
    	for widget in encryptionFrame.winfo_children():
        	widget.destroy()
    	for widget in decryptionFrame.winfo_children():
        	widget.destroy()
        generateKeyFrame.pack_forget()
    	encryptionFrame.pack_forget()
    	decryptionFrame.pack_forget()

	def pilihFile():
		global f_content
		root.filename = filedialog.askopenfilename(initialdir = "/c", title = "Pilih file")
		with open(root.filename,'r') as f:
			f_content = f.read()
		fileLabel = Label(root, text = root.filename)
		fileLabel.pack()

	def generateKeyCommand(p, q, g):
		publicKey, privateKey = Pailler.bangkitKunci(int(p), int(q), int(e))
		labelGenerate = Label(generateKeyFrame, text = "Key Public dan Private:")
		labelGenerate.pack()
		publicKey = Label(generateKeyFrame, text = publicKey)
		publicKey.pack()
		privateKey = Label(generateKeyFrame, text = privateKey)
		privateKey.pack()

    def generateKey():
    	hideAllFrame()
    	generateKeyFrame.pack(fill = BOTH, expand = 1)

    	# Label 2 = p
    	label2 = Label(generateKeyFrame, text = "Masukkan nilai p").pack()
    	entry2 = Entry(generateKeyFrame, width = 25)
    	entry2.pack()

    	# Label 3 = q
    	label3 = Label(generateKeyFrame, text = "Masukkan nilai q").pack()
    	entry3 = Entry(generateKeyFrame, width = 25)
    	entry3.pack()

		# Label 4 = g
    	label4 = Label(generateKeyFrame, text = "Masukkan nilai g").pack()
    	entry4 = Entry(generateKeyFrame, width = 25)
    	entry4.pack()

    	# Button 1 untuk generate key
		button1 = Button(generateKeyFrame, text = "Generate Key", command = lambda : generateKeyCommand(entry2.get(), entry3.get(), entry4.get())).pack()

	def encryptionCommand(text, n, g, r):
		publicKey = [int(n), int(g)]
		cipher = Pailler.encrypt(text, publicKey, r)
		labelCipher = Label(encryptionFrame, text = "Ciphertext: ")
		labelCipher.pack()
		ciphertext = Label(encryptionFrame, text = cipher)
		ciphertext.pack()

	def encryption():
		hideAllFrame()
		encryptionFrame.pack(fill = BOTH, expand = 1)

		# Label 1 = Text
		label1 = Label(encryptionFrame, text = "Masukkan text").pack()
		entry1 = Entry(encryptionFrame, width = 25)
		entry1.pack()
		openFileButton = Button(encryptionFrame, text = "Pilih file", command = pilihFile).pack()

		# Label 5 = public key n
		label5 = Label(encryptionFrame, text = "Masukkan nilai n").pack()
		entry5 = Entry(encryptionFrame, width = 25)
		entry5.pack()

		# Label 6 = public key g
		label6 = Label(encryptionFrame, text = "Masukkan nilai g").pack()
		entry6 = Entry(encryptionFrame, width = 25)
		entry6.pack()

		# Label 7 = r
		label7 = Label(encryptionFrame, text = "Masukkan nilai r").pack()
		entry7 = Entry(encryptionFrame, width = 25)
		entry7.pack()

		# Button 2 untuk enkripsi
		button2 = Button(encryptionFrame, text = "Encrypt", command = lambda : encryptionCommand(entry1.get(), entry5.get(), entry6.get(), entry7.get())).pack()

	def decryptionCommand(text, lamda, miu, n):
		privateKey = [int(lamda), int(miu)]
		plain = Pailler.decrypt(text, privateKey, n)
		labelDecipher = Label(decryptionFrame, text = "Plaintext: ")
		labelDecipher.pack()
		plaintext = Label(decryptionFrame, text = plain)
		plaintext.pack()

	def decryption():
		hideAllFrame()
		decryptionFrame.pack(fill = BOTH, expand = 1)

		# Label 1 = Text
		label1 = Label(decryptionFrame, text = "Masukkan text").pack()
		entry1 = Entry(decryptionFrame, width = 25)
		entry1.pack()
		openFileButton = Button(decryptionFrame, text = "Pilih file", command = pilihFile).pack()

		# Label 8 = private key lambda
		label8 = Label(decryptionFrame, text = "Masukkan nilai lambda").pack()
		entry8 = Entry(decryptionFrame, width = 25)
		entry8.pack()

		# Label 9 = private key miu
		label6 = Label(decryptionFrame, text = "Masukkan nilai miu").pack()
		entry6 = Entry(decryptionFrame, width = 25)
		entry6.pack()

		# Label 5 = public key n
		label5 = Label(decryptionFrame, text = "Masukkan nilai n").pack()
		entry5 = Entry(decryptionFrame, width = 25)
		entry5.pack()

		# Button 3 untuk dekripsi
		button3 = Button(decryptionFrame, text = "Decrypt", command = lambda : decryptionCommand(entry1.get(), entry8.get(), entry9.get(), entry5.get())).pack()

	root = Tk()
	menubar = Menu(root)
	filemenu = Menu(menubar, tearoff = 0)
	filemenu.add_command(label = "Generate Key", command = generateKey)
	filemenu.add_command(label = "Encrypt", command = encryption)
	filemenu.add_command(label = "Decrypt", command = decryption)
	menubar.add_cascade(label = "Paillier", menu = filemenu)

	generateKeyFrame = Frame(root,width = 400, height = 400)
	encryptionFrame = Frame(root,width = 400, height = 400)
	decryptionFrame = Frame(root,width = 400, height = 400)

	root.config(menu = menubar)
	root.mainloop()