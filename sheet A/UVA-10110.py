import math
while True:
    x = int(input(""))
    if x == 0:
        break
    root = int(math.sqrt(x) + 1e-27)
    if root * root == x:
        print("Yes")
    else :
        print("No")