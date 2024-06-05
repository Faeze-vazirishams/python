a,b,c,d,e= (input("R=")).split()
x=(float(a)+float(b)+float(c)+float(d)+float(e))/5
x=float(x)
if x>=18 and x<20:
    print("A")
if x>=15 and x<17.99:
    print("B")
if x>=12 and x<14.99:
    print("C")
if x>=0 and x<11.99:
    print("F")
if x>=20:
    print("Invalid Grade")
