import classZip as cz


# 수정 필요함.
class Bu_hae(cz.Bang):
    def __init__(self):
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        super().__init__(a, b, c)
    
    def hae(self):
        d = input("부등호 기호를 입력해주세요: ")
        return d

def budbgsick_reque():
    answer = int(input("""
1. 해(근) 구하기

2. 수직선 보기

"""))
    if answer==1:
        try1 = Bu_hae()
        d = try1.hae()
        answer = cz.puli()
        if answer == 'y':
            cz.answer_print()
            if d=="<" or d=="<=":
                print(f'{min(try1.fun_1())} {d} x {d} {max(try1.fun_1())}')
            elif d==">" or d==">=":
                print(f"{min(try1.fun_1())} {d} x or x {d} {max(try1.fun_1())}")
            else:
                print("예상치 못한 입력으로 시스템을 종료합니다.")
            cz.answer_print()
        elif answer == 'n':
            cz.answer_print()
            if d=="<" or d=="<=":
                print(f'{min(try1.fun_1())} {d} x {d} {max(try1.fun_1())}')
            elif d==">" or d==">=":
                print(f"{min(try1.fun_1())} {d} x or x {d} {max(try1.fun_1())}")
            else:
                print("예상치 못한 입력으로 시스템을 종료합니다.")
        else:
            print("예상치 못한 입력으로 시스템을 종료합니다.")
    elif answer == 2:
        pass
    else:
        print("숫자 제대로")
        bangjungsick_reque()

# 테스트
# a = Bu_hae()
# print(a.fun_1())