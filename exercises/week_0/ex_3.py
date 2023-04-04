"""excercise 3 week 0 on function"""
import math


def distance(p_1, p_2):
    """compute distance between two points"""
    dx = p_1[0] - p_2[0]
    dy = p_1[1] - p_2[1]
    dist = math.sqrt(dx * dx + dy * dy)
    return dist


a = (0, 1)
b = (0, 2)
print(distance(a, b))
