from collections import defaultdict
from typing import List


# 높이의 범위 : 가장 낮은 블록 ~ 가장 높은 블록
"""
1) 좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다. -> 2초
2) 인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다. -> 1초

최소 시간을 내려면 2번 작업을 우선 최대 수행, 1번 작업을 최소 수행
"""
# 풀이용 함수
def solution(grid: List[List[int]], count: defaultdict, blocks: int):
    # count에서 가장 많은 key 구하기
    max_value = max(count.values())
    max_blocks = sorted([key for key, value in count.items() if value == max_value], reverse=False)
    print("가장 많으면서 가장 높은 블록 : " + str(max_blocks))

    # 최대한 2번 작업(blocks)을 수행해서 쌓을 수 있는 거 전부 쌓기(+ 카운팅)
    """
    많은 애들 중, 낮은 애들의 높이에 맞춰 먼저 블록을 쌓아간다.
    
    반복문 while
    분기마다 가장 낮은(value가 가장 작은) 블록에게 채워줌
    최적화 방안 : 그 다음으로 낮은 블록을 찾기 위해서 value도 전부 리스트화시키기?
    
    비슷한 방법으로 깎아내려가는 것도 같은 방식으로
    """

    # 울퉁불퉁 튀어나온 블록들 깎아내기(+ 카운팅)

    pass



# 입력 처리
# N == 세로, M == 가로, B == block == 블록 개수
N, M, blocks = map(int, input().split())
grid = []
count = defaultdict(int) # 입력을 받음과 동시에 요소 개수 세리기

for _ in range(N):

    row = list(map(int, input().split()))
    grid.append(row)

    # 투 포인터로 요소 세리기
    left = 0
    right = M - 1

    while left <= right:
        if left != right:
            count[row[left]] += 1
            count[row[right]] += 1
        else:
            count[row[left]] += 1

        left += 1
        right -= 1

print("맵: " + str(grid))
print("개수: " + str(count))

# 정답 출력
solution(grid, count, blocks)


"""
https://www.acmicpc.net/problem/18111
"""