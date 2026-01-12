from collections import defaultdict
userSongs = {  
       "David": ["song1", "song2", "song3", "song4", "song8"],
       "Emma":  ["song5", "song6", "song7"]
    }
songGenres = {  
       "Rock":    ["song1", "song3"],
       "Dubstep": ["song7"],
       "Techno":  ["song2", "song4"],
       "Pop":     ["song5", "song6"],
       "Jazz":    ["song8", "song9"]
    }

dict={}
count = {}
for g,songs in songGenres.items():
    count[g]=0
    for s in songs:
        dict[s]=g

sel = []
final = defaultdict(list)
for n,songs in userSongs.items():
    cur = count.copy()
    m = 0
    sel = ''
    for s in songs:
        gen = dict[s]
        cur[gen]+=1
        if cur[gen]>m:
            m=cur[gen]
    for g ,c in cur.items():
        if c==m:
            final[n].append(g)
    


print(final)

        
        

