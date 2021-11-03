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




def bangkitKunci(num1,num2,e):
    publik = []
    privat = []
    d = 0
    n = num1 * num2
    nfaiz = (num1-1) * (num2-1)
    if(computeGCD(e,nfaiz)==1):
        d = ModulUmum.modInverse(e,nfaiz)
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
    print(temp)
    N = len(str(Key[1]))/2 
    for i in range(len(temp)):
        count += 1
        if(count == N or i == len(temp)-1):
            m += str(temp[i])
            chiper.append(m)
            count = 0
            m = ""
        elif(count < N):
            m += str(temp[i])
       
    temp.clear()
    print(chiper)
    for x in chiper:
        
        if(len(str(pow(int(x),Key[0])%Key[1])) < len(str(Key[1]))):
            print(str(pow(int(x),Key[0])%Key[1]))
            temp.append('0'+str(pow(int(x),Key[0])%Key[1]))
        else:
            temp.append(str(pow(int(x),Key[0])%Key[1]))
            print(str(pow(int(x),Key[0])%Key[1]))
    return temp      

def dekirpRSA (Chiper,Key):
    temp = []
    temp2 = []
    temp3 = []
    temp4=[]
    N = len(str(Key[1]))
    count = 0
    C = ''
    for x in Chiper:
        count += 1
        if(count < N):
            C += x        
        elif(count == N):
            C += x
            temp3.append(C)
            count = 0
            C = ''

    for x in temp3:
        print(x)
        temp.clear()
        while(len(temp) < len(str(Key[1])) ):
            if(len(temp) == len(str(Key[1]))-len(str(pow(int(x),Key[0])%Key[1]))):
                for o in str(pow(int(x),Key[0])%Key[1]):
                    temp.append(o)
            else:
                temp.append('0')
            
        print(temp)
        arr = ModulUmum.copy_array(temp)
        temp4.append(arr)      
        
    count = 0
    C = ''
    print(temp4)
    for x in temp4:
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
    
