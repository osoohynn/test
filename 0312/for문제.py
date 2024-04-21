n = int(input())
r = 0

if n >=180 :
    r = 4
elif n >= 170:
    r = 5
elif n >= 160:
    r = 6
else:
    r = 7

for i in range(1, r+1):
    print("""|  |        |  |
|  |________|  |
|   ________   |
|  |        |  |""")
