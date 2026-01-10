from collections import defaultdict
IA = [ [1, 2],[3, 4],[4, 5]]

graph =defaultdict(set)
groups=[]
for [a,b] in IA:
    graph[a].add(b)
    graph[b].add(a)
print(graph)
cur=[]
visited = set()
def dfs(i):
    visited.add(i)
    cur.append(i)
    print("cur:",cur)
    print("visited",visited)
    for j in graph[i]:
        if j not in visited:
            dfs(j)
for key,val in graph.items():
    cur=[]
    print("cur:",cur)
    print("visited",visited)
    print("key:",key," ","val:",val)
    if key not in visited:
        dfs(key)
    groups.append(cur)
    print("groups:",groups)
sel=[]
for grp in groups:
    m=0
    if len(grp)> m:
        sel = grp
        print("sel",sel)

print(sel)


    