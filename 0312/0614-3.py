'''num1, num2= map(int, input().split())
try:
    result = num1/num2
    print(f'연산결과는 {result}입니다.')
except:
    print('에러가 발생했어요.')
else:
    print('정상동작 했어요.')
finally:
    print('수행종료 합니다.')'''
#4 2 입력 결과
#연산결과는 2.0입니다.
#정상동작 했어요.
#수행종료 합니다.

#1 0 입력결과 <-에러발생
#에러가 발생했어요.
#수행종료 합니다.
'''
try:
    10 / 0
except ZeroDivisionError as e:
    print(e)
'''
try:
    10 / '0'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)