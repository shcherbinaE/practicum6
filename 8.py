import math
n = int(input())
if n <= 10:
    print(n - 1)
elif n <= 190:
    num = math.ceil((n - 10) / 2) + 9
    if n % 2 == 0:
        print(num % 10)
    else:
        print(num // 10)
else:
    num = math.ceil((n - 190) / 3) + 189
    if n % 3 == 0:
        print(num % 10)
    elif n % 3 == 1:
        print(num % 100 // 10)
    else:
        print(num // 100)


