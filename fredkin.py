def fredkin(c, a1, a2):
    if c == 0:
        b1 = a2
        b2 = a1
    else:
        b1 = a1
        b2 = a2
    return c, b1, b2
