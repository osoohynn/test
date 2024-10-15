import classZip as cz

class Bu_hae(cz.Bang, cz.Pan): # 부등식 해를 구하는 클래스
    def __init__(self):
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        super().__init__(a, b, c)
    
    def hae(self): # 부등호 기호를 입력받고 반환하는 함수
        d = input("부등호 기호를 입력해주세요: ")
        return d

def result(d, D, small, big): # 부등식 해를 조건에 맞게 출력하는 함수
    if D>0: # 판별식이 0보다 클때
        if d==">":
            print(f"x < {small} or x {d} {big}")
        elif d==">=":
            print(f"x <= {small} x or x {d} {big}")
        elif d=="<" or d=="<=":
            print(f'{small} {d} x {d} {big}')
    elif D == 0: # 판별식이 0일 때
        if d==">":
            print(f"x != {small} 인 모든 실수")
        elif d==">=":
            print("모든 실수")
        elif d=="<":
            print("해는 없다.")
        elif d=="<=":
            print(f"x = {small}")
    elif D < 0: # 판별식이 0보다 작을 때
        if d==">" or d==">=":
            print("모든 실수")
        elif d=="<" or d=="<=":
            print("해는 없다.")
    else:
        print("예상치 못한 입력으로 시스템을 종료합니다.")

# 부등호 기호가 '>' 인 경우 그릴 수직선
def ver1(small, big):
        print("\n<______"+" "*(len(str(small))+5)+"______>")
        print("       |"+" "*(len(str(small))+3)+"|")
        print("-------o"+"-"*(len(str(small))+3)+"o------")

        print(' '*5,end="")
        print(small,end="")
        print(' '*5,end="")
        print(big)

# 부등호 기호가 '>=' 인 경우 그릴 수직선
def ver2(small, big):
        print("\n<______"+" "*(len(str(small))+5)+"______>")
        print("       |"+" "*(len(str(small))+3)+"|")
        print("-------@"+"-"*(len(str(small))+3)+"@------")

        print(' '*5,end="")
        print(small,end="")
        print(' '*5,end="")
        print(big)

# 부등호 기호가 '<' 인 경우 그릴 수직선
def ver3(small, big):
        print("\n       "+"_"*(len(str(small))+5))
        print("       |"+" "*(len(str(small))+3)+"|")
        print("-------o"+"-"*(len(str(small))+3)+"o------")

        print(' '*5,end="")
        print(small,end="")
        print(' '*5,end="")
        print(big)

# 부등호 기호가 '<=' 인 경우 그릴 수직선
def ver4(small, big):
        print("\n       "+"_"*(len(str(small))+5))
        print("       |"+" "*(len(str(small))+3)+"|")
        print("-------@"+"-"*(len(str(small))+3)+"@------")

        print(' '*5,end="")
        print(small,end="")
        print(' '*5,end="")
        print(big)

def budbgsick_reque(): # 이차함수 중 어떤 하위 항목을 선택할지 묻고 그에 맞게 알맞은 함수를 호출함
    answer = int(input("""
1. 해(근) 구하기

2. 수직선 보기

"""))
    if answer==1: # III 이차부등식 - 1. 해 구하기
        cz.des_bu()
        try1 = Bu_hae()
        d = try1.hae()
        D = try1.d_Pan()
        answer = cz.puli()
        small, big = sorted(try1.fun_1())
        if answer == 'y':
            cz.answer_print()
            if d=="<" or d=="<=" or d==">" or d==">=":
                print(f"판별식 D = {D}")
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
    elif answer == 2: # III 이차부등식 - 2. 수직선 보기
        cz.des_bu()
        try1 = Bu_hae()
        d = try1.hae()
        small, big = try1.fun_1()
        if d==">": # 조건문으로 부등호 기호에 따라 알맞는 함수 호출
            ver1(small, big)
        elif d==">=":
            ver2(small, big)
        elif d=="<":
            ver3(small, big)
        elif d=="<=":
            ver4(small, big)
        else:
            print("예상치 못한 입력으로 시스템을 종료합니다.")
    else:
        print("숫자를 제대로 입력해주세요.")
        budbgsick_reque()