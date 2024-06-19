import numpy as np
import matplotlib.pyplot as plt

import classZip as cz

class Ham_pan(cz.Pan):
    def __init__(self):
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        super().__init__(a, b, c)

class Ham_hae(cz.Bang):
    pass

def graph():
    def find_maximum_of_quadratic(a, b, c):
        # 계산을 위해 x 좌표를 정점 공식을 이용해 구함: x = -b / (2*a)
        x_vertex = -b / (2 * a)
        # 정점에서의 최댓값을 계산함: y = ax^2 + bx + c
        y_maximum = a * x_vertex**2 + b * x_vertex + c
        return x_vertex, y_maximum

    a=float(input("a: "))
    b=float(input("b: "))
    c=float(input("c: "))
    max,min=find_maximum_of_quadratic(a,b,c)
    print(max)
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

def minmax():
    pass

def hamsu_reque():
    answer = int(input("""
1. 해(근) 구하기

2. 판별식 구하기

3. 그래프 보기

4. 최댓닶, 최솟값 구하기

"""))
    if answer == 1:
        pass
    elif answer == 2:
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
    elif answer == 3:
        graph()
    elif answer == 4:
        pass
    else:
        print("숫자 제대로")
        hamsu_reque()