no_of_servers=int(input("no of servers"))
load_of_servers=[]
print("enter server loads")
for i in range(no_of_servers):
    q = int(input(str(i)+": "))
    load_of_servers.append(q)

no_of_req=int(input("no of requests"))

# for _ in range(no_of_req):
#     min = 9999999999999999
#     idx=0
#     for i, load in enumerate(load_of_servers):
#         if min>load:
#             min=load
#             idx=i
            
#     load_of_servers[idx]=load_of_servers[idx]+1


#     print("updated load ", load_of_servers)

load_of_servers.sort()
for _ in range(no_of_req):
    i=1
    while load_of_servers[i]==load_of_servers[i-1]:
        i+=1
        if i == no_of_servers:
            break
    if i==1:
        load_of_servers[i-1]+=1
        # load_of_servers[i], load_of_servers[i+1] = load_of_servers[i+1], load_of_servers[i]
    else:
        load_of_servers[i-1]+=1
    print("updated load ", load_of_servers)
