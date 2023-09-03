a = eval(input())

x1 = float(a[0][0])
y1 = float(a[0][1])
x2 = float(a[1][0])
y2 = float(a[1][1])
x3 = float(a[2][0])
y3 = float(a[2][1])
x4 = float(a[3][0])
y4 = float(a[3][1])
if min(y1, y2, y3, y4) >= 0:
    #three sides facing the x-axis
    #the shape is tilted towards right
    area_of_shape = (-(x1*y2+x2*y3+x3*y4+x4*y1)+(x2*y1+x3*y2+x4*y3+x1*y4))/2
    if x1<x3<=x4<x2 or x1<x4<=x3<x2:
        if y3<y4<=y2<y1 or y3<=y4<y2<=y1 or y3<y4<=y1<y2 or y2<=y3<y4<y1 or y3<y1<=y4<y2:
            area = (x2-x1)*(y2+y1)/2 -area_of_shape

    if x4<x2<=x3<x1 or x4<x3<=x2<x1:
        if y2<y3<=y1<y4 or y2<=y3<y1<=y4 or y2<y3<=y4<y1 or y1<=y2<y3<y4 or y2<y4<=y3<y1:
            area = (x1-x4)*(y1+y4)/2 -area_of_shape

    if x3<x1<=x2<x4 or x3<x2<=x1<x4:
        if y1<y2<=y4<y3 or y1<=y2<y4<=y3 or y1<y2<=y3<y4 or y4<=y1<y2<y3 or y1<y3<=y2<y4:
            area = (x4-x3)*(y4+y3)/2 -area_of_shape

    if x2<x4<=x1<x3 or x2<x1<=x4<x3:
        if y4<y1<=y3<y2 or y4<=y1<y3<=y2 or y4<y1<=y2<y3 or y3<=y4<y1<y2 or y4<y2<=y1<y3:
            area = (x3-x2)*(y3+y2)/2 -area_of_shape
    #the shape is tilted towards left
    if x1<x4<=x3<x2 or x1<x3<=x4<x2:
        if y4<y3<=y2<y1 or y4<y3<=y1<y2 or y4<=y3<y1<=y2 or y4<=y1<y3<y2 or y4<y2<=y3<y1:
            area = (x2-x1)*(y2+y1)/2 -area_of_shape

    if x4<x3<=x2<x1 or x4<x2<=x3<x1:
        if y3<y2<=y1<y4 or y3<y2<=y4<y1 or y3<=y2<y4<=y1 or y3<=y4<y2<y1 or y3<y1<=y2<y4:
            area = (x1-x4)*(y1+y4)/2 -area_of_shape

    if x3<x2<=x1<x4 or x3<x1<=x2<x4:
        if y2<y1<=y4<y3 or y2<y1<=y3<y4 or y2<=y1<y3<=y4 or y2<=y3<y1<y4 or y2<y4<=y1<y3:
            area = (x4-x3)*(y4+y3)/2 -area_of_shape

    if x2<x1<=x4<x3 or x2<x4<=x1<x3:
        if y1<y4<=y3<y2 or y1<y4<=y2<y3 or y1<=y4<y2<=y3 or y1<=y2<y4<y3 or y1<y3<=y4<y2:
            area = (x3-x2)*(y3+y2)/2 -area_of_shape
    #two sides are facing the x-axis
    if min(x1, x2, x3, x4) == x1 and max(x1, x2, x3, x4) == x3 and min(y1, y2, y3, y4) == y4 and x4 != x1 and x4 != x3:
        area = (x4-x1)*(y1+y4)/2 + (x3-x4)*(y3+y4)/2
    if min(x1, x2, x3, x4) == x4 and max(x1, x2, x3, x4) == x2 and min(y1, y2, y3, y4) == y3 and x3 != x4 and x3 != x2:
        area = (x3-x4)*(y4+y3)/2 + (x2-x3)*(y2+y3)/2
    if min(x1, x2, x3, x4) == x3 and max(x1, x2, x3, x4) == x1 and min(y1, y2, y3, y4) == y2 and x2 != x3 and x2 != x1:
        area = (x2-x3)*(y3+y2)/2 + (x1-x2)*(y1+y2)/2
    if min(x1, x2, x3, x4) == x2 and max(x1, x2, x3, x4) == x4 and min(y1, y2, y3, y4) == y1 and x1 != x2 and x1 != x4:
        area = (x1-x2)*(y2+y1)/2 + (x4-x1)*(y4+y1)/2

    if min(x1, x2, x3, x4) == x1 and max(x1, x2, x3, x4) == x3:
        if min(y1, y2, y3, y4) == y1 or y3:
            if x4 != x1 and x4 != x3:
                area = (x4-x1)*(y1+y4)/2 + (x3-x4)*(y3+y4)/2
    if min(x1, x2, x3, x4) == x4 and max(x1, x2, x3, x4) == x2:
        if min(y1, y2, y3, y4) == y2 or y4:
            if x3 != x4 and x3 != x2:
                area = (x3-x4)*(y4+y3)/2 + (x2-x3)*(y2+y3)/2
    if min(x1, x2, x3, x4) == x3 and max(x1, x2, x3, x4) == x1:
        if min(y1, y2, y3, y4) == y3 or y1:
            if x2 != x3 and x2 != x1:
                area = (x2-x3)*(y3+y2)/2 + (x1-x2)*(y1+y2)/2
    if min(x1, x2, x3, x4) == x2 and max(x1, x2, x3, x4) == x4:
        if min(y1, y2, y3, y4) == y2 or y4:
            if x1 != x2 and x1 != x4:
                area = (x1-x2)*(y2+y1)/2 + (x4-x1)*(y4+y1)/2
    #one side is facing the x-axis
    if min(y1, y2, y3, y4)==y1 or min(y1, y2, y3, y4)==y4:
        if min(x1, x2, x3, x4) == x1 and max(x1, x2, x3, x4) == x4:
            area = (x4-x1)*(y1+y4)/2
    if min(y1, y2, y3, y4)==y4 or min(y1, y2, y3, y4)==y3:
        if min(x1, x2, x3, x4) == x4 and max(x1, x2, x3, x4) == x3:
            area = (x3-x4)*(y4+y3)/2
    if min(y1, y2, y3, y4)==y3 or min(y1, y2, y3, y4)==y2:
        if min(x1, x2, x3, x4) == x3 and max(x1, x2, x3, x4) == x2:
            area = (x2-x3)*(y3+y2)/2
    if min(y1, y2, y3, y4)==y2 or min(y1, y2, y3, y4)==y1:
        if min(x1, x2, x3, x4) == x2 and max(x1, x2, x3, x4) == x1:
            area = (x1-x2)*(y2+y1)/2

