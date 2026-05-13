def f1(f,a,b):
    sum=0
    for i in range(a,b+1):
        sum+=f(i)*i
    return sum
def f2(L):
    def f(x):
        sum=0
        for i in L:
            sum+=i*(x**(i-1))
        return sum
    return f
def f3(x0,y0):
    m=2
    def recta(x):
        y=m*(x-x0)+y0
        return y
    def paralela(x):
        x1,y1=1,1
        m=2
        y=m*(x-x1)+y1
        return y
    return recta,paralela
def f4(L):
    sumault=0
    resul=0
    for i in L:
        i2=int(str(i)[0])
        i3=int(str(i)[-1])
        sum=i2+i3
        if sum%2==0:
            resul+=i
    return resul


