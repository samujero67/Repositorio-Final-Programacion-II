def f1(f,a,b):
    Resl = 0
    for i in range(a,b+1):
        Resl += (f(i)*i)
    return Resl

def f2(L):
    def f(x):
        cont=0
        poli= 0
        for i in L:
            poli+=(i*(x**cont))
            cont+=1
        return poli
    return f

def f3(x0,y0):
    def recta(x):
        b = y0-(2*x0)
        return 2 * x + b
    def paralela(x):
        return 2*x-1
    return recta,paralela

def f4(L):
    nueva=[]
    for i in L:
        tep=[]
        if i > 10:
            h = str(i)
            for c in h:
                tep.append(int(c))
            u = tep[0]+tep[-1]
            if (u) % 2 == 0:
                nueva.append(i)
    return sum(nueva)