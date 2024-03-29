x1, y1, x2, y2 = map(float, input().split())
x3, y3, x4, y4 = map(float, input().split())

if x2 < x3 or x1 > x4 or y2 < y3 or y1 > y4:
    print("Прямоугольники лежат вне друг друга, не касаясь")
elif x2 == x3 or x1 == x4 or y2 == y3 or y1 == y4:
    print("Прямоугольники имеют касание")
elif x2 > x3 and x1 < x4 and y2 > y3 and y1 < y4:
    print("Один прямоугольник лежит внутри другого, не касаясь")
else:
    print("Прямоугольники имеют пересечение")