# cd Desktop/python/pming2
# python3 13011308.py

import moduleZip.bangjungsick as ba
import moduleZip.hamsu as ha
import moduleZip.budngsick as bu

# 클래스 모아놓은 사용자 모듈
import classZip as cz

import time as t
from art import text2art,tprint

# 실행하면 기록 지워주는 모듈
import os
os.system('clear')

# 계산드림 로고
print(text2art("* * * * *", font="slant"))
print(text2art("          gyesan",font="tarty1"))
print(text2art("             dream",font="tarty1"))
print(text2art("* * * * *", font="slant"))
print(" "*30, "계산드림  made by 권수현, 서현동")
# 여기까지


# 잠깐 딜레이
t.sleep(1.2)


def manual():
    # manual함수를 호출하면 매뉴얼을 보여준다.
    # 사용자에게 편의를 제공하기 위해 전체 매뉴얼을 보여주는 것.
    print("""
* * * * * * * * * 매뉴얼입니다* * * * * * * *
?                                           ?
?                                           ?
?       I 이차방정식                        ?
?                                           ?
?           1. 해(근) 구하기                ?
?                                           ?
?           2. 판별식 구하기                ?
?                                           ?
?                                           ?
?       II 이차함수                         ?
?                                           ?
?           1. 해(근) 구하기                ?
?                                           ?
?           2. 판별식 구하기                ?
?                                           ?
?           3. 그래프 보기                  ?
?                                           ?
?           4. 최댓값, 최솟값 구하기        ?
?                                           ?
?                                           ?
?       III 이차부등식                      ?
?                                           ?
?           1. 해(근) 구하기                ?
?                                           ?
?           2. 수직선 보기                  ?
?                                           ?
?                                           ?
? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ?
    """)

    t.sleep(1)

    print("-------------------------------\n")

    # 1, 2, 3 중에 원하는 것을 선택하고 그 값을 int로 변환하여
    firstChoice = int(input("""
이차방정식 메뉴를 이용하고 싶으시면 1,

이차함수   메뉴를 이용하고 싶으시면 2,

이차부등식 메뉴를 이용하고 싶으시면 3,

종료하고 싶으시면 4 를 입력해주세요
        
"""))
    # 리턴한다.
    return firstChoice

def main_reque():
    firstChoice = manual()
    # manual 함수를 호출해서 첫번 째 선택한 값을 firstChoice에 담는다.
    # 만약 firstChoice가 int가 아닌 다른 자료형이 입력되면 빠져나갈 예외처리 구현 필요함.

        # 1: 이차방정식 선택
    if firstChoice == 1:
        
        # 방정식 중에서 어떤 메뉴를 선택할 것인지 묻는 함수를 호출한다.
        ba.bangjungsick_reque()

        # 재사용 여부를 묻는 함수를 호출한다.
        # 만약 y라면 main_reque를 호출하여 다시 시작한다.
        answer = cz.again()
        if answer == 'y':
            main_reque()
        elif answer == 'n':
            print("감사합니다. 시스템을 종료합니다.")
        else:
            print("예상치 못한 입력으로 시스템을 종료합니다.")

        # 2: 이차함수 선택
    elif firstChoice == 2:

        # 함수 중에서 어떤 메뉴를 선택할 것인지 묻는 함수를 호출한다.
        ha.hamsu_reque()

        # 재사용 여부를 묻는 함수를 호출한다.
        # 만약 y라면 main_reque를 호출하여 다시 시작한다.
        answer = cz.again()
        if answer == 'y':
            main_reque()
        elif answer == 'n':
            print("감사합니다. 시스템을 종료합니다.")
        else:
            print("예상치 못한 입력으로 시스템을 종료합니다.")

        # 3: 이차부등식 선택
    elif firstChoice == 3:

        # 부등식 중에서 어떤 메뉴를 선택할 것인지 묻는 함수를 호출한다.
        bu.budbgsick_reque()

        # 재사용 여부를 묻는 함수를 호출한다.
        # 만약 y라면 main_reque를 호출하여 다시 시작한다.
        answer = cz.again()
        if answer == 'y':
            main_reque()
        elif answer == 'n':
            print("\n감사합니다. 시스템을 종료합니다.")
        else:
            print("예상치 못한 입력으로 시스템을 종료합니다.")

        # 4: 종료 선택
    elif firstChoice == 4:
        print("감사합니다. 시스템을 종료합니다.")

        # 만약 1~4가 아닌 다른 숫자라면
    else:
        print("\n------------------------")
        print(f"{firstChoice}는 올바른 입력이 아닙니다.\n")
        print("올바른 숫자를 입력해주세요.")
        t.sleep(1)

        # 다시 입력할 기회를 준다.
        main_reque()

#처음 실행하면 1회 호출.
main_reque()