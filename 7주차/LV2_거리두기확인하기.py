dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def solution(places):
    answer = []
    for i in range(5):
        arr = [list(s) for s in places[i]]
        flag = isValid(arr)
        if flag == True:
            answer.append(1)
        else:
            answer.append(0)
    return answer


def isValid(arr):
    pCnt = 0
    for i in range(5):
        for j in range(5):
            if arr[i][j] == 'P':
                pCnt += 1
                # 상하좌우 P 있는지 검사
                for d in range(4):
                    nr = dr[d] + i
                    nc = dc[d] + j
                    if isIn(nr, nc) == True:
                        if arr[nr][nc] == 'P':
                            return False
                # 좌우 대각선일 때 파티션 검사
                if isIn(i + 1, j - 1) == True:
                    if arr[i + 1][j - 1] == 'P':
                        if arr[i + 1][j] == 'O' or arr[i][j - 1] == 'O':
                            return False
                if isIn(i + 1, j + 1) == True:
                    if arr[i + 1][j + 1] == 'P':
                        if arr[i + 1][j] == 'O' or arr[i][j + 1] == 'O':
                            return False
                # 상하좌우x2일 때 파티션 검사
                for d in range(4):
                    nr = dr[d] + i
                    nnr = dr[d] * 2 + i
                    nc = dc[d] + j
                    nnc = dc[d] * 2 + j
                    if isIn(nnr, nnc) == True:
                        if arr[nnr][nnc] == 'P':  # 2칸 간격에 P가 있는 경우 -> 사이에 파티션 없다면 False
                            if arr[nr][nc] != 'X':
                                return False
    if pCnt == 0:
        return True
    return True


def isIn(r, c):
    return r >= 0 and r < 5 and c >= 0 and c < 5