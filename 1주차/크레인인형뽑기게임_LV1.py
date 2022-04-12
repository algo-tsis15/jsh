def solution(board, moves):
    answer=0
    n=len(board[0])
    stack=[]
    for i in moves:
        for j in range(n):
            if board[j][i-1]>0:
                x=board[j][i-1]
                board[j][i-1]=0
                if len(stack)==0:
                    stack.append(x)
                elif x==stack[-1]:
                    answer+=2
                    stack.pop(-1)
                else:
                    stack.append(x)
                break
    return answer