import heapq # 최소힙 형태(가장 큰 값을 감소시키는 풀이에 맞는 자료구조)

def solution(n, works):
    if sum(works)<n:
        return 0
    works=[-i for i in works] # 최대힙 형태로 변환
    heapq.heapify(works)
    while n>0:
        min_value=heapq.heappop(works)
        min_value+=1
        heapq.heappush(works,min_value)
        n-=1
    return sum([i**2 for i in works])


