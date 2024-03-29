s = input()
a = s.split('x')
if (int(a[0]) ** 2 + int(a[1]) ** 2) ** 0.5 <= 13:
    print('да')
else:
    print('нет')

