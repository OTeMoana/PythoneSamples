import math

g = 9.8
l = 160
alpha = 12

alpha = alpha * 2 * math.pi / 360

v = (l * g / math.cos(alpha) / math.sin(alpha)) ** 0.5
print(v)

t = 160 / (math.cos(alpha) * v )

print(t)