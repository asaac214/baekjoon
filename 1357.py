def REV(k):
    k = str(k)
    k = k[::-1]
    k = int(k)
    return k


x, y = map(int, input().split())

print(REV(REV(x) + REV(y)))
