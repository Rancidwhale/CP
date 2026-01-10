import math
while True:
    step , mod = map(int, input().split())
    if step == 0 and mod == 0:
        break
    if math.gcd(step,mod) == 1:
        r = 'good'
    else:
        r = 'bad'
    
    print(f"{step:>10}{mod:>10} {r}")
    print()  # (optional) empty line for better readability
