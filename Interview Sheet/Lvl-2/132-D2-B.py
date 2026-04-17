import math 
x = list(map(int, input().split()))
y = list(map(int, input().split()))
m = y.pop(0)
z = list(map(int, input().split()))
k = z.pop(0)
A,B = map(int, input().split())

r1 = max(x)
p1 = max(y)
p2 = min(z)

print(r1 * math.sqrt((B * p1) / (A * p2 + B * p1)))