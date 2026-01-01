from decimal import Decimal, getcontext
a=int(input("Please Enter You Want Precision:"))
def chudnovsky_pi(precision):
    getcontext().prec = precision + 2
    C = 426880 * Decimal(10005).sqrt()
    K, M, X, L, S = 6, 1, 1, 13591409, 13591409
    for k in range(1, precision//14 + 2):
        M = M * (K**3 - 16*K) // (k**3)
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
        K += 12
    return C / S
print(chudnovsky_pi(100)) 
