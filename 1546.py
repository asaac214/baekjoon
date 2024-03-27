num = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

S = 0
avg = [0 for i in range(1000)]
for i in range(num):
    avg[i] = a[i]/a[0]*100
for i in range(num):
    S += avg[i]
S /= num
print(S)
