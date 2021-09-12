# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/60062

from itertools import permutations

def solution(n, weak, dist):
    L = len(weak)
    cand = []
    weak_point = weak + [w + n for w in weak] # 원형 배열을 선형 배열로 구현

    for i, start in enumerate(weak):
        for friends in permutations(dist):
            cnt = 1
            position = start
            # 점검하는 친구 배치
            for friend in friends:
                position += friend
                # 끝 포인트까지 도달 못했을 때
                if position < weak_point[i + L - 1]:
                    cnt += 1 # 친구 더 투입
                    # 현재 위치보다 멀리 있는 취약지점 중 가장 가까운 위치로
                    position = [w for w in weak_point[i+1 : i+L] if w > position][0]
                else:  # 끝 포인트까지 도달
                    cand.append(cnt)
                    break

    return min(cand) if cand else -1