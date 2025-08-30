import random

a = [0] * 9
n = 9

for k in range(n):
    a[k] = random.randint(0, 99)

def chart(a):
    m = 9
    t = [['' for _ in range(n)] for _ in range(m)]

    # Use default=1 to avoid 
    # division by zero.

    max_val = max(a, default=1)

    for j in range(m):
        for i in range(n):

            f = int((m / max_val) * a[i])
            t[m - j - 1][i] = '\u2591'

            if j < f:
                t[m - j - 1][i] = '\u2593'
    
    return t

def SMC(a):
    n = len(a)
    m = len(a[0])
    r = ''
    
    for i in range(n + 2):
        for j in range(m):
            if i < n:
                r += a[i][j]
            if i == n:
                r += '|'
            if i > n:
                r += str(j + 1)
        if i == n:
            r += '\n'
        if i < n:
            r += "_" + str(n - i) + "\n"
    
    return r

print(SMC(chart(a)))
print('\n' + str(a))

'''
Ex. (198) - Vertical chart from array with random values at each run.

References

Paul A. Gagniuc. Coding Examples from Simple to Complex - Applications in Python, Springer, 2024, pp. 1-245.
Paul A. Gagniuc. Coding Examples from Simple to Complex - Applications in MATLAB, Springer, 2024, pp. 1-255.
Paul A. Gagniuc. Coding Examples from Simple to Complex - Applications in Javascript, Springer, 2024, pp. 1-240.

'''


