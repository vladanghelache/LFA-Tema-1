f = open('txt.in')
n = int(f.readline())
m = int(f.readline())
alfabet = []
for x in f.readline().split():
    alfabet += x
q0 = int(f.readline())
k = int(f.readline())
stari_finale = []
for x in f.readline().split():
    stari_finale += [int(x)]
I = int(f.readline())
d = {}
for i in range(I):
    x = f.readline().split()
    if (int(x[0]),x[1]) not in d.keys():
        d[(int(x[0]),x[1])] = [int(x[2])]
    else:
        d[(int(x[0]), x[1])] += [int(x[2])]
for cuvant in f.readlines():
    cuvant = cuvant.strip('\n')
    ok=False

    def functie(i,stare):
        global ok
        if i == len(cuvant) and (stare in stari_finale):
            ok = True
        else:
            if i < len(cuvant) and (stare,cuvant[i]) in d.keys() :
                for x in d[(stare,cuvant[i])]:
                    functie(i+1,x)
            if (stare,'$') in d.keys():
                for x  in d[(stare,'$')]:
                    functie(i,x)
    functie(0,q0)
    if ok == True:
        print(cuvant,"DA")
    else:
        print(cuvant,"NU")
f.close()