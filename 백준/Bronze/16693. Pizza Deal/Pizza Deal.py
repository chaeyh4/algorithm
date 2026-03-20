import math

a, p1 = map(float, input().split())
r, p2 = map(float, input().split())

slice_value = a / p1
whole_value = (math.pi * r * r) / p2

if slice_value > whole_value:
    print("Slice of pizza")
else:
    print("Whole pizza")