print("*이차부등식의 우변에 0만 남기고 모두 좌변으로 이항해주신 후 입력해주세요*")
print()

a = int(input("x^2의 계수를 입력하세요: "))
b = int(input("x의 계수를 입력하세요: "))
c = int(input("상수항을 입력하세요: "))
d = input("'>' 또는 '<' 또는 '<=' 또는 '>='를 입력하세요: ")


import math 
def fun_2(a,b,c):
    return (((-b+math.sqrt(b**2-4*a*c))/2*a)*(1), ((-b-math.sqrt(b**2-4*a*c))/2*a)*(1))
    
if d=="<" or d=="<=":
    print(f'{min(fun_2(a,b,c))} {d} x {d} {max(fun_2(a,b,c))}')
elif d==">" or d==">=":
    print(f"{min(fun_2(a,b,c))} {d} x or x {d} {max(fun_2(a,b,c))}")