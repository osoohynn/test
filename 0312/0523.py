
'''arr = [-1]*100
def fibo(n):
    if arr[n]!=-1:
        return arr[n]
    # if n == 1:
    #     return 1
    # if n==2:
    #     return 1
    arr[n] = fibo(n-1) + fibo(n-2)
    return arr[n]
    #메모이제이션

arr[1]=1
arr[2]=1

print(fibo(int(input())))'''

'''def f(n):
    if n == 1:
        return 1
    return n * f(n-1)

print(f(int(input())))'''

def f(a, b):
    if b==1:
        return 1
    if a==b:
        return 1
    if a < b:
        return 0
    return f(a-1,b-1)+f(a-1,b)

a, b = map(int, input().split())
print(f(a, b))