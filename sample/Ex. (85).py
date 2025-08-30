a = [5, 2, 8, 4, 6, 22, 8, 9]

m = 15
t = ''
max_value = 0

n = len(a)

for i in range(n):
    if a[i] > max_value:
        max_value = a[i]

for i in range(n):
    
    f = int((m / max_value) * a[i])
    
    for k in range(m):
        
        if k < f:
            t += '▮'
        else:
            t += '▯'

    t += '\n'

print(t)

'''
Ex. (85) - Horizontal chart with UTF characters proportional with max array.

References

Paul A. Gagniuc. Coding Examples from Simple to Complex - Applications in Python, Springer, 2024, pp. 1-245.
Paul A. Gagniuc. Coding Examples from Simple to Complex - Applications in MATLAB, Springer, 2024, pp. 1-255.
Paul A. Gagniuc. Coding Examples from Simple to Complex - Applications in Javascript, Springer, 2024, pp. 1-240.

'''


