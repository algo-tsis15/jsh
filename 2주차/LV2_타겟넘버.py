def solution(numbers, target):
    global answer  # 전역 변수 사용
    answer = 0
    N = len(numbers)
    DFS(0, 0, N, numbers, target)  # level,total
    return answer


def DFS(level, total, N, numbers, target):
    if level == N:
        if total == target:
            global answer
            answer += 1
            return
        else:
            return
    else:
        DFS(level + 1, total + numbers[level], N, numbers, target)  # 양의 정수 누적합
        DFS(level + 1, total + numbers[level] * -1, N, numbers, target)  # 음의 정수 누적합


