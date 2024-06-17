import cmath

# 부모 클래스들
class Pan:
    def __init__(self, a, b, c) :
        self.a = a
        self.b = b
        self.c = c

    D = 0
    def fun_D_Pan(self, D):
        D=((self.b**2-(4*self.a*self.c)))
        return D

# 방정식 계산이 방정식과, 함수, 부등식에 모두 사용됨.
class Ban: 
    def __init__(self, a, b, c) :
        self.a = a
        self.b = b
        self.c = c

    def fun_1(self):
        small = ((-self.b+cmath.sqrt(self.b**2-4*self.a*self.c))/2*self.a)
        big =  ((-self.b-cmath.sqrt(self.b**2-4*self.a*self.c))/2*self.a)
        return (small, big)




# 자식 클래스들
class Bang_hae:
    pass

class Bang_pan(Pan):
    pass

class Ham_hae(Ban):
    pass

class Ham_pan(Pan):
    pass

class Ham_gragh:
    pass

class Ham_minmax:
    pass

class Bu_hae(Ban):
    pass

class Bu_ver:
    pass

test = Ban(1,3,2)
print(test.fun_1())