s = input()
if abs(ord(s[0]) - ord(s[3])) == 2 and abs(int(s[1]) - int(s[4])) == 1 or abs(ord(s[0]) - ord(s[3])) == 1 and abs(int(s[1]) - int(s[4])) == 2:
    print('верно')
else:
    print('ошибка')