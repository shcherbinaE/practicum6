s = input()
a = s.split('x')
s = input()
r = s.split('x')
if (int(a[0]) ** 2 + int(a[1]) ** 2) ** 0.5 >= min((int(r[0]) ** 2 + int(r[1]) ** 2) ** 0.5, (int(r[1]) ** 2 + int(r[2]) ** 2) ** 0.5, (int(r[0]) ** 2 + int(r[2]) ** 2) ** 0.5):
    print('да')
else:
    print('нет')