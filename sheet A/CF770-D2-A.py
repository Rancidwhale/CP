import string
al = list(string.ascii_lowercase)

n,k = map(int, input().split())
al = al[:k]
password = ""
i=0
for _ in range(n):
    if i == len(al):i=0
    password+=al[i]
    i+=1

print(password)
