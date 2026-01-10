x = input()
l,u =0,0
for i in x:
    if i.islower():
        l+=1
    else: u+=1
if u>l:
    print(x.upper())
else :
    print(x.lower())