

def factor(n):
    if n == 1:
        return n
    return n * factor(n-1)


sam = factor(5)
print(sam)