import math
points = [(1.1, 2.0), (3.1, 1.0), (4.4, 5.3), (2.6, 3.2), (2.6, 4.6), (5.3, 5.2), (3.2, 4.5), (5.3, 4.7)]
def distance(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    dist = math.sqrt(dx ** 2 + dy ** 2)
#     print("dist", p1, p2, " is ", dist)
    res.append([p1, p2, dist])
    return dist


res = []
def cloestPoint(p, low, high):
    min_dist = math.inf
    if high - low <= 3:
        for i in range(low, high):
            for j in range(i + 1, high):
                d = distance(p[i], p[j])
                if d < min_dist:
                    min_dist = d
        return min_dist
    else:
        mid = (high - low) // 2 + low
        axis = p[mid]
        d_left = cloestPoint(p, low, mid)
        d_right = cloestPoint(p, mid + 1, high)
        delta = min(d_left, d_right)

        # k = 0
        Y = sorted(p, key=lambda point: point[1])
        T = []
        for i in range(len(Y)):  # 从按y坐标升序排序的点对p中抽取集合T
            if abs(Y[i][0] - axis[0]) <= delta:
                T.append(Y[i])
                # k = k + 1
        delta_prime = delta

        for i in range(len(T) - 1):  # i=0 to len(T) - 1开区间[0, len(T))
            for j in range(i + 1, min(i + 7, len(T))):
                d = distance(T[i], T[j])
                if d < delta_prime:
                    delta_prime = d
        delta = delta_prime
    return delta


md = cloestPoint(points, 0, len(points))
sres = sorted(res, key=lambda b: b[2])[0]
print("最小点对和最小距离",sres)


