import ModulUmum


def bangkitKunci(p,g,x):
    y = pow(g,x)%p
    publick = [y,g,p]
    privat = [x,p]
    return publick,privat



def enkripsi(teks,k,publick):
    m = ''
    for x in teks:
        m += ModulUmum.convert_alfabet(x)
    print(m) 
    a = pow(publick[1],k)%publick[2]
    b = pow(publick[0],k)*int(m)%publick[2]
    chiper = [a,b]
    return chiper

def decripsi(chiper,privat):
    plain = ''
    temp = []
    char = '' 
    Counter = 0
    print(chiper)
    print(privat)
    a = pow(chiper[0],privat[1]-1-privat[0])%privat[1]
    m = (chiper[1]*a)%privat[1]
    m = str(m)
    if len(m) %2 !=0:
        temp.append('0')
    for x in m:
        temp.append(x)

    for i in range(len(temp)):
        Counter += 1
        if(Counter < 2):
            char += temp[i]
        elif(Counter == 2):
             char += temp[i]
             Counter = 0
             print(char)
             plain += ModulUmum.convert_Back(char)
             char = ''
        
    return plain



# p = int(input("Masukan nilai p:"))
# g = int(input("Masukan nilai g:"))
# x = int(input("Masukan nilai x:"))
# k = int(input("Masukan nilai k:"))
# teks = input("Masukan nilai teks:")
# publick,privat = bangkitKunci(p,g,x)
# print(publick)
# print(privat)
# chiper = enkripsi(teks,k,publick)
# print(chiper)
# plain = decripsi(chiper,privat)
# print(plain)