def umax1(A):
    """Our first attempt at solving the unique maximum problem.
    According to 2(b), it has a bug.
    """
    if len(A) == 1:
        return A[0]
    head = A[0]
    tail = A[1:]
    tmax = umax1(tail)
    if head == tmax:
        return -1
    elif head > tmax:
        return head
    else:
        return tmax

def umax2(A):
    """Our second attempt. This is the version you must prove the correctness
    of in question 2(c).
    """
    if len(A) == 1:
        return A[0]
    head = A[0]
    tail = A[1:]
    tmax = umax2(tail)
    if head == tmax:
        return -1 * head
    elif head > abs(tmax):
        return head
    else:
        return tmax
