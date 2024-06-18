import cmath

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
        small = ((-self.b+cmath.sqrt(self.b**2-4*self.a*self.c))/2*self.a)
        big =  ((-self.b-cmath.sqrt(self.b**2-4*self.a*self.c))/2*self.a)
        return (small, big)




# 자식 클래스들
class Bang_hae(Bang):
    pass


class Bang_pan(Pan):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)


class Ham_hae(Bang):
    pass

class Ham_pan(Pan):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

class Ham_gragh:
    pass

class Ham_minmax:
    pass

class Bu_hae(Bang):
    pass

class Bu_ver:
    pass


def again():
    answer = input("다시 하시겠습니까?  y/n\n")
    return answer