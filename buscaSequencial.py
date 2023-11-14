
A = [2,5,4,9]
x = 7
n = len(A)

def ordenar(A, x):
    i = 1
    while i <= n  and A[i] != x:
        i += 1
    if i <= n: return print(i)
    else: return print("-1")
    
ordenar(A, x)