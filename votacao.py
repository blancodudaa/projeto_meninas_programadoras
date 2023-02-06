v1=int(input())
v2=int(input())
v3= int(input())
v4=int(input())

if v1 > v2 and v1> v3 and v1> v4:
    print(v1)
if v2> v3 and v2> v4 and v2 > v1:
    print(v2)
if v3 > v4 and v3 > v2 and v3 > v1:
    print(v3)
else:
    print(v4)