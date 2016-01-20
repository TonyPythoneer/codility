def solution(A):
    # write your code in Python 2.7
    left = 0
    right = sum(A)
    min_ = float("inf")
    for index in range(len(A)-1):
        left += A[index]
        right -= A[index]
        diff = abs(left-right)
        if diff < min_:
            min_ = diff
    return min_
