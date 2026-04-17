n,m,k = map(int, input().split())
holes = list(map(int,input().split()))

start = False
hole = False
end = 1
ishole = [False]*(n+1)
bonepos = 1
for i in holes:
    ishole[i]=True
if ishole[1]:
    hole = True
for _ in range(k):
    u,v = map(int, input().split())
    if hole:
        # print("Hole is True")
        continue
    else:
        # print("Bone Pos: ",bonepos)
        if u == bonepos or v == bonepos:
            pos = u+v-bonepos
            bonepos = pos
            # print("Bone Pos switch: ",bonepos)
            # print(holes)
            if ishole[pos]:
                # print("In hole making true")
                hole = True
            
print(bonepos)

