T = int(input())
c = 'cubelover'
k = 'koosaga'

for i in range(T):
    N = int(input())
    if N == 1:
        print(k)
    if N == 2:
        print(c)
    if N == 3:
        print(k)
    if N == 4:
        print(c)
    elif N!=1 and N!=2 and N!=3 and N!=4:
        print('모르겠어요..')
