def interS(l1, l2):
    s1 = set(l1)
    s2 = set(l2)
    return list(s1.intersection(s2)) # set.intersection 사용

l1 = [45, 5, 22, 31, 7, 19]
l2 = [2, 1, 5, 22, 7, 38, 27, 19, 13, 41]

print(interS(l1, l2))
