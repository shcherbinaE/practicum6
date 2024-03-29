def possibility(k):
    if k % 5 == 0 or k % 7 == 0:
        return True
    for i in range(0, k//5 + 1):
        if (k - i*5) % 7 == 0:
            return True
    return False

k = int(input())
if possibility(k):
    print('да')
else:
    print('нет')