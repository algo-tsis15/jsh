from itertools import combinations


def solution(relation):
    row = len(relation)
    col = len(relation[0])
    combs = []  # 릴레이션 속성의 조합

    # lenght 자리만큼 range(col) 조합 생성 후 combs 삽입
    #	[(0,), (1,), (2,), (3,), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3), (0, 1, 2), (0, 1, 3), (0, 2, 3),
    #	(1,2, 3), (0, 1, 2, 3)]
    for length in range(1, col + 1):
        combs.extend(combinations(range(col), length))

        # 유일성 검사 (tuple 활용)
    unique = []
    for comb in combs:
        tmp = [tuple([r[idx] for idx in comb]) for r in relation]
        if len(set(tmp)) == row:  # 유일성 만족
            isUnique = True
            for u in unique:
                if set(u).issubset(set(comb)):  # 최소성 검사
                    isUnique = False
                    break
            if isUnique:
                unique.append(comb)
    return len(unique)