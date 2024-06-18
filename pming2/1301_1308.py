# cd Desktop/python/pming2
# python3 13011308.py

import bangjungsick as ba
import hamsu as ha

import classZip as cz

import time as t
from art import text2art,tprint
import os
os.system('clear')

print(text2art("* * * * *", font="slant"))
print(text2art("          gyesan",font="tarty1"))
print(text2art("             dream",font="tarty1"))
print()
print(text2art("* * * * *", font="slant"))
print(" "*30, "계산드림  made by 권수현, 서현동")

t.sleep(1.2)

print("""""")

def manual():
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
?           4. 최댓닶, 최솟값 구하기        ?
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

    firstChoice = int(input("""
이차방정식 메뉴를 이용하고 싶으시면 1,

이차함수   메뉴를 이용하고 싶으시면 2,

이차부등식 메뉴를 이용하고 싶으시면 3,

종료하고 싶으시면 4 를 입력해주세요
        
"""))
    return firstChoice

def main_reque():
    firstChoice = manual()

    if firstChoice == 1:
        ba.bangjungsick_reque()
        answer = cz.again()
        if answer == 'y':
            main_reque()
    elif firstChoice == 2:
        ha.hamsu_reque()
        answer = cz.again()
        if answer == 'y':
            main_reque()
    elif firstChoice == 3:
        pass
    elif firstChoice == 4:
        print("감사합니다.")
    else:
        print("올바른 숫자를 입력해주세요")
        print(firstChoice)

main_reque()