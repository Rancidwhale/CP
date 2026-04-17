from collections import defaultdict

n , m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

deg = [0]*(n+1)

for i in range(n+1):
    deg[i]=len(graph[i])
# print(deg)
group =0
while True:
    
    st = []
    for i in range(n+1):
        if deg[i]==1:
            st.append(i)
    
    if not st:
        break
    group+=1
    for s in st:
        deg[s] = 0
        # print(graph[s])
        for nei in graph[s]:
            if deg[nei]>0:
                deg[nei]-=1
    
    # print("deg: ",deg)

print(group)