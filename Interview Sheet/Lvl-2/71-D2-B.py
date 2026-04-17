from bisect import bisect_right
n, m, k, t = map(int, input().split())

waste_set = []
for _ in range(k):
    a,b = map(int, input().split())
    pos = (a-1)*m + (b-1)
    waste_set.append(pos)

queries = []
for _ in range(t):
    a,b = map(int, input().split())
    queries.append([a-1,b-1])

waste_set.sort()
# print("Waste Set: ", waste_set)
total_cells = n * m
cultivated_positions = {}
# pos = r*m + c
crops = ["Carrots", "Kiwis", "Grapes"]
# print(cultivated_positions)
# print("\n\nQueries")
for ri, ci in queries:
    # print(ri,ci)
    pos = ri * m + ci
    if pos in waste_set:
        print("Waste")
        continue
    
    waste_before = bisect_right(waste_set,pos)
    cultivated_positions=pos - waste_before
    # print(pos)
    idx = cultivated_positions%3
    # left, right = 0, len(cultivated_positions)
    # while left < right:
    #     mid = (left + right) // 2
    #     if cultivated_positions[mid] == pos:
    #         idx = mid
    #         break
    #     elif cultivated_positions[mid] < pos:
    #         left = mid + 1
    #     else:
    #         right = mid
        # print(mid, left, right)
    # idx = left - 1  # Index in cultivated sequence
    # print(idx)
    print(crops[idx % 3])