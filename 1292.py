arr = [0]*1000

sum = 0
ai = 0
for i in range(1000):
    for j in range(i+1):
        arr[ai] = i+1
        ai += 1
        if ai == 1000:
            break
    if ai == 1000:
        break

a, b = map(int, input().split())

for i in range(a-1, b):
    sum += arr[i]

print(sum)
