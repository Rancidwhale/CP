n = int(input())
k = int(input())
comp = list(map(str,input().split()))
r = int(input())
revs=[
    "newshop is providing good services in the city; everyone should use newshop",
    "best services by newshop",
    "fashionbeats has great services in the city",
    "I am proud to have fashionbeats",
    "newshop has awesome services",
    "Thanks newshop for the quick delivery"]

dict={}
for i in comp:
    dict[i]=0
print(revs)
for r in revs:
    for word in r.split():
        if str(word) in dict:
            dict[word]+=1
ans =[]
print(dict)
for _ in range(k):
    max = 0
    nam = ''
    for key,val in dict.items():
        if val>max:
            max=val
            nam = key
    del dict[nam]
    ans.append(nam)

print(ans)
