import classZip as cz

class Bu_hae(cz.Bang):
    def __init__(self):
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        super().__init__(a, b, c)

a = Bu_hae()
print(a.fun_1())