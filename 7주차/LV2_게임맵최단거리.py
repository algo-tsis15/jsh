dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
min_distance = 10000


def solution(maps):
    n, m = len(maps) - 1, len(maps[0]) - 1  # 도착 지점 좌표
    BFS(0, 0, 1, maps, n, m)  # r,c,distance,maps
    return min_distance


def BFS(r, c, distance, maps, n, m):
    global min_distance
    q = []
    q.append((r, c, 1))
    visited = [[False] * (m + 1) for _ in range(n + 1)]
    visited[r][c] == True
    while q:
        cur = q.pop(0)
        if cur[0] == n and cur[1] == m:
            min_distance = min(min_distance, cur[2])
            return
        for d in range(4):
            nr, nc = dr[d] + cur[0], dc[d] + cur[1]
            if isIn(nr, nc, n, m) == False or visited[nr][nc] == True:
                continue
            if maps[nr][nc] == 1:
                q.append((nr, nc, cur[2] + 1))
                visited[nr][nc] = True

    if min_distance == 10000:  # 도착 못할 경우 예외 처리
        min_distance = -1


def isIn(r, c, n, m):
    return r >= 0 and r <= n and c >= 0 and c <= m