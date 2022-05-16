def solution(n, t, m, timetable):
    answer = 0
    timetable = [int(time[:2]) * 60 + int(time[3:]) for time in timetable]  # timetable -> 분 단위로 통일시키기
    timetable.sort()
    busDict = [[9 * 60 + i * t, 0, 0] for i in range(n)]  # 버스도착시간, 탑승자 수, 마지막 탑승 시간
    t_idx = 0
    d_idx = 0

    while True:
        if t_idx == len(timetable) or d_idx == n:
            break
        # 탑승 자리가 있는 경우 and 버스 도착시간보다 이전인 경우:
        #   1) 마지막 탑승 시간에 시간 추가 -> dict[i][2]
        #   2) 탑승자 수 1 증가 -> dict[i][1]++
        if busDict[d_idx][1] < m and timetable[t_idx] <= busDict[d_idx][0]:
            busDict[d_idx][1] += 1
            busDict[d_idx][2] = timetable[t_idx]
            t_idx += 1  # 다음 크루원 계산 위해 idx 증가
        else:
            d_idx += 1  # 버스를 타지 못하는 경우 -> 다음 버스 시간으로 넘김

    # 마지막 버스가 꽉찼다면 1분 전에 줄서야 함
    # 그게 아니라면 마지막 버스 도착시간에 줄서면 됨
    if busDict[-1][1] == m:
        answer = busDict[-1][2] - 1
    else:
        answer = busDict[-1][0]
    return str(answer // 60).zfill(2) + ":" + str(answer % 60).zfill(2)
