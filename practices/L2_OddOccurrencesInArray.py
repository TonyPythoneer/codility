def solution(A):
    # write your code in Python 2.7
    counter = {}
    for e in A:
        if e not in counter:
            counter[e] = 1
        else:
            counter[e] += 1
    unpair = 0
    for k,v in counter.items():
        if v % 2 == 1:
            if k > unpair:
                unpair = k
    return unpair


#
def solution(A):
    # write your code in Python 2.7
    unpair = 0
    while A:
        e = A.pop(0)
        try:
            index = A.index(e)
            A.pop(index)
        except IndexError:
            if e > unpair:
                unpair = e
    return unpair
