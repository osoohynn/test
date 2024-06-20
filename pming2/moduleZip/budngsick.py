import classZip as cz

# class Bu_pan(cz.Pan):
#     def __init__(self):
#         a = int(input("a: "))
#         b = int(input("b: "))
#         c = int(input("c: "))
#         super().__init__(a, b, c)

# 수정 필요함.
class Bu_hae(cz.Bang, cz.Pan):
    def __init__(self):
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        super().__init__(a, b, c)
    
    def hae(self):
        d = input("부등호 기호를 입력해주세요: ")
        return d

def result(d, D, small, big):
    if D>0:
        if d==">":
            print(f"x < {small} or x {d} {big}")
        elif d==">=":
            print(f"x <= {small} x or x {d} {big}")
        elif d=="<" or d=="<=":
            print(f'{small} {d} x {d} {big}')
    elif D == 0:
        if d==">":
            print(f"x != {small} 인 모든 실수")
        elif d==">=":
            print("모든 실수")
        elif d=="<":
            print("해는 없다.")
        elif d=="<=":
            print(f"x = {small}")
    elif D < 0:
        if d==">" or d==">=":
            print("모든 실수")
        elif d=="<" or d=="<=":
            print("해는 없다.")
    else:
        print("예상치 못한 입력으로 시스템을 종료합니다.")

def budbgsick_reque():
    answer = int(input("""
1. 해(근) 구하기

2. 수직선 보기

"""))
    if answer==1:
        cz.des_bu()
        try1 = Bu_hae()
        d = try1.hae()
        D = try1.d_Pan()
        answer = cz.puli()
        small, big = try1.fun_1()
        if answer == 'y':
            cz.answer_print()
            if d=="<" or d=="<=" or d==">" or d==">=":
                print(f"D = {D}")
                result(d, D, small, big)
            else:
                print("예상치 못한 입력으로 시스템을 종료합니다.")
            cz.answer_print()
        elif answer == 'n':
            cz.answer_print()
            if d=="<" or d=="<=" or d==">" or d==">=":
                result(d, D, small, big)
            else:
                print("예상치 못한 입력으로 시스템을 종료합니다.")
            cz.answer_print()
        else:
            print("예상치 못한 입력으로 시스템을 종료합니다.")
    elif answer == 2:
        cz.des_bu()
        pass
    else:
        print("숫자 제대로")
        bangjungsick_reque()

# 테스트
# a = Bu_hae()
# print(a.fun_1())