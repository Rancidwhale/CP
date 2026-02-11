n = input().strip()
count=0
while len(n) > 1:
    s = 0
    for ch in n:
        s += int(ch)
    n = str(s)       
    count +=1
print(count)

