negyjegyu=[]
pali=[]
for i in range(1000,10000):
    negyjegyu.append(i)
for j in range(1000,10000):
    for k in range(len(negyjegyu)):
        n=j*negyjegyu[k]
        szam=str(n)
        forditott=szam[::-1]
        if(szam==forditott):
            pali.append(n)



max=pali[0]
for i in pali:
    if i>max:
        max=i


print("{} a legnagyobb palindrom szam, amely eloall ket negyjegyu szam szorzatakent.".format(max))