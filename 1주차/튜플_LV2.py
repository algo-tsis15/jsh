def solution(s):
    answer = []
    tmp = []
    s = s[2:len(s) - 2]
    s = s.replace('{', '')
    s = s.replace('},', ' ')

    tmp = s.split()  # ["111","20,111"]
    tmp.sort(key=len)  # 원소 길이 순으로 정렬
    answer.append(tmp.pop(0))  # 첫 원소는 바로 answer에 추가

    for t in tmp:
        new_t = t.split(',')
        for i in new_t:
            if i not in answer:
                answer.append(i)

    for i in range(0, len(answer)):
        answer[i] = int(answer[i])
    return answer