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
            small = ((-self.b)/(2*self.a)+(s1*-1)/2*self.a)
            big =  ((-self.b)/(2*self.a)-(s1*-1)/2*self.a)
        else:
            small = ((-self.b)//(2*self.a)+(math.sqrt(D))//2*self.a)
            big =  ((-self.b)//(2*self.a)-(math.sqrt(D))//2*self.a)
        return small,big

    #     small = ((-self.b+math.sqrt(self.b**2-4*self.a*self.c))/2*self.a)
    #     big =  ((-self.b-(math.sqrt(self.b**2-4*self.a*self.c)))/2*self.a)
    #     return (small, big)


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
    pass

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
