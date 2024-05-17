import heapq
from typing import List


# 출력 함수 작성
def solution(points: List, new_point: int):
    # 함수 내림차순 정렬
    points.sort(reverse=True)
    print(points)

    # 최적화(-1 리턴)
    # 여기서 틀렸네
    if points.index(new_point) >= len(points) - 2:
        print(-1)
        return

    # 배열을 [요소, 등수(인덱스+1)] 형식으로 바꿈
    index_arr = list(map(lambda x: [x[1], x[0]+1], enumerate(points)))
    print(index_arr)

    # 투 포인터 사용해서 최적화하기
    left = 0
    right = 1

    while right <= len(index_arr)-1:
        sequence = index_arr[left][1]

        # 만약 내림차순 순서대로 가다가 같은 요소들을 만나면
        while True:

            if index_arr[left][0] == index_arr[right][0]:
                # 내부 리스트의 인덱스 1인 등수 바꾸기
                index_arr[right][1] = sequence
                right += 1
            else:
                break

        left = right
        right += 1

    print(index_arr)
    print(points.index(new_point) + 1)



# 입력 처리
"""
N == count
태수의 새로운 점수 == new_point
P == point_range
"""
count, new_point, point_range = map(int, input().split())

points = list(map(int, input().split()))

# 추가 할당
points.append(new_point)

# 정답 출력
solution(points, new_point)