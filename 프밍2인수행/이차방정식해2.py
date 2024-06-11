import math 
def fun_2(a,b,c):
    return (((-b+math.sqrt(b**2-4*a*c))/2*a)*(-1), ((-b-math.sqrt(b**2-4*a*c))/2*a)*(-1))
    # (x + "이부분")(x + "이부분")
    # 으로 만듬. 해를 구하려면 여기에 (-1)곱하면 됨.

print(fun_2(1,4,-12))