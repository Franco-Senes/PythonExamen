import heapq

g = {
    1: {2: 5, 3: 2},
    2: {1: 5, 3: 1, 4: 4},
    3: {1: 2, 2: 1, 5: 6},
    4: {2: 4, 6: 2, 7: 8},
    5: {3: 6, 6: 1},
    6: {4: 2, 5: 1, 7: 3},
    7: {4: 8, 6: 3}
}

m_d = -1
m_n = None

for s in g:
    d = {v: float('inf') for v in g}
    d[s] = 0
    q = [(0, s)]

    while q:
        c_d, u = heapq.heappop(q)
        if c_d > d[u]:
            continue
        for n, w in g[u].items():
            if d[u] + w < d[n]:
                d[n] = d[u] + w
                heapq.heappush(q, (d[n], n))

    for v in d:
        if d[v] != float('inf') and d[v] > m_d:
            m_d = d[v]
            m_n = v

print("Nodo:", m_n)
print("Distancia:", m_d)