import string
n = int(input())
st = input().lower()

st = set(st)

def solve(st):
    alpha = list(string.ascii_lowercase)
    if len(st)== len(alpha):
        return "YES"
    else:
        return "NO"

print(solve(st))