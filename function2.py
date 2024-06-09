def prime(n):
    if n in [2,3]:
        return True
    if (n==1) or (n%2==0):
        return False
    r=3
    while r * r <=n:
        if n%r==0:
            return False
        r=r+2
    return True
print(prime(78), prime(79))