def transform():
    size = 128000

    a = 2.0
    b = 0.5
    c = 0.1
    d = 0.5
    e = 2.0
    f = 0.1

    data = []
    s = 0.0
    for i in xrange(size):
        x = i
        y = i
        X = a*x + c*y + e
        Y = b*x + d*y + f
        data.append((X, Y))
        s += X

    return s