if max(y1, y2, y3, y4) <= 0:
    # three sides facing the x-axis
    area_of_shape = abs((-(x1 * y2 + x2 * y3 + x3 * y4 + x4 * y1) + (x2 * y1 + x3 * y2 + x4 * y3 + x1 * y4)) / 2)
    # shape is tilted toward right
    if x2 < x4 <= x3 < x1 or x2 < x3 < x1 < x4 or x2 < x3 <= x4 < x1 or x2 < x3 < x4 < x1:
        if y2 < y1 <= y3 < y4 or y2 <= y1 < y3 <= y4 or y1 < y2 <= y3 < y4 or y4 < y1 < y2 <= y3 or y1 < y3 <= y2 < y4:
            area = abs((x2 - x1) * (y2 + y1) / 2) - area_of_shape

    if x1 < x3 <= x2 < x4 or x1 < x2 < x4 < x3 or x1 < x2 <= x3 < x4 or x1 < x2 < x3 < x4:
        if y1 < y4 <= y2 < y3 or y1 <= y4 < y2 <= y3 or y4 < y1 <= y2 < y3 or y3 < y4 < y1 <= y2 or y4 < y2 <= y1 < y3:
            area = abs((x1 - x4) * (y1 + y4) / 2) - area_of_shape

    if x4 < x2 <= x1 < x3 or x4 < x1 < x3 < x2 or x4 < x1 <= x2 < x3 or x4 < x1 < x2 < x3:
        if y4 < y3 <= y1 < y2 or y4 <= y3 < y1 <= y2 or y3 < y4 <= y1 < y2 or y2 < y3 < y4 <= y1 or y3 < y1 <= y4 < y2:
            area = abs((x4 - x3) * (y4 + y3) / 2) - area_of_shape

    if x3 < x1 <= x4 < x2 or x3 < x4 < x2 < x1 or x1 < x4 <= x3 < x2 or x3 < x4 < x1 < x2:
        if y1 < y2 <= y4 < y3 or y1 <= y2 < y4 <= y3 or y2 < y3 <= y4 < y1 or y1 < y2 < y3 <= y4 or y2 < y4 <= y3 < y1:
            area = abs((x3 - x2) * (y3 + y2) / 2) - area_of_shape
    # the shape is tilted towards left

    if x1 < x2 <= x3 < x4 or x1 < x3 <= x2 < x4:
        if y1 < y4 <= y3 < y2 or y4 < y1 <= y3 < y2 or y4 <= y1 < y3 <= y2 or y4 <= y3 < y1 < y2:
            area = abs((x4 - x1) * (y4 + y1) / 2) - area_of_shape

    if x4 < x1 <= x2 < x3 or x4 < x2 <= x1 < x3:
        if y4 < y3 <= y2 < y1 or y3 < y4 <= y2 < y1 or y3 <= y4 < y2 <= y1 or y3 <= y2 < y4 < y1:
            area = abs((x3 - x4) * (y3 + y4) / 2) - area_of_shape

    if x3 < x4 <= x1 < x2 or x3 < x1 <= x4 < x2:
        if y3 < y2 <= y1 < y4 or y2 < y3 <= y1 < y4 or y2 <= y3 < y1 <= y4 or y2 <= y1 < y3 < y4:
            area = abs((x2 - x3) * (y2 + y3) / 2) - area_of_shape

    if x2 < x3 <= x4 < x1 or x2 < x4 <= x3 < x1:
        if y2 < y1 <= y4 < y3 or y1 < y2 <= y4 < y3 or y1 <= y2 < y4 <= y3 or y1 <= y4 < y2 < y3:
            area = abs((x1 - x2) * (y1 + y2) / 2) - area_of_shape

    # two sides are facing the x-axis
    if min(x1, x2, x3, x4) == x1 and max(x1, x2, x3, x4) == x3 and min(y1, y2, y3, y4) == y4 and x2 != x1 and x4 != x3:
        area = -(x4 - x1) * (y1 + y4) / 2 - (x3 - x4) * (y3 + y4) / 2
    if min(x1, x2, x3, x4) == x4 and max(x1, x2, x3, x4) == x2 and min(y1, y2, y3, y4) == y3 and x1 != x4 and x3 != x2:
        area = -(x3 - x4) * (y4 + y3) / 2 - (x2 - x3) * (y2 + y3) / 2
    if min(x1, x2, x3, x4) == x3 and max(x1, x2, x3, x4) == x1 and min(y1, y2, y3, y4) == y2 and x4 != x3 and x2 != x1:
        area = -(x2 - x3) * (y3 + y2) / 2 - (x1 - x2) * (y1 + y2) / 2
    if min(x1, x2, x3, x4) == x2 and max(x1, x2, x3, x4) == x4 and min(y1, y2, y3, y4) == y1 and x3 != x2 and x1 != x4:
        area = -(x1 - x2) * (y2 + y1) / 2 - (x4 - x1) * (y4 + y1) / 2

    if min(x1, x2, x3, x4) == x1 and max(x1, x2, x3, x4) == x3:
        if max(y1, y2, y3, y4) == y1 or y3:
            if x2 != x1 and x4 != x3:
                area = -(x3 - x2) * (y3 + y2) / 2 - (x2 - x1) * (y2 + y1) / 2
    if min(x1, x2, x3, x4) == x4 and max(x1, x2, x3, x4) == x2:
        if max(y1, y2, y3, y4) == y2 or y4:
            if x1 != x4 and x3 != x2:
                area = -(x2 - x1) * (y2 + y1) / 2 - (x1 - x4) * (y1 + y4) / 2
    if min(x1, x2, x3, x4) == x3 and max(x1, x2, x3, x4) == x1:
        if max(y1, y2, y3, y4) == y3 or y1:
            if x4 != x3 and x2 != x1:
                area = -(x1 - x4) * (y1 + y4) / 2 - (x4 - x3) * (y4 + y3) / 2
    if min(x1, x2, x3, x4) == x2 and max(x1, x2, x3, x4) == x4:
        if max(y1, y2, y3, y4) == y2 or y4:
            if x3 != x2 and x1 != x4:
                area = -(x4 - x3) * (y4 + y3) / 2 - (x3 - x2) * (y3 + y2) / 2

    if min(x1, x2, x3, x4) == x2 and max(x1, x2, x3, x4) == x4:
        if max(y1, y2, y3, y4) == y2 or y4:
            if x1 == x4 and x3 != x2:
                area = -(x4 - x3) * (y4 + y3) / 2 - (x3 - x2) * (y3 + y2) / 2
    if min(x1, x2, x3, x4) == x1 and max(x1, x2, x3, x4) == x3:
        if max(y1, y2, y3, y4) == y1 or y3:
            if x4 == x3 and x2 != x1:
                area = -(x3 - x2) * (y3 + y2) / 2 - (x2 - x1) * (y2 + y1) / 2
    if min(x1, x2, x3, x4) == x4 and max(x1, x2, x3, x4) == x2:
        if max(y1, y2, y3, y4) == y4 or y2:
            if x3 == x2 and x1 != x4:
                area = -(x2 - x1) * (y2 + y1) / 2 - (x1 - x4) * (y1 + y4) / 2
    if min(x1, x2, x3, x4) == x3 and max(x1, x2, x3, x4) == x1:
        if max(y1, y2, y3, y4) == y3 or y1:
            if x2 == x1 and x4 != x3:
                area = -(x1 - x4) * (y1 + y4) / 2 - (x4 - x3) * (y4 + y3) / 2
    # one side is facing the x-axis
    if max(y1, y2, y3, y4) == y1 or max(y1, y2, y3, y4) == y2:
        if min(x1, x2, x3, x4) == x1 and max(x1, x2, x3, x4) == x2:
            area = -(x2 - x1) * (y1 + y2) / 2
    if max(y1, y2, y3, y4) == y4 or max(y1, y2, y3, y4) == y1:
        if min(x1, x2, x3, x4) == x4 and max(x1, x2, x3, x4) == x1:
            area = -(x1 - x4) * (y4 + y1) / 2
    if max(y1, y2, y3, y4) == y3 or max(y1, y2, y3, y4) == y4:
        if min(x1, x2, x3, x4) == x3 and max(x1, x2, x3, x4) == x4:
            area = -(x4 - x3) * (y3 + y4) / 2
    if max(y1, y2, y3, y4) == y2 or max(y1, y2, y3, y4) == y3:
        if min(x1, x2, x3, x4) == x2 and max(x1, x2, x3, x4) == x3:
            area = -(x3 - x2) * (y3 + y2) / 2

print("%.2f"%area)