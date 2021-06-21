n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))


candi = []
for i in range(1, 1001):
    for j in range(m):
        try:
            value = [b[j + i * k] for k in range(n)]
            if value == a:
                candi.append(i)
        except:
            pass

if len(candi) == 0:
    print(-1)
else:
    print(min(candi) - 1, max(candi) - 1)
