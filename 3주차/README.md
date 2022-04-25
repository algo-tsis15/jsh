#### **3주차 메모**



**LV2 구명보트 문제**

기존 코드 - list.pop() 사용

def solution(people, limit):

```python
answer=0
people.sort(reverse=True)
while people:
    now=people.pop(0)
    if len(people)==0:
        answer+=1
        break
    if now == limit:
        answer+=1
    else:
        for i in range(len(people)):
            if people[i]<=limit-now:
                people.pop(i)
                break
        answer+=1
return answer
```
효율성 개선 코드 - 인덱스로 처리

def solution(people, limit):

```python
answer=0
people.sort(reverse=True)
start,end=0,len(people)-1
while start<=end:
    if people[start]+people[end]<=limit:
        end-=1
    start+=1
    answer+=1
    
return answer
```