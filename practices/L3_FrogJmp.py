def solution(X, Y, D):
    last_distance = (Y - X) % D
    extra_step = 1 if last_distance != 0 else 0
    return (Y - X) / D + extra_step
