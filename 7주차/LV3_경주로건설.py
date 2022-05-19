from collections import deque


def solution(board):
    dr = [0, 1, 0, -1]  # 우,하,좌,상
    dc = [1, 0, -1, 0]
    N = len(board)

    def isIn(r, c):
        return r >= 0 and r < N and c >= 0 and c < N

    def BFS(r, c, cost, direction):
        dp = [[0] * N for _ in range(N)]
        for i in range(N):  # dp 초기화
            for j in range(N):
                if board[i][j] == 1: dp[i][j] = 1

        q = deque()
        q.append((r, c, cost, direction))
        while q:
            curR, curC, curCost, curDir = q.popleft()
            for d in range(4):
                nr, nc = dr[d] + curR, dc[d] + curC
                if isIn(nr, nc) == False: continue
                if dp[nr][nc] == 1: continue
                nCost = curCost + 100 if curDir == d else curCost + 600
                if dp[nr][nc] == 0 or (dp[nr][nc] > 0 and dp[nr][nc] > nCost):
                    q.append((nr, nc, nCost, d))
                    dp[nr][nc] = nCost
        return dp[-1][-1]

    return min(BFS(0, 0, 0, 0), BFS(0, 0, 0, 1))