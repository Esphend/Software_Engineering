from math import sqrt
def Heron(a, b, c):
    P = (a+b+c)/2
    S = sqrt(P*(P-a)*(P-b)*(P-c))
    print(S)

