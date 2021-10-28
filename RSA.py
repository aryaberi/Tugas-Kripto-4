def cekPrima(num):
    for i in range(2,num):
        if (num % i) == 0:
            i = num
            return False
            
    else:
        return True

def computeGCD(x, y):
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
              
    return gcd

def modInverse(a, m):
     
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1

def convert_alfabet(X):
    if(X == "A" or X == "a"):
        return "00"
    elif(X == "B" or X == "b"):
        return "01"
    elif(X == "C" or X == "c"):
        return "02"
    elif(X == "D" or X == "d"):
        return "03"
    elif(X == "E" or X == "e"):
        return "04"
    elif(X == "F" or X == "f"):
        return "05"
    elif(X == "G" or X == "g"):
        return "06"
    elif(X == "H" or X == "h"):
        return "07"
    elif(X == "I" or X == "i"):
        return "08"
    elif(X == "J" or X == "j"):
        return "09"
    elif(X == "K" or X == "k"):
        return "10"
    elif(X == "L" or X == "l"):
        return "11"
    elif(X == "M" or X == "m"):
        return "12"
    elif(X == "N" or X == "n"):
        return "13"
    elif(X == "O" or X == "o"):
        return "14"
    elif(X == "P" or X == "p"):
        return "15"
    elif(X == "Q" or X == "q"):
        return "16"
    elif(X == "R" or X == "r"):
        return "17"
    elif(X == "S" or X == "s"):
        return "18"
    elif(X == "T" or X == "t"):
        return "19"
    elif(X == "U" or X == "u"):
        return "20"
    elif(X == "V" or X == "v"):
        return "21"
    elif(X == "W" or X == "w"):
        return "22"
    elif(X == "X" or X == "x"):
        return "23"
    elif(X == "Y" or X == "y"):
        return "24"
    elif(X == "Z" or X == "z"):
        return "25"
    else:
        return None

def convert_Back(X):
    if(X == "00"):
        return "A"
    elif(X == "01"):
        return "B"
    elif(X == "02"):
        return "C"
    elif(X == "03"):
        return "D"
    elif(X == "04"):
        return "E"
    elif(X == "05"):
        return "F"
    elif(X == "06"):
        return "G"
    elif(X == "07"):
        return "H"
    elif(X == "08"):
        return "I"
    elif(X == "09"):
        return "J"
    elif(X == "10"):
        return "K"
    elif(X == "11"):
        return "L"
    elif(X == "12"):
        return "M"
    elif(X == "13"):
        return "N"
    elif(X == "14"):
        return "O"
    elif(X == "15"):
        return "P"
    elif(X == "16"):
        return "Q"
    elif(X == "17"):
        return "R"
    elif(X == "18"):
        return "S"
    elif(X == "19"):
        return "T"
    elif(X == "20"):
        return "U"
    elif(X == "21"):
        return "V"
    elif(X == "22"):
        return "W"
    elif(X == "23"):
        return "X"
    elif(X == "24"):
        return "Y"
    elif(X == "25"):
        return "Z"


def bangkitKunci(num1,num2,e):
    publik = []
    privat = []
    d = 0
    n = num1 * num2
    nfaiz = (num1-1) * (num2-1)
    if(computeGCD(e,nfaiz)==1):
        d = modInverse(e,nfaiz)
        if(d != -1):
            publik.append(e)
            publik.append(n)
            privat.append(d)
            privat.append(n)
            return publik, privat
        else:
            print("nilai d tidak ditemukan")
    else:
        print("nilai e tidak prima dengan nfaiz")

def encriptRSA(Text,Key):
    m = ""
    count = 0
    N = 0
    temp = []
    chiper = []
    for x in Text:
        if(convert_alfabet(x) != None):
            temp.append(convert_alfabet(x))
    if(len(str(Key[1]))%2 == 0):
        N = len(str(Key[1]))/2 
    else:
        N = len(str(Key[1]))/2 + 1
    for i in range(len(temp)):
        count += 1
        if(count < N):
            m += str(temp[i])
        elif(count == N):
            m += str(temp[i])
            chiper.append(m)
            count = 0
            m = ""
    temp.clear()
    for x in chiper:
        
        if(len(str(pow(int(x),Key[0])%Key[1])) < len(str(Key[1]))):
            temp.append('0'+str(pow(int(x),Key[0])%Key[1]))
        else:
            temp.append(str(pow(int(x),Key[0])%Key[1]))

    return temp      

def dekirpRSA (Chiper,Key):
    temp = []
    temp2 = []
    for x in Chiper:
        
        if(len(str(pow(int(x),Key[0])%Key[1])) < len(str(Key[1]))):
            temp.append('0'+str(pow(int(x),Key[0])%Key[1]))
        else:
            temp.append(str(pow(int(x),Key[0])%Key[1]))
    
    count = 0
    C = ''
    for x in temp:
        for i in range(len(x)):
            count += 1
            if(count < 2):
                C += x[i]
            elif(count == 2):
                C += x[i]
                temp2.append(C)
                count = 0
                C = ''
    temp.clear()
    for x in temp2:
        temp.append(convert_Back(x))
    return temp
    

num1 = int(input("masukan nilai P:"))
num2 = int(input("masukan nilai q:"))
e = int(input("masukan nilai e:"))
Text = input("masukan Text:")
publik, privat = bangkitKunci(num1,num2,e)
chiper = encriptRSA(Text,publik)
print("ini chiper text nya:",chiper)
decrip = dekirpRSA(chiper,privat)
print("ini plain text nya:", decrip)
