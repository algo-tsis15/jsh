def solution(n, computers):
    answer = 0
    visited=[False]*n
    for i in range(n):
        if visited[i]==False:
            BFS(n,computers,i,visited)
            answer+=1
    return answer

def BFS(n,computers,i,visited):
    visited[i]=True
    q=[]
    q.append(i)
    while q:
        cur=q.pop(0)
        for j in range(n):
            if j!=i and computers[cur][j]==1:
                if visited[j]==False:
                    visited[cur]=True
                    q.append(j)