# cd Desktop/python/pming2
# python3 13011308.py

import classZip as cz

import time as t
from art import text2art,tprint
import os
os.system('clear')

print(text2art("* * * * *", font="slant"))
print(text2art("          gyesan",font="tarty1"))
print(text2art("             dream",font="tarty1"))
print(text2art("* * * * *", font="slant"))
print(" "*30, "계산드림  made by 권수현, 서현동")

t.sleep(1.2)

print("""""")

print("""
************매뉴얼입니다************
?
?
?   I 이차방정식
?
?       1. 해(근) 구하기
?
?       2. 판별식 구하기
?
?
?   II 이차함수
?
?       1. 해(근) 구하기
?
?       2. 판별식 구하기
?
?       3. 그래프 보기
?
?       4. 최댓닶, 최솟값 구하기
?
?
?   III 이차부등식
?
?       1. 해(근) 구하기
?
?       2. 수직선 보기
?
?
? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ?
""")

t.sleep(1)

print("\n-------------------------------\n")

firstChoice = input("""
이차방정식 메뉴를 이용하고 싶으시면 1,

이차함수   메뉴를 이용하고 싶으시면 2,

이차부등식 메뉴를 이용하고 싶으시면 3,

종료하고 싶으시면 4 를 입력해주세요

""")
