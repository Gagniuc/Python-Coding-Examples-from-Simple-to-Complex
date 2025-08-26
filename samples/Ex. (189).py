a = {}
b = [3, 6, 2, 78, 99, 1, 4]

r = 0
n = len(b)

for i in range(n):
    a[b[i]] = b[i]

m = max(a.keys()) + 1

for j in range(m):
    if j in a:
        b[r] = a[j]
        r += 1

print(b)

'''
Ex. (189) - Low level native sort and eliminate duplicates (I).

References

Paul A. Gagniuc. Coding Examples from Simple to Complex - Applications in Python, Springer, 2024, pp. 1-245.
Paul A. Gagniuc. Coding Examples from Simple to Complex - Applications in MATLAB, Springer, 2024, pp. 1-255.
Paul A. Gagniuc. Coding Examples from Simple to Complex - Applications in Javascript, Springer, 2024, pp. 1-240.

'''


