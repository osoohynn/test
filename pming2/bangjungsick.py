import cmath
import classZip as cz


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


def bangjungsick_reque():
    answer = int(input("""
1. 해(근) 구하기

2. 판별식 구하기

"""))
    if answer==1:
        pass
    elif answer == 2:
        try1 = Bang_pan()
        print(try1.d_Pan())
    else:
        print("숫자 제대로")
        bangjungsick_reque()

