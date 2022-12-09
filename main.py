# import Dynamics
# if __name__ == "__main__":
#     Dynamics.print_equations_for_Wolfram_Mathematica()

line1 = input().split(" ")
line2 = input().split(" ")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def orientation(p, q, r):
    val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - p.y))
    if val == 0:
        return 0
    if val > 0:
        return 1  # clock
    return 2


# q belong pr
def intersection(p, q, r):
    if ((q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and
            (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))):
        return True
    return False

pairs1 = list(float(val) for val in line1)

pairs2 = list(float(val) for val in line2)

p1 = Point(pairs1[0], pairs1[1])
q1 = Point(pairs1[2], pairs1[3])

p2 = Point(pairs2[0], pairs2[1])
q2 = Point(pairs2[2], pairs2[3])

o1 = orientation(p1, q1, p2)
o2 = orientation(p1, q1, q2)
o3 = orientation(p2, q2, p1)
o4 = orientation(p2, q2, q1)

if o1 != o2 and o3 != o4:
    print(1)
elif o1 == 0 and intersection(p1, p2, q1):
    print(1)
elif o2 == 0 and intersection(p1, q2, q1):
    print(1)
elif o3 == 0 and intersection(p2, q1, q2):
    print(1)
elif o4 == 0 and intersection(p2, q1, q2):
    print(1)
else:
    print(0)