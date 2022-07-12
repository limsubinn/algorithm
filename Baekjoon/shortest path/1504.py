import heapq
import sys
input = sys.stdin.readline
INF = int(1e8)

n, e = map(int, input().split())

graph = [[] for i in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance

d1 = dijkstra(1)
d2 = dijkstra(v1)
d3 = dijkstra(v2)

res = min(d1[v1] + d2[v2] + d3[n], d1[v2] + d3[v1] + d2[n])

if res >= INF:
    print(-1)
else:
    print(res)