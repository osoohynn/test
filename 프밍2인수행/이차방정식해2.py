import math 
def fun_2(a,b,c):
    return (((-b+math.sqrt(b**2-4*a*c))/2*a)*(1), ((-b-math.sqrt(b**2-4*a*c))/2*a)*(1))

a = int(input("x^2의 계수를 입력하세요: "))
b = int(input("x의 계수를 입력하세요: "))
c = int(input("상수항을 입력하세요: "))

# print(fun_2(a,b,c))
print(f"x = {min(fun_2(a,b,c))} or x = {max(fun_2(a,b,c))}")