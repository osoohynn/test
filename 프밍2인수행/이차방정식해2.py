import math 
def fun_2(a,b,c):
    return (((-b+math.sqrt(b**2-4*a*c))/2*a)*(-1), ((-b-math.sqrt(b**2-4*a*c))/2*a)*(-1))

print(fun_2(1,-2,1))