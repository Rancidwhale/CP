n = int(input())
st = list(map(int, input().split()))
 
st.sort()
def solve(st):
    l,r = 0,n-1
    if st[l]==st[r]: return 0
 
    while st[l+1]==st[l] and l<n-1:
        l+=1
    while st[r-1]==st[r] and r>0:
        r-=1
 
    sp = len(st[l+1:r])
    return sp
 
print(solve(st))