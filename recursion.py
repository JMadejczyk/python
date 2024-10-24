cache = {1: 1}

def a(n, cache):
    if n in cache:
        return cache[n]
    elif n not in cache:
        cache[n] = (1 + a(n+1-a(a(n))))
        return cache[n]
    