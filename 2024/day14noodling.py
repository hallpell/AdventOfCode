"""Horizontal groupings: 14, 115, 216, 317, 418, 519, 620, 721, 822
Vertical groupings: 94, 197, 300, 403
H: 14 + 101nh
V: 94 + 103nv

94 + 103nh = 14 + 101nv
80 + 103nh = 101nv
n = 40
14 + 4040 = 4054"""

h = []
v = {}
for i in range(1000):
    h.append(14+101*i)
    v[94+103*i] = 1

for hval in h:
    if hval in v:
        print(hval)

