def lab(a):
    s = 0
    for i in range(0, len(a), 1):
        s = s + a[i]
    print(s / len(a))


a = [1, 4, 7, 10, 11, 14, 6, 8, 9]
lab(a)