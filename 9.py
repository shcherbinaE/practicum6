x1, y1, r1 = map(float,input().split())
x2, y2, r2 = map(float,input().split())

dist_centers = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
sum_radius = r1 + r2
diff_radius = abs(r1 - r2)

if dist_centers > sum_radius:
    print("Окружности лежат одна вне другой, не касаясь.")
elif dist_centers == sum_radius:
    print("Окружности имеют внешнее касание.")
elif sum_radius > dist_centers > diff_radius:
    print("Окружности пересекаются.")
elif dist_centers == diff_radius:
    print("Окружности имеют внутреннее касание.")
elif dist_centers < diff_radius:
    print("Одна окружность лежит внутри другой, не касаясь.")
