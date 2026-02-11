n,m = map(int, input().split())
containers = []

for _ in range(m):
    a, b = map(int, input().split())
    containers.append((a, b))

# sort by b (matches per box), descending
containers.sort(key=lambda x: x[1], reverse=True)
left = n
ans = 0
for (a,b) in containers:
    take = min(left,a)
    ans += take*b
    left -= take
    if left == 0:
        break
print(ans)