def compute(x):
    return x + x / x - x * x

def distribution(start, stop):
    t = ""
    for i in range(start, stop):
        t += str(compute(i)) + "\n"
    return t

a = distribution(3, 21)
print(a)

'''
Ex. (140) - A simple scanner to find the output distribution.

References

Paul A. Gagniuc. Coding Examples from Simple to Complex - Applications in Python, Springer, 2024, pp. 1-245.
Paul A. Gagniuc. Coding Examples from Simple to Complex - Applications in MATLAB, Springer, 2024, pp. 1-255.
Paul A. Gagniuc. Coding Examples from Simple to Complex - Applications in Javascript, Springer, 2024, pp. 1-240.

'''


