import numpy as np
import matplotlib.pyplot as plt

#2차함수에서 d,c 부분 입력 필요
def graph():
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

    if a>1:
        b=b/a
        c=c/a

    x = np.arange(-8,9) # 값 표시 범위
    y = x**2+x*(b)+(c) # 그래프를 표시할 2차함수

    # 그래프를 그린다
    plt.plot(x, y)
    plt.grid(color='0.8')
    plt.show()

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
        pass
    elif answer == 3:
        graph()
    elif answer == 4:
        pass
    else:
        print("숫자 제대로")
        hamsu_reque()