import math
import classZip as cz


# ax^2 + bx + c
# a, b, c를 차례대로 입허갸ㅓㅇ
# 입력창 나오게,

# class Bang_pan(cz.Pan):
#     def num():
#         a = int(input("a: "))
#         b = int(input("b: "))
#         c = int(input("c: "))
#     def __init__(self, a, b, c):
#         super().__init__(a, b, c)

class Bang_pan(cz.Pan):
    def __init__(self):
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        super().__init__(a, b, c)

class Bang_hae(cz.Bang):
    def __init__(self):
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        super().__init__(a, b, c)


def bangjungsick_reque():
    answer = int(input("""
1. 해(근) 구하기

2. 판별식 구하기

"""))
    if answer==1:
        cz.des()
        try1 = Bang_hae()
        answer = cz.puli()
        if answer == 'y':
            if try1.fun_1()[0]>0:
                t1 = -(try1.fun_1()[0])
            if try1.fun_1()[1]>0:
                t2 = -(try1.fun_1()[1])            
            cz.answer_print()
            print(f"\n인수분해 결과 : (x-{-(t1)})(x-{-(t2)})")
            print(f"\nx = {try1.fun_1()[0]} or x = {try1.fun_1()[1]}\n")
            cz.answer_print()
        elif answer == 'n':
            cz.answer_print()
            print(f"\nx = {try1.fun_1()[0]} or x = {try1.fun_1()[1]}")
            cz.answer_print()
        else:
            print("예상치 못한 입력으로 시스템을 종료합니다.")
    elif answer == 2:
        cz.des()
        try1 = Bang_pan()
        answer = cz.puli()
        if answer == 'y':
            cz.answer_print()
            print("D = b² - (4 * a * c)")
            print(f"D = {try1.b}² - (4 * {try1.a} * {try1.c})")
            print(f"D = {try1.d_Pan()}")
            cz.answer_print()
        elif answer == 'n':
            cz.answer_print()
            print(f"D = {try1.d_Pan()}")
            cz.answer_print()
        else:
            print("예상치 못한 입력으로 시스템을 종료합니다.")
    else:
        print("숫자 제대로")
        bangjungsick_reque()

# bangjungsick_reque()