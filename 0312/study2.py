city = 'daegu'
name = 'suhyun'
id = 1234
pw = 'a'
tem = 21.66666
# print("아이디 '%07d' 비밀번호 '%05c' 인 %s님이 거주하신곳은 %s로 온도가 %d입니다." %(1234, pw, name, city, tem))

# print("저의 이름은 {1}입니다. 그리고 나이는 {age}살이고 키는 {0:.1f}cm입니다. 내 꿈은 {name}입니다.".format(181.350001, "대소고",122, height = 181.25, age = 17, name = "개발자"))

a = 1
b = 3
c = "정사각형"
# print(f"가로{a}, 높이{b}인 {c}의 넓이는{a*b/2:20.6f} 입니다.")
d = [1]
if bool(d) == True:
    print('t')
else:
    print('f')

for a in range(10):
    for b in range(10):
        for c in range(10):
            if (a*100+b*10+c)-(a*10+b)==(c*10+c) and a !=b != c:
                print(f"{a}{b}{c}-{a}{b}={c}{c}")

score = 70
# print("PASS") if score >= 80 else print("RETEST")

numbers = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]

#값만 삭제
numbers[3] = ""
# print(numbers)

numbers = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]

a = "goorm"

city = ["서울", "대전", "대구", "부산"]
sale = [80, 60, 22, 50, 75]

# for i,j in enumerate(city) :
	# print(i)

d = [x for x in range(13)]
# print(*d)

d = list(x for x in range(12) if x>5)
# print(d)

# str_a = ['1', '2', '3']
# int_a = [int(i) for i in str_a]
# print(int_a)

dic = dict(apple='사과', b=122, aple=1200)
# dic[0,] = 1
# print(dic)

# print(sorted(dic))
# print(dic.get('appl'))

# del dic
dic.clear()
# print(dic)

t1 = ('a', 'b', 'c', 1, 2, 3)
t2 = ("hello",)
t3 = "goorm", 'b', "hello", 1, 2, 3

# print(t1 + t2 + t3) # 튜플 결합
# print(t2 * t3[4]) # 곱셈으로 반복 출력

s1 = {1,2,3}
s1.update("123")
# print(s1)

def func(**kwargs) :
    print(kwargs)
    
num = 10
func(apple="사과", a = num, n = [1,2,4])

class Triangle :
    def setData(self, b, h=5) :
        self.b = b
        self.h = h
                
    def area(self) :
        return self.b * self.h / 2

tri1 = Triangle()
tri1.setData(4)

tri2 = Triangle()
tri2.setData(6, 10)

print(tri1.b, tri1.h, tri1.area())
print(tri2.b, tri2.h, tri2.area())

a = 30
print('-'*20)
print(f"{10/3:!^10.2f}")
print(f"{10/3:.2f}")


j = 5
del id
print(id(j))

print(f"{a:!>10}")

def mul(n):
    if n == 1:
        return 1
    return n * mul(n-1)

# n = int(input())
# print(mul(n))

def func(a,b, *kwargs) :
    print(kwargs)
    print(a, b)
    
num = 10
func(1, 'apple',342,35345,34)

del a
del b
del c

print('-'*20)

a = 10
b = a
c = 10
print(id(a), id(b), id(c))
a = 20
print(id(a), id(b))
print(b)

a = [1,2]
b = a
a.append(3)
print(b)