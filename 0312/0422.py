'''n = int(input())

# for i in range(n-1):
#     print('*')


for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1:
            print('*', end="")
        else:
            print(' ', end="")
    print()'''

#다이아 a 하트 b 세모 c 별 d ㅔㄴ모 e

for a in range(10):
    for b in range(10):
        for c in  range(10):
            for d in range(10):
                for e in range(10):
                    if (a*100+b*10+b)+(b*100+c*10+d)+(e*100+c*10+b)==(d*100+d*10+a) and a !=b and a != c and a !=d and a != e and b !=c and b != d and b !=e and c != d and c !=e and d != e:
                        print(f"{a}{b}{b}+{b}{c}{d}+{e}{c}{b}={d}{d}{a}")
                        print(a,b,c,d,e)