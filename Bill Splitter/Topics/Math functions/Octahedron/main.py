from math import pow
from math import sqrt
edge_length = int(input())
oct_area = round(2 * sqrt(3) * pow(edge_length, 2), 2)
oct_volume = round( 1/3 * sqrt(2) * pow(edge_length, 3), 2)
print(oct_area, oct_volume, sep=" ")