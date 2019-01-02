import math

a = 0.5
b = 1.5
tol = math.pow(10, -3)

def f(x):
    return 2 + math.cos(math.exp(x) - 2) - math.exp(x)

def sign(x):
    return x > 0

n = 1
while n <= 10:
    c = (a+b)/2
    if f(c) == 0:
        print("error tolernece reached: f(c) = 0")
        break

    if((b-a)/2 < tol):
        print(f'error tolerance reached: (b-a)/2 = {(b-a)/2}')
        break

    print(f'Iteration {n}:')
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')
    print(f'f(c) = {f(c)}')

    n += 1
    if sign(f(c)) == sign(f(a)):
        a = c

    else:
        b = c

    