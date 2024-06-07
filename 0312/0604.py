class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def displayInfo(self):
        print(f"This car is a {self.make} {self.model}.")

car1 = Car("Toyota", "Corolla")
car1.displayInfo()
car2 = Car("Hyundae", "산타페")
car2.displayInfo()

print("-"*30)

class Book:
    cnt = 0
    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.cnt += 1
    def getSummary(self):
        print(f"{self.title} by {self.author}")

book1 = Book("해리포터", "조앤K.롤링")
book1.getSummary()
print(Book.cnt)
book2 = Book("해리포타", "조앤K.롤릴")
book2.getSummary()
print(Book.cnt)
print("-"*30)

class Student:
    std = []
    def __init__(self, num, name, kor, mat, eng):
        self.num = num
        self.name = name
        self.kor = kor
        self.mat = mat
        self.eng = eng
        Student.std.append(self)
        # Student.std.append(self.kor)
    def avg(self):
        print(f"{self.num}{self.name}의 평균은 {(self.kor+self.eng+self.mat)/3}점입니다.")

hunchun = Student(1301, "권헌춘", 50, 87, 94)
hunchun.avg()

std1 = Student(1319, "kkk", 90, 87, 64)
hunchun.avg()

std2 = Student(1320, "jjj", 81, 82, 74)
hunchun.avg()

print(Student.std)
a = [x.kor for x in Student.std]
print(a)

print("-"*30)

class Triangle : 
    cal_count = 0
    
    def __init__(self, b, h = 5) :
        self.b = b
        self.h = h
        
    def area(self) :
        Triangle.cal_count += 1
        return self.b * self.h / 2

    @staticmethod
    def isIsosceles(a, b) :
        Triangle.cal_count += 1
        return a == b    

tri1 = Triangle(4) #밑변 4 삼각형 객체 생성

print(tri1.b, tri1.h, tri1.area(), tri1.cal_count)
print(tri1.isIsosceles(5,5), tri1.cal_count)
print(Triangle.isIsosceles(5,4), tri1.cal_count)

print("-"*30)

