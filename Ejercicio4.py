import heapq

x = [7, 1, 6, 2, 10, 4, 1, 5]
h = []

for v in x:
    heapq.heappush(h, v)

r = []
while h:
    r.append(heapq.heappop(h))

print(r)