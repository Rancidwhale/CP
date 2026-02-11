ab=bc=ac=None
def getab(s1):
    if s1 == 'A>B' or s1 == 'B<A':
        return True
    else: return False
def getbc(s2):
    if s2 == 'B>C' or s2 == 'C<B':
        return True
    else: return False
def getac(s3):
    if s3 == 'A>C' or s3 == 'C<A':
        return True
    else: return False

for _ in range(3):
    s=input()
    # print(s[0],s[2])
    if (s[0]== 'A' or s[0]== 'B') and (s[2]== 'A' or s[2]== 'B'):
        ab = getab(s) 
        # print("got ab")
    elif (s[0]== 'C' or s[0]== 'B') and (s[2]== 'C' or s[2]== 'B'):
        bc = getbc(s)
        # print("got bc")
    elif (s[0]== 'A' or s[0]== 'C') and (s[2]== 'A' or s[2]== 'C'):
        ac = getac(s)
        # print("got ac")
# print(ab,bc,ac)
if ab == None or bc ==None or ac ==None:
    print("Impossible")
else:
    if ab:
        if bc:
            if ac:
                print("CBA")
            else:
                print("Impossible")
        else:
            if ac:
                print("BCA")
            else:
                print("BAC")
    else:
        if bc:
            if ac:
                print("CAB")
            else:
                print("ACB")
        else:
            if ac:
                print("Impossible")
            else:
                print("ABC")
        

'''
a>b b>a
b>c c>b
a>c c>a

'''