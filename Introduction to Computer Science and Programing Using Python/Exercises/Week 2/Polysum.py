from math import pi
from math import tan

def polysum(n, s):
    perimeter = n * s
    area = (0.25 * n * (s **2))/ (tan(pi/n))
    result = perimeter**2 + area
    return result
