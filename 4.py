s = input()
if (ord(s[0]) - ord('a') + int(s[1])) % 2 == 1:
    print('черный')
else:
    print('белый')