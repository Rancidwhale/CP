import math
n, m, x = map(int,input().split())
keyboard = []
for i in range(n):
    keyboard.append(input())
keys = {}
shifts = []
for r in range(n):
    for c in range(m):
        if keyboard[r][c] == 'S':
            shifts.append((r, c))

q = int(input())
def distance(a, b, p, r):
    dist = math.sqrt((p - a)**2 + (r - b)**2)
    return dist
s = input()

