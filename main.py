import array
b = 120
# (a, b) = 1
# a^t mod b = 1

#fi(b) = b* П (1 do n) ((p-1)/p) -- b = p1*p2*p3...pn

#naci proste brojeve
prosti = array.array('i',(0 for i in range(0,b+1)))
for i in range(2,b+1):
    prosti[i-2] = i
for i in range(2,11):
    for k in prosti:
        if(k % i == 0 and k!=i):
            prosti.remove(k)
#print(prosti)

#naci fi(b)
rezultat = b
ostatak = b
list = []
while(ostatak != 1):
    for i in prosti:
        if(ostatak % i == 0):
            #print(i)
            if(not list.__contains__(i)):
                rezultat = rezultat * float(((i-1)/i))
                list.append(i)
            ostatak = ostatak/i
            #print(rezultat)
            break
rezultat = int(rezultat)
print("Fi(b):",rezultat)

a=0
#naci (a,b)=1
for i in range(2,b):
    if(pow(i,rezultat,b) == 1):
        print("a:",i)
        a=i