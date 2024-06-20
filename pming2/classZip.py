import math

# 부모 클래스들
class Pan:
    def __init__(self, a, b, c) :
        self.a = a
        self.b = b
        self.c = c

    D = 0
    def d_Pan(self):
        D=((self.b**2-(4*self.a*self.c)))
        return D

# 방정식 계산이 방정식과, 함수, 부등식에 모두 사용됨.
class Bang: 
    def __init__(self, a, b, c) :
        self.a = a
        self.b = b
        self.c = c

    def fun_1(self):
        D = Pan.d_Pan(self)
        if D<0:
            D=D*-1
            s1=math.sqrt(D)
            small = (((-self.b)+(s1*(-1)))/2*self.a)
            big =  (((-self.b)-(s1*(-1)))/2*self.a)
        else:
            small = (((-self.b)+(math.sqrt(D)))/2*self.a)
            big =  (((-self.b)-(math.sqrt(D)))/2*self.a)

        # print(small, big)
        return (small,big)

        # big = ((-self.b+math.sqrt(self.b**2-4*self.a*self.c))/2*self.a)
        # small =  ((-self.b-(math.sqrt(self.b**2-4*self.a*self.c)))/2*self.a)
        # return (small, big)


# 자식 클래스들

# 옮김.
class Bang_hae(Bang):
    def __init__(self):
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        super().__init__(a, b, c)


# 옮김.
class Bang_pan(Pan):
    def __init__(self):
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        super().__init__(a, b, c)


class Ham_hae(Bang):
    pass

class Ham_pan(Pan):
    def __init__(self):
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        super().__init__(a, b, c)

# class Ham_gragh:
#     pass

class Ham_minmax:
    def find_maximum(self):
        D = Pan.d_Pan(self)
        a=float(input("a: "))
        b=float(input("b: "))
        c=float(input("c: "))
        g_max= -b / (2 * a)  # 공식을 이용해 구함: x = -b / (2*a)
        g_min = a * g_max**2 + b * g_max + c  # 정점에서의 최댓값을 계산함: y = ax^2 + bx + c
        if D>0:
            return g_min
        
        elif D<0:
            return g_max

        else:
            print("다시 입력하여 주세요")

        # if D>0:
        #     print(D)
        #     print("최솟값")
        #     return g_min
        # elif D<0:
        #     print(D)
        #     print("최댓값")
        #     return g_max

        # else:
        #     print("다시 입력하여 주세요")

# 옮김
class Bu_hae(Bang):
    def __init__(self):
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        super().__init__(a, b, c)

# 수직선
class Bu_ver:
    pass


def again():
    answer = input("다시 하시겠습니까?  y/n\n")
    return answer

def puli():
    answer = input("\n풀이를 원하시면 y, 답만 원하시면 n을 입력하세요. y/n\n")
    return answer

def answer_print():
    print("-"*40)

def des():
    print("\n'ax² + bx + c = 0' 의 형태입니다. \n a, b, c를 차례대로 입력해주세요. \n")

def des_bu():
    print("\n'ax² + bx + c (입력받은 부등호 기호) 0' 의 형태입니다. \n a, b, c를 차례대로 입력해주세요. \n")