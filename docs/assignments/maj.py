def R(A):
    B = []
    i = 0
    while i < len(A):
        a = A[i]
        b = A[(i+1) % len(A)]
        if a == b:
            B.append(a)
        i += 1
    return B

def maj(A):
    prev = A
    curr = R(A)
    while len(curr) != len(prev):
        prev = curr
        curr = R(curr)
    return curr[0]
