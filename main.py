#y0 arvot a- ja b kohtiin
# demonstroidaan Rungekutan ja eksplisiittisen eulerin menetelmien tarkkuuseroja
Ay0=-1
By0=0.5
# h:n arvot
h1=0.1 #100 askelta
h2=0.2 #50 askelta
h3=0.5 #20 askelta
h4=1 #10 askelta
h5=2 #5 askelta
# iteroinnin päätepiste
t=10
#Tarkat arvot
A=18.000045399
B=0.9999999979387
#eksplisiittinen Eulerin menetelmä a) ja b)kohdille

def eksplisiittinen_EulerA(h,t,y0):#a)-kohdan metodi
    iteraatioiden_määrä=int(t/h)
    ##Alustetaan lista y:n arvoja varten
    y=[0 for i in range(iteraatioiden_määrä+1)]
    # asetetaan indeksiin 0 y0:n arvo
    y[0]=y0
    ti=0 # t:n arvo joka iteraatiokierroksella. alkaa nollasta
    for i in range(iteraatioiden_määrä):
        # y[k+1] = y[k]+h*f(t,y(t))=y[k]+2*h(2*t-y(t))
        y[i+1]=y[i]+h*(2*ti-y[i])
        ti = ti + h
    return y
def eksplisiittinen_EulerB(h,t,y0):#b)-kohdan metodi
    iteraatioiden_määrä=int(t/h)
    y=[0 for i in range(iteraatioiden_määrä+1)]
    y[0]=y0
    ti=0
    for i in range(iteraatioiden_määrä):
        #y[k+1] = y[k]+h*f(t,y(t))=y[k]+2*h(2*y(t)(1-y(t)))
        y[i+1]=y[i]+h*(2*y[i]*(1-y[i]))
        ti = ti + h
    return y


# 4-vaiheinen Runge-Kutta metodi
def Runge_KuttaA(h,t,y0):#a)-kohdan toteutus
    iteraatioiden_määrä = int(t / h)
    #Alustetaan lista y:n arvoja varten
    y = [0 for i in range(iteraatioiden_määrä + 1)]
    #asetetaan indeksiin 0 y0:n arvo
    y[0] = y0
    ti = 0 # t:n arvo joka iteraatiokierroksella. alkaa nollasta
    for i in range(iteraatioiden_määrä):
        #lasketaan k:n arvot joka iteraatiokerralle
        k1=2*ti-y[i]
        k2=2*(ti+0.5*h)-(y[i]+0.5*h*k1)
        k3=2*(ti+0.5*h)-(y[i]+0.5*h*k2)
        k4=2*(ti+h)-(y[i]+h*k3)
        y[i+1]=y[i]+h/6*(k1+2*k2+2*k3+k4)
        #päivitetään t:n arvoa
        ti = ti + h
    return y #palautetaan lista laskettuja y:n arvoja. Kaikki askeleet

def Runge_KuttaB(h,t,y0):#b)-kohdan toteutus
    iteraatioiden_määrä = int(t / h)
    y = [0 for i in range(iteraatioiden_määrä + 1)]
    y[0] = y0
    ti = 0
    for i in range(iteraatioiden_määrä):
        k1=2*y[i]*(1-y[i])
        k2=2*(y[i]+0.5*h*k1)*(1-(y[i]+0.5*h*k1))
        k3=2*(y[i]+0.5*h*k2)*(1-(y[i]+0.5*h*k2))
        k4=2*(y[i]+h*k3)*(1-(y[i]+h*k3))
        y[i+1]=y[i]+h/6*(k1+2*k2+2*k3+k4)
        ti = ti + h
    return y
print("A-kohta:")
print("Eksplisiittinen Euler: 5 askelta")
print(eksplisiittinen_EulerA(h5,t,Ay0))
print("Eksplisiittinen Euler: 10 askelta")
print(eksplisiittinen_EulerA(h4,t,Ay0))
print("Runge-Kutta: 5 askelta")
print(Runge_KuttaA(h5,t,Ay0))
print("Runge-Kutta: 10 askelta")
print(Runge_KuttaA(h4,t,Ay0))
print("A-kohdan tarkka arvo:")
print(Runge_KuttaA(0.000001,t,Ay0)[-1])
#print(eksplisiittinen_EulerA(0.000001,t,Ay0)[-1])
print("Virheet")
print("Eksplisiittinen Euler: 5 askelta")
print("Suhteellinen virhe: "+str((A-eksplisiittinen_EulerA(h5,t,Ay0)[-1])/A)+"%")
print("Eksplisiittinen Euler: 10 askelta")
print("Suhteellinen virhe: "+str((A-eksplisiittinen_EulerA(h4,t,Ay0)[-1])/A)+"%")
print("Eksplisiittinen Euler: 20 askelta")
print("Suhteellinen virhe: "+str((A-eksplisiittinen_EulerA(h3,t,Ay0)[-1])/A)+"%")
print("Runge-Kutta: 5 askelta")
print("Suhteellinen virhe: "+str((A-Runge_KuttaA(h5,t,Ay0)[-1])/A)+"%")
print("Runge-Kutta: 10 askelta")
print("Suhteellinen virhe: "+str((A-Runge_KuttaA(h4,t,Ay0)[-1])/A)+"%")
print("Runge-Kutta: 20 askelta")
print("Suhteellinen virhe: "+str((A-Runge_KuttaA(h3,t,Ay0)[-1])/A)+"%")
print()
print()
print("B-kohta:")
print("Eksplisiittinen Euler: 10 askelta")
print(eksplisiittinen_EulerB(h4,t,By0))
print("Eksplisiittinen Euler: 20 askelta")
print(eksplisiittinen_EulerB(h3,t,By0))
print("Runge-Kutta: 10 askelta")
print(Runge_KuttaB(h4,t,By0))
print("Runge-Kutta: 20 askelta")
print(Runge_KuttaB(h3,t,By0))
print("B-kohdan tarkka arvo:")
print(Runge_KuttaB(0.000001,t,By0)[-1])
#print(eksplisiittinen_EulerB(0.000001,t,By0)[-1])
print("Virheet")
print("Eksplisiittinen Euler: 5 askelta")
print("Suhteellinen virhe: "+str((B-eksplisiittinen_EulerB(h5,t,By0)[-1])/B)+"%")
print("Eksplisiittinen Euler: 10 askelta")
print("Suhteellinen virhe: "+str((B-eksplisiittinen_EulerB(h4,t,By0)[-1])/B)+"%")
print("Eksplisiittinen Euler: 20 askelta")
print("Suhteellinen virhe: "+str((B-eksplisiittinen_EulerB(h3,t,By0)[-1])/B)+"%")
print("Eksplisiittinen Euler: 40 askelta")
print("Suhteellinen virhe: "+str((B-eksplisiittinen_EulerB(0.25,t,By0)[-1])/B)+"%")
print("Runge-Kutta: 5 askelta")
print("Suhteellinen virhe: "+str((B-Runge_KuttaB(h5,t,By0)[-1])/B)+"%")
print("Runge-Kutta: 10 askelta")
print("Suhteellinen virhe: "+str((B-Runge_KuttaB(h4,t,By0)[-1])/B)+"%")
print("Runge-Kutta: 20 askelta")
print("Suhteellinen virhe: "+str((B-Runge_KuttaB(h3,t,By0)[-1])/B)+"%")
print("Runge-Kutta: 40 askelta")
print("Suhteellinen virhe: "+str((B-Runge_KuttaB(0.25,t,By0)[-1])/B)+"%")