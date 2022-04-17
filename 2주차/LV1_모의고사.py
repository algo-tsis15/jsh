def solution(answers):
    answer = []
    s1=[1,2,3,4,5]
    s2=[2,1,2,3,2,4,2,5]
    s3=[3,3,1,1,2,2,4,4,5,5]
    c1=c2=c3=0
    for i in range(len(answers)):
        if answers[i] == s1[i%5]: c1 += 1
        if answers[i] == s2[i%8]: c2 += 1
        if answers[i] == s3[i%10]: c3 += 1

    score=max(c1,c2,c3)
    if c1==score:
        answer.append(1)
    if c2==score:
        answer.append(2)
    if c3==score:
        answer.append(3)
    return answer

print(solution([1,2,3,4,5]))