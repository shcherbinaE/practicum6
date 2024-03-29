s = input()
a = s.split('x')
k = int(input())
if k / int(a[0]) <= int(a[1]) and k % int(a[0]) == 0 or k / int(a[1]) <= int(a[0]) and k % int(a[1]) == 0:
    print('успешно')
else:
    print('неосуществимо')