import math

# 부모 클래스들
class Pan: # 판별식 구하기
    def __init__(self, a, b, c) : #a,b,c 정의
        self.a = a
        self.b = b
        self.c = c

    D = 0
    def d_Pan(self):
        D=((self.b**2-(4*self.a*self.c)))
        return D

# 방정식 계산이 방정식과, 함수, 부등식에 모두 사용됨.
class Bang:  # 방정식 계산
    def __init__(self, a, b, c) : #a,b,c 정의
        self.a = a
        self.b = b
        self.c = c

    def fun_1(self):
        D = Pan.d_Pan(self) # 판별식 해(근)구하기
        if D<0:
            D=D*-1
            s1=math.sqrt(D)
            small = (((-self.b)+(s1*(-1)))/2*self.a)
            big =  (((-self.b)-(s1*(-1)))/2*self.a)
        else:
            small = (((-self.b)+(math.sqrt(D)))/2*self.a)
            big =  (((-self.b)-(math.sqrt(D)))/2*self.a)

        return (small,big)

# 다양한 기능을 하는 함수들

def again(): # 프로그램을 다시 사용할 것인지 질문하고 그 값을 반환하는 함수
    answer = input("\n다시 하시겠습니까?  y/n\n")
    return answer

def puli(): # 풀이를 볼건지 질문하고 그 값을 반환하는 함수
    answer = input("\n풀이를 원하시면 y, 답만 원하시면 n을 입력하세요. y/n\n")
    return answer

def answer_print(): # 정답이 더 잘 보이도록 강조해줄 함수
    print("-"*40)

def des(): # 사용자에게 무엇을 입력해야할지 알려주는 함수
    print("\n'ax² + bx + c = 0' 의 형태입니다. \n a, b, c를 차례대로 입력해주세요. \n")

def des_bu(): # 사용자에게 무엇을 입력해야할지 알려주는 함수 (부등식에서)
    print("\n'ax² + bx + c (입력받은 부등호 기호) 0' 의 형태입니다. \n a, b, c, 부등호 기호('>' or '>=' or '<' or '<=')를 차례대로 입력해주세요. \n")