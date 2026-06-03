from collections import deque

g = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2, 7],
    5: [2],
    6: [3],
    7: [4]
}

m_l = -1
m_p = []

for s in g:
    q = deque([[s]])
    v = {s}

    while q:
        p = q.popleft()
        u = p[-1]

        if len(p) > m_l:
            m_l = len(p)
            m_p = p

        for n in g[u]:
            if n not in v:
                v.add(n)
                q.append(p + [n])

print("Camino:", m_p)