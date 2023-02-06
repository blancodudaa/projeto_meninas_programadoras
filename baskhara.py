a= float(input())
b=float(input())
c=float(input())

delta=(b**2)-(4*a*c)
x1=(((-1)*b) + (delta**0.5))/(2*a)
x2=(((-1)*b) - (delta**0.5))/(2*a)

if delta <0:
    print("0")

elif delta ==0:
    print('1')
else:
    print("2")


    