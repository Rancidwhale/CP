n,x = map(int,input().split())
chap = list(map(int,input().split()))

hours=0
chap = sorted(chap)

for c in chap:
    hours += c * x
    if x>1:x-=1

print(hours)
