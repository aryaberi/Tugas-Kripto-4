import ModulUmum

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
        if(ModulUmum.convert_alfabet(x) != None):
            temp.append(ModulUmum.convert_alfabet(x))
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
        temp.append(ModulUmum.convert_Back(x))
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
