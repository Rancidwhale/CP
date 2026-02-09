n = int(input())
f = input()

if "R" in f and "L" not in f:
    s=f.index('R')
    t=n-1-f[::-1].index('R')
    print(s+1,t+1)
elif 'L' in f and 'R' not in f:
    s=n-1-f[::-1].index('L')
    t=f.index('L')
    print(s+1,t+1)
else:
    s=f.index('R')
    t=n-1-f[::-1].index('R')
    print(s+1,t+1)