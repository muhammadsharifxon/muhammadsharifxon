import math
print("UniMath dasturi")
print("Algebraik va Geometrik masalalarni avtomtik yechishga yo'naltirilgan dasturi")
print('Kvadrat tenglama: 1 ni kiriting')
print('Kvadrat yuzi: 2 ni kiriting ')
print('Kvadrat perimetri: 3 ni kiriting')
print('To`g`ri to`rt burchak perimetri: 4 ni kiriting')
print('To`g`ri to`rt burchak dioganali: 5 ni kiriting')
print('To`g`ri to`rt burchak yuzi:6 ni kiriting')
print('Uchburchak yuzi Geron formulasi:7 ni kiriting')
print('Uchburchak perimetri: 8 ni kiriting')
print('Uchburchak gipotenuza: 9 ni kiriting')
print('Aylana yuzi: 10 ni kiriting')
print('Aylana uzunligi:11 ni kiriting')
print('Trapetsiya yuzini topish: 12 ni kiriting')
print('Slindir hajmini topish: 13 ni kiriting')
print('Konus hajmini topish: 14 ni kiriting')
print('Shar hajmini topish: 15 ni kiriting')
print('Konus tashqi yuzasi: 16 ni kiriting')
print('Shar tashqi yuzasi: 17 ni kiriting')
print('Piramida hajmi: 18 ni kiriting')
print('Kvadrat dioganal uzunligi: 19 ni kiriting')
print('Romb yuzini balandllik orqali topish: 20 ni kiriting')
x=float(input('Mavzu raqamini kiriting-'))
if x==1:
    print("Kvadrat tenglama")
    a = int(input("a ni qiymatini kiriting-"))
    b = int(input("b ni qiymatini kiriting-"))
    c = int(input("c ni qiymatini kiriting-"))
    D=(b**2)-4*a*c
    if D>0:
        x1=(-b+math.sqrt((b**2)-4*a*c))/(2*a)
        x2=(-b-math.sqrt((b**2)-4*a*c))/(2*a)
        print("x1=",x1," x2=",x2)
    elif D==0:
        x1=-b/(2*a)
    else:
        print("Bo'sh to'plam")
elif x==2:
    print("Kvadrat yuzi")
    a = int(input("Tomonni kiriting-"))
    print("S=",a**2)
elif x==3:
    print("Kvadrat perimetri")
    a = int(input("Tomonni kiriting-"))
    print("P=",4*a)
elif x==4:
    print("To`g`ri to`rt burchak perimetri")
    a = int(input("a tomonni kiriting-"))
    b = int(input("b tomonni kiriting-"))
    print("P=",2*(a+b))
elif x==5:
    print("To`g`ri to`rt burchak dioganali")
    a = int(input("a tomonni kiriting-"))
    b = int(input("b tomonni kiriting-"))
    print("d=",math.sqrt((a**2)+(b**2)))
elif x==6:
    print("To`g`ri to`rt burchak yuzi")
    a = int(input("a tomonni kiriting-"))
    b = int(input("b tomonni kiriting-"))
    print("S=",a*b)
elif x==7:
    print("Uchburchak yuzi Geron")
    a = int(input("a tomonni kiriting-"))
    b = int(input("b tomonni kiriting-"))
    c = int(input("c tomonni kiriting-"))
    P=a+b+c
    print("S=",math.sqrt(P*(P-a)*(P-b)*(P-c)))
elif x==8:
    print("Uchburchak perimetri")
    a = int(input("a tomonni kiriting-"))
    b = int(input("b tomonni kiriting-"))
    c = int(input("c tomonni kiriting-"))
    print("P=",a+b+c)
elif x==9:
    print("Uchburchak gipotenuza")
    a = int(input("a tomonni kiriting-"))
    b = int(input("b tomonni kiriting-"))
    print("c=",math.sqrt((a**2)+(b**2)))
elif x==10:
    print("Aylana yuzi")
    r = int(input("radiusni kiriting-"))
    print("S=",math.pi*(r**2))
elif x==11:
    print("Aylana uzunligi")
    r = int(input("radiusni kiriting-"))
    print("C=",2*math.pi*r)
elif x==12:
    print("Trapetsiya yuzini topish")
    a = int(input("a tomonni kiriting-"))
    b = int(input("b tomonni kiriting-"))
    h = int(input("h balandlikni kiriting-"))
    S=((a+b)/2)*h
    print("S=",S)
elif x==13:
    print("Slindir hajmini topish")
    R = int(input("R Radiusni kiriting-"))
    h = int(input("h balandlikni kiriting-"))
    V=math.pi*(R**2)*h
    print("V=",V)
elif x==14:
    print("Konus hajmini topish")
    S = int(input("S asos yuzasini kiriting-"))
    h = int(input("h balandlikni kiriting-"))
    V=(1/3)*S*h
    print("V=",V)
elif x==15:
    print("Shar hajmini topish")
    R = int(input("R Radiusni kiriting-"))
    V=(4/3)*math.pi*R**3
    print("V=",V)
elif x==16:
    print("Konus tashqi yuzasi")
    R = int(input("R Radiusni kiriting-"))
    h = int(input("h balandlikni kiriting-"))
    S=math.sqrt(R**2+h**2)
    print("S=",S)
elif x==17:
    print("Shar tashqi yuzasi")
    R = int(input("R Radiusni kiriting-"))
    S=4*math.pi*R**2
    print("S=",S)
elif x==18:
    print("Piramida hajmi")
    h = int(input("h balandlikni kiriting-"))
    V=((a**2)*h)/(4*math.sqrt(3))
    print("V=",V)
elif x==19:
    print("Kvadrat dioganal uzunligi")
    a = int(input("a qiymatini kiriting-"))
    d=a*math.sqrt(2)
    print("d=",d)
elif x==20:
    print("Romb yuzini balandllik orqali topish")
    a = int(input("a tomonni kiriting-"))
    h = int(input("h balandlikni kiriting-"))
    S=a*h
    print("S=",S)
else:
    print('error')
