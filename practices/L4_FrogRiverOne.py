def solution(X, A):
    # write your code in Python 2.7
    steps = X
    leaves = {}
    for i, e in enumerate(A):
        if e not in leaves:
            leaves[e] = None
            steps -= 1
        if steps == 0:
            return i
    return -1
