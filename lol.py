n=100
ct1 = 0
for i in range(n+1):
    if i%2==0 or i%3==0 or i%5==0 or i%7==0:
        ct1 += 1

print(ct1)
ct2 = 0
for i2 in range(2):
    for i3 in range(2):
        for i5 in range(2):
            for i7 in range(2):
                d=1
                ect = 0

                if i2: 
                    d *= 2
                    ect+=1
                if i3:
                    d *= 3
                    ect+=1
                if i5:
                    d *= 5
                    ect+=1
                if i7:
                    d *= 7
                    ect+=1

                print(i2, i3, i5, i7)
                if ect == 0:
                    continue
                
                print(d,ect)
                sign = 0
                if ect%2==1:
                    sign = 1
                else:
                    sign = -1

                print(sign)
                ct2 += sign * (int)(n / d) 
                print(ct2)

print(ct2)