s = list(map(str, input().split(', ')))
if s == ['{}']:
    print(0)
else : 
    n=len(s)
    s[0]=s[0][1]
    s[n-1]=s[n-1][0]

    s = set(s)
    print(len(s))