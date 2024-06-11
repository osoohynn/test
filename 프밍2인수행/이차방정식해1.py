import cmath
while True:
    while True:
        try:
            a = float (input ("Input a : "))
            break 
        except:
            print("Please try again...")

    while True:
        try:
            b = float (input ("Input b : "))
            break
        except:
            print("Please try again...")
    while True:
        try:
            c = float (input ("Input c : "))
            break 
        except:
            print("Please try again...")
    if a==0 :
        print("a is not supposed to be zero. Try again!!!")
        continue 
    else:
        break

d = (b ** 2) - (4*a*c)
answer1 = (-b - cmath.sqrt(d)) / (2*a)
answer2 = (-b + cmath.sqrt(d)) / (2*a)
print ('The solutions are {0} and{1}'. format (answer1, answer2))