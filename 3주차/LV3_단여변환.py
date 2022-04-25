def solution(begin, target, words):
    if target not in words:
        return 0
    return BFS(begin,target,words)

def BFS(begin,target,words):
    q=[]
    q.append((1,begin)) # 1: level
    while q:
        level,cur=q.pop(0)
        for word in words: # 조건에 맞는 word 탐색 시 -> return level하면 끄읕
            if validation(word,cur) and word==target:
                return level
            elif validation(word,cur): # 바꿀 수만 있는 word일 경우 -> 큐에 저장
                q.append((level+1,word))

def validation(word,cur): # 다른 문자 개수가 1개일 때만 True
    cnt=0
    for w,c in zip(word,cur):
        if w!=c: cnt+=1
        if cnt>1: return False
    if cnt==0: return False
    else: return True