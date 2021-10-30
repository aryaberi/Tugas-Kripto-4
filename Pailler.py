import ModulUmum

def lcm(x,y):
    if x > y:
       greater = x
    else:
       greater = y
    bool = True
    while(bool):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           bool = False
       greater += 1

    return lcm


def bangkitKunci(p,q,g):
    n = p*q
    lamda = lcm(p-1,q-1)
    k = ((pow(g,lamda)%pow(n,2))-1)/n
    publick = [n,g]
    privat = [lamda,int(k)]
    return publick, privat

def encrypt(m,publick,r):
    c = pow(publick[1],m)*pow(r,publick[0])%pow(publick[0],2)
    return c

def decrypt(chiper, privat,publick):
    kinvers = ModulUmum.modInverse(privat[1],publick[0])
    temp = ((pow(chiper,privat[0])%pow(publick[0],2))-1)/publick[0]
    plain = temp*kinvers%publick[0]
    return int(plain)

p = int(input("Masukan nilai p:"))
q = int(input("Masukan nilai q:"))
g = int(input("Masukan nilai g:"))
publick,privat = bangkitKunci(p,q,g)
print(publick)
print(privat)
chiper = encrypt(51,publick,23)
print(chiper)
plain = decrypt(chiper,privat,publick)
print(plain)