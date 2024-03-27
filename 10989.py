import sys
length = int(input())
a = [0]*10001
for i in range(length):
    inp = int(sys.stdin.readline())
    a[inp] = a[inp] + 1

for i in range(10001):
    if a[i] != 0:
        for j in range(a[i]):
            print(i)
