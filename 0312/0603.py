# n, h = map(int,input().split())

# print(n*h/2)


# def area(b, h):
#     print(b*h/2)
print('<삼각형 클래스>')
print()

class Triangle: #클래스를 만드는 코드
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        print(self.b*self.h/2)

 #객체를 생성하는 코드
b=1
h=2
a1 = Triangle(b,h)
a1.area()
print(a1.h)
a2 = Triangle(3,4)
a2.area()

print()
print('<챔피언 클래스>')
print()

class Champion:
    def setData(self, name, hp, dmg, mo):
        self.name = name
        self.hp = hp
        self.dmg = dmg 
        self.mo = mo
    def lmove(self):
        print(f'{self.name}가 왼쪽으로 한칸 이동했습니다.')
    def attack(self):
        print(f"{self.name}가 재민이에게 {self.dmg}만큼 피해를 입힘")

colt = Champion()
colt.setData('콜트', 1000, 100, 3)

salley = Champion()
salley.setData('셀리', 1200, 100, 3)

salley.attack()
salley.lmove()
colt.attack()

print()
print('<이닛 배우기>')
print()

class Champion:
    def __init__(self, name, hp, dmg, mo):
        #무조건 바로 실행됨
        self.name = name
        self.hp = hp
        self.dmg = dmg 
        self.mo = mo
    def lmove(self):
        print(f'{self.name}가 왼쪽으로 한칸 이동했습니다.')
    def attack(self):
        print(f"{self.name}가 재민이에게 {self.dmg}만큼 피해를 입힘")

colt = Champion('콜트', 1000, 100, 3)
                #객체를 생성함과 동시에 매개변수를 넣어줌

salley = Champion('셀리', 1200, 100, 3)

salley.attack()
salley.lmove()
colt.attack()

print()
print('<클래스 변수>')
print()

class Triangle :
    height = 10
    bottom = 4

tri1 = Triangle()
tri2 = Triangle()

Triangle.height = 5

print(tri1.height)
print(tri2.height)

