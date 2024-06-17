f = open("aaa/test3.txt", "w")
for i in range(4):
    a = input()
    f.write(a+"\n")
f.close()

f = open("aaa/test3.txt", "r")
# a = f.read()
# print(a)

for i in range(1,5):
    a = f.readline().split()
    b = list(map(int, a[1:]))
    print(f"{a[0]} {sum(b)/len(b):.2f}")
    
f.close()