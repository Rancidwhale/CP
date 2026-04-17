import math

s1 = input()
s2 = input()

p1=s1.count('+')
m1=s1.count('-')

p2=s2.count('+')
m2=s2.count('-')
q2=s2.count('?')

if q2 == 0:
    if p1 == p2:
        print(1/1)
    else:
        print(0/1)
else:
    p3 = p1-p2
    m3 = m1-m2
    # print(m3,p3)
    # print(q2)
    if q2< p3 or q2 < m3:
        print(0/1)
    else:
        probability =  math.comb(q2, p3) / (2 ** q2)
        print(probability)
