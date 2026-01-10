n = list(map(int, input().split()))

n.sort()
n=set(n)
l = len(n)

print(4-l)