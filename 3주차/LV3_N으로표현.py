def solution(N, number):
    answer = 0
    if N==number:
        return 1

    # [{5}, {55}, {555}, {5555}, {55555}, {555555}, {5555555}, {55555555}]
    numbers = [set([int(str(N)*i)]) for i in range(1,9)]

    for i in range(1,8):
        for j in range(i):
            for op1 in numbers[j]:
                for op2 in numbers[i-j-1]:
                    numbers[i].add(op1+op2)
                    numbers[i].add(op1-op2)
                    numbers[i].add(op1*op2)
                    if op2!=0:
                        numbers[i].add(op1//op2)
        if number in numbers[i]:
            answer=i+1
            break
    else:
        answer-=1

    return answer