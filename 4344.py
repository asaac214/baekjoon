num = int(input())

for i in range(num):
    sum = 0
    student = 0
    a = list(map(int, input().split()))
    for j in range(1, a[0]+1):
        sum += a[j]
    avg = sum/a[0]
    for k in range(1, a[0]+1):
        if a[k] > avg:
            student += 1
    print("%.3f%%" % (student/a[0]*100))
