import math
def f(x):
    result = 3*x-math.cos(x)-1
    return result

rootList = []

def checkingRoot(presentRoot):
    for root in rootList:
        if(root==presentRoot):
            return True
    return False
        
def bisectionMethod(a,b):
    i = 1
    while True:
        c = round(((a+b)/2), 4)
        print(f'Iteration {i}:   a={a}  f(a)={f(a)}    b={b}    f(b)={f(b)}   c={c}    f(c)={f(c)}')
        if checkingRoot(c):
            print("The Root is: ", c)
            quit()
        rootList.append(c)
        if(f(a)*f(c)<=0):
            b = c
        else:
            a = c
        i+=1
        if(i==20):
            break
        
a = float(input("Enter the first number a: "))
b = float(input("Enter the second number b: "))

if(f(a)*f(b)<0):
    bisectionMethod(a,b)
else:
    print(f'Result of f(a)*f(b) = {f(a)*f(b)}')
    print("Your assumption is Wrong")
