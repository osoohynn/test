import math

# 부모 클래스가 있는 python 파일을 모듈화 하여 불러옴.
import classZip as cz

class Bang_pan(cz.Pan): # 방정식의 판별식을 구하는 클래스
    def __init__(self): # 생성자, a,b,c를 입력받아 부모클래스에게 전달.
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        super().__init__(a, b, c)

class Bang_hae(cz.Bang): # 방정식의 해를 구하는 클래스
    def __init__(self):
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        super().__init__(a, b, c)


def bangjungsick_reque(): # 이차방정식 중 어떤 하위 항목을 선택할지 묻고 그에 맞게 알맞은 함수를 호출함
    answer = int(input("""
1. 해(근) 구하기

2. 판별식 구하기

"""))
    if answer==1: # I 이차방정식 - 1. 해 구하기
        cz.des() # 설명 띄우기
        try1 = Bang_hae() # 인스턴스 생성
        answer = cz.puli() #해만 볼건지, 풀이까지 볼 것인지 판단한 후 answer에 담음
        if answer == 'y':
            sign1 = '-'  #초기값 세팅
            sign2 = '-'
            t1 = list(try1.fun_1()).copy()[0]
            t2 = list(try1.fun_1()).copy()[1]
            if try1.fun_1()[0]<0: # 작은 값이 음수면 양수로 만들어준다
                t1 = -(list(try1.fun_1()).copy()[0])  # 풀이에선 (x-t1) 으로 나오기 때문
                sign1 = '+'                          # 만약 t1을 바꿨다면 부호도 바꿔주기
            if try1.fun_1()[1]<0:
                t2 = -(list(try1.fun_1()).copy()[1])
                sign2 = '+'
            cz.answer_print()
            print(f"\n인수분해 결과 : (x {sign1} {t1})(x {sign2} {t2})") # 이차방정식 풀이
            print(f"\nx = {try1.fun_1()[0]} or x = {try1.fun_1()[1]}\n") # 이차방정식 답
            cz.answer_print()
        elif answer == 'n':
            cz.answer_print()
            print(f"\nx = {try1.fun_1()[0]} or x = {try1.fun_1()[1]}")
            cz.answer_print()
        else:
            print("예상치 못한 입력으로 시스템을 종료합니다.") # 만약 잘못된 값이 입력되면 프로그램 종료
    elif answer == 2: # I 이차방정식 - 2. 판별식 구하기
        cz.des()
        try1 = Bang_pan() # 인스턴스 생성
        answer = cz.puli()
        if answer == 'y':
            cz.answer_print()
            print("D = b² - (4 * a * c)") # 판별식 풀이
            print(f"D = {try1.b}² - (4 * {try1.a} * {try1.c})")
            print(f"D = {try1.d_Pan()}") # 판별식 답
            cz.answer_print()
        elif answer == 'n':
            cz.answer_print()
            print(f"D = {try1.d_Pan()}")
            cz.answer_print()
        else:
            print("예상치 못한 입력으로 시스템을 종료합니다.")
    else:
        print("숫자를 제대로 입력해주세요.")
        bangjungsick_reque()