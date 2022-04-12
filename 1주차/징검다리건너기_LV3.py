def solution(stones, k):
    answer = 0  # 완주한 사람 수
    while True:
        tmp=[]
        maxJump=0
        for i in range(0,len(stones)):
            if stones[i]==0:
                tmp.append(i) # 0인 인덱스 저장
        if len(tmp)>0:
            jump=0
            for i in range(0, len(tmp)-1):
                if (tmp[i]+1)!=tmp[i+1]:
                    jump=0
                else:
                    jump+=1
                maxJump=max(maxJump,jump) # 최대 점프 개수 갱신
            if maxJump>=(k-1):
                return answer
            else :
                answer+=1
                for i in range(0, len(stones)):
                    if i not in tmp:
                        stones[i]-=1
        else:
            answer+=1
            for i in range(0, len(stones)):
                stones[i]-=1
    return answer