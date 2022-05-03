def solution(n, times):
    answer = 0
    times.sort()
    left = 1
    right = times[-1] * n  # 최대 심사 시간
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for time in times:
            cnt += mid // time
        if cnt >= n:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1

    return answer