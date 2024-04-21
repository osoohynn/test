# 로또 번호 알려주는 프로그램
# 랜덤으로 1~45까지의 번호 6개 뽑아 출력
# random모듈 사용
# 추가기능으로는 time모듈로 카운트다운 넣기

import random as r
import time as t
import os
os.system('clear')

co_lotto = [11, 13, 20, 21, 32, 44]
co_b_lotto = 8

print("지시가 있기 전까진 입력을 삼가주세요.")
print()
print("______________________________")
print()
t.sleep(.5)
print("복권 번호를 추첨해드립니다.")
print()
t.sleep(1)
print("지갑에 얼마 있으신가요? 숫자로만 입력해주세요.")
money = int(input())
print()
print()

if  money>= 10000:

    print("돈이 많으시네요! 1회당 가격은 만원입니다. 잘 받았습니다^^")
    print()
    t.sleep(2)
    lotto = list(range(1,46))
    u_lotto = r.sample(lotto, 6)
    u_lotto.sort()

    b_lotto = r.randint(1, 45)

    print("공 6개를 뽑아드립니다")
    t.sleep(1)
    print("____________________________")

    print()
    print("당신의 번호는?")
    t.sleep(1)
    print(".")
    t.sleep(1)
    print(".")
    t.sleep(1)
    print(".")
    t.sleep(1)
    # print(u_lotto)
    print(f"""
         -----
       /       \\
      /         \\
     |     {u_lotto[0]}    |
      \\         /
       \\       /
         -----

    """)
    t.sleep(0.5)
    print(f"""
         -----
       /       \\
      /         \\
     |     {u_lotto[1]}    |
      \\         /
       \\       /
         -----

    """)
    t.sleep(0.5)
    print(f"""
         -----
       /       \\
      /         \\
     |     {u_lotto[2]}    |
      \\         /
       \\       /
         -----

    """)
    t.sleep(0.5)
    print(f"""
         -----
       /       \\
      /         \\
     |     {u_lotto[3]}    |
      \\         /
       \\       /
         -----

    """)
    t.sleep(0.5)
    print(f"""
         -----
       /       \\
      /         \\
     |     {u_lotto[4]}    |
      \\         /
       \\       /
         -----

    """)
    t.sleep(0.5)
    print(f"""
         -----
       /       \\
      /         \\
     |     {u_lotto[5]}    |
      \\         /
       \\       /
         -----

    """)
    t.sleep(2)

    print("여기 있습니다. ^0^")

    print(f"""
    -------------------------
    |{u_lotto}|
    -------------------------
    """)

    t.sleep(1)
    print("_____________________________")
    money -= 10000
    print()
    print(f"잔액은 {money}입니다. (*^_^*)")
    print()

    print("당첨 결과를 알고 싶다면 1, 알고 싶지 않다면 2를 눌러주세요")

    u_choice = int(input())

    if u_choice == 1:
        co1 = 0
        co2 = 0
        co3 = 0
        co4 = 0
        co5 = 0
        co6 = 0

        prize = 0


        if u_lotto[0] in co_lotto:
            co1 = 1
        if u_lotto[1] in co_lotto:
            co2 = 1
        if u_lotto[2] in co_lotto:
            co3 = 1
        if u_lotto[3] in co_lotto:
            co4 = 1
        if u_lotto[4] in co_lotto:
            co5 = 1
        if u_lotto[5] in co_lotto:
            co6 = 1
        co_l = [co1, co2, co3, co4, co5, co6]

        if int(co_l.count(1)) == 6:
            prize = 1
            money += 1,987,426,822
        elif int(co_l.count(1)) == 5 and b_lotto==co_b_lotto:
            prize = 2
            money += 81,356,654
        elif int(co_l.count(1)) == 5:
            prize = 3
            money += 1,579,472
        elif int(co_l.count(1)) == 4:
            prize = 4
            money += 50,000
        elif int(co_l.count(1)) == 3:
            prize = 5
            money += 5000

        print()
        print()
        if prize!=0:
            print(f"""
            _______________

            \\\\((*^3^*))//
            {prize}등입니다!!
            :>>>>>>>>>>>>>

            ---------------
            """)
        else :
            print("""
            -------------------

            //(( ㅠ _ ㅠ ))\\\\
            다음 기회를 노리세요 :(

            -------------------    
            """)
        
        t.sleep(2)
        print()
        print(f"당첨번호는 {co_lotto},\n당신의 번호는 {u_lotto}입니다.")
        print()
        print(f"잔액은 {money}원입니다.")
        # print(co_l)
        t.sleep(1)
        print()
        print("안녕히 가세요")

    else:
        print("안녕히 가세요")
        

else :
    print("저희 가게는 만원을 주셔야 합니다. 안녕히 가세요.")
