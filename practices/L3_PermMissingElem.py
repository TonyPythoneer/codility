def solution(A):
    # write your code in Python 2.7
    A.sort()
    pointer = 1
    index = 0
    for e in A:
        if e != pointer:
            break
        pointer += 1
        index += 1
    return pointer
