n, k, m = map(int, input().split())
sessions = n * 2 // k
if n * 2 % k != 0:
    sessions += 1
if sessions == 1:
    sessions = 2
print(sessions * m)