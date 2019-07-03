import math
print('enter coefficient a')
a=float(input())
print('enter coefficient b')
b=float(input())
print('enter coefficient c')
c=float(input())

delta=(b*b-4.0*a*c)
if delta <0.0:
    print('no solution')
else:
    x1=((-b+math.sqrt(delta))/2*a)
    x2=((-b-math.sqrt(delta))/2*a)
    print("the first solution is {}, the second solution is {}".format(x1, x2))