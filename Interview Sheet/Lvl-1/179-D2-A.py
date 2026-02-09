from collections import Counter

n = int(input())
a = list(map(int,input().split()))
counter = Counter(a)
max_occurrence = max(counter.values())
if max_occurrence > (n+1)//2:
    print("NO")
else:
    print("YES")