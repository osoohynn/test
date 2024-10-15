import numpy as np
import matplotlib.pyplot as plt

import classZip as cz

class Ham_pan(cz.Pan): # 함수의 판별식을 구하는 클래스
    def __init__(self):
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        super().__init__(a, b, c)

class Ham_hae(cz.Pan): # 함수의 해를 구하는 클래스
    def __init__(self):
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        super().__init__(a, b, c)

    def hae(self): # 해를 출력하는 함수
        D = cz.Pan.d_Pan(self)
        if D>0:
            print("서로 다른 두 점에서 만난다.")
        elif D==0:
            print("한 점에서 만난다. (접한다.)")
        else:
            print("만나지 않는다.")

def graph(): # 이차함수의 그래프를 그리는 함수
    a = int(input("a: ")) 
    b = int(input("b: "))
    c = int(input("c: "))

    def find_maximum_of_quadratic(a, b, c): # 최솟값, 최댓값을 구하는 함수
        # 계산을 위해 x 좌표를 정점 공식을 이용해 구함: x = -b / (2*a)
        x_vertex = -b / (2 * a)
        # 정점에서의 최댓값을 계산함: y = ax^2 + bx + c
        y_maximum = a * x_vertex**2 + b * x_vertex + c
        return x_vertex, y_maximum

    max,min=find_maximum_of_quadratic(a,b,c)

    # a가 양수일 경우 최솟값, a가 음수일 경우 최댓값을 이용하여 좌표설정
    if a>0:
        x = np.arange(max-8,max+9)
        y =(x**2)+x*(b//a)+(c//a)
    else:
        x = np.arange(max-8,max+9)
        y =-(x**2)+x*(b//a)+(c//a)

    # 그래프를 그린다
    plt.plot(x, y)
    plt.grid(color='0.8')
    plt.show()

def minmax(): # 최솟값, 최댓값을 찾는 함수

    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

    D1 = cz.Pan(a,b,c)
    D = D1.d_Pan()
    
    g_m= -b / (2 * a)  # 공식을 이용해 구함: x = -b / (2*a)
    if a>0: # a가 양수일 경우 최솟값,
        cz.answer_print()
        print(f"최솟값은 {g_m}입니다.")
        cz.answer_print()
    elif a<0: # a가 음수일 경우 최댓값 출력
        cz.answer_print()
        print(f"최댓값은 {g_m}입니다.")
        cz.answer_print()
    else:
        print("다시 입력하여 주세요")


def hamsu_reque(): # 이차함수 중 어떤 하위 항목을 선택할지 묻고 그에 맞게 알맞은 함수를 호출함
    answer = int(input("""
1. 해(근) 구하기

2. 판별식 구하기

3. 그래프 보기

4. 최댓값, 최솟값 구하기

"""))
    if answer == 1: # II 이차함수 - 1. 해 구하기
        cz.des()
        try1 = Ham_hae()
        answer = cz.puli()
        if answer == 'y':
            cz.answer_print()
            print(f"판별식 D = {try1.D}") # 이차함수 해 풀이
            try1.hae()
            cz.answer_print()
        elif answer == 'n':
            cz.answer_print()
            try1.hae()
            cz.answer_print()
        else:
            print("예상치 못한 입력으로 시스템을 종료합니다.")
    elif answer == 2: # II 이차함수 - 2. 판별식 구하기
        cz.des()
        try1 = Ham_pan()
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
    elif answer == 3: # II 이차함수 - 3.그래프 보기
        cz.des()
        graph()
    elif answer == 4: # II 이차함수 - 4.최솟값, 최댓값 구하기
        cz.des()
        minmax()
    else:
        print("숫자를 제대로 입력해주세요.")
        hamsu_reque()