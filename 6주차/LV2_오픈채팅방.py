def solution(record):
    tmp = []  # id로 저장한 채팅 목록
    answer = []  # id -> 이름으로 변환한 채팅 목록
    matching = {}  # {id:name}
    for i in range(len(record)):
        input = record[i].split()
        if input[0] == "Enter":
            chat = input[1] + "님이 들어왔습니다."
            matching[input[1]] = input[2]
            tmp.append(chat)
        elif input[0] == "Leave":
            chat = input[1] + "님이 나갔습니다."
            tmp.append(chat)
        else:
            matching[input[1]] = input[2]

    for i in tmp:
        uid = i[:i.index("님")]
        suffix = i[i.index("님"):]
        answer.append(matching[uid] + suffix)

    return answer