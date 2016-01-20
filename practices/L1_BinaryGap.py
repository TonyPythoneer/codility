def solution(N):
    _ , t = str(bin(N)).split('b')
    gaps = 0
    start = 0
    for i in xrange(1, t.count('1')-1):
        a_pos = t.index('1', start)
        b_pos = t.index('1', a_pos+1)
        start = a_pos+1
        print a_pos, b_pos
        diff = b_pos - a_pos - 1
        if diff > gaps:
            print a_pos, b_pos
            gaps = diff
    return gaps
