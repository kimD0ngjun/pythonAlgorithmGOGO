from typing import List


# 출력 함수 작성
def solution(points: List, new_point: int, point_range: int):
    """
    우선, 정렬된 배열의 마지막 인덱스 요소와 값이 같으면 -1을 반환한다.
    """
    if points[len(points)-1] == new_point and point_range == len(points):
        print(-1)
        return

    # 추가 할당 및 함수 내림차순 정렬
    points.append(new_point)
    points.sort(reverse=True)
    # print(points)

    """
    또한, 정렬된 배열의 마지막 인덱스 요소의 값이 되면 -1을 반환한다.
    """
    if points[len(points)-1] == new_point and point_range + 1 == len(points):
        print(-1)
        return

    # 배열을 [요소, 등수(인덱스+1)] 형식으로 바꿈
    index_arr = list(map(lambda x: [x[1], x[0]+1], enumerate(points)))
    # print(index_arr)

    # 투 포인터 사용해서 최적화하기
    left = 0
    right = 1

    while right < len(index_arr):
        sequence = index_arr[left][1]

        # 만약 내림차순 순서대로 가다가 같은 요소들을 만나면
        while True:

            if index_arr[left][0] == index_arr[right][0]:
                # 내부 리스트의 인덱스 1인 등수 바꾸기
                index_arr[right][1] = sequence
                right += 1

                if right >= len(index_arr):
                    break
            else:
                break

        left = right
        right += 1

    # print(index_arr)
    # 여기겠다
    new_index = 0

    while new_index < len(index_arr):
        if index_arr[new_index][0] == new_point:
            print(index_arr[new_index][1])
            break

        new_index += 1



# 입력 처리
"""
N == count
태수의 새로운 점수 == new_point
P == point_range
"""
count, new_point, point_range = map(int, input().split())


if count == 0:
    print(1)
else:
    points = list(map(int, input().split()))
    # 정답 출력
    solution(points, new_point, point_range)

"""
반례 : right의 인덱스에러 문제

ex)
4 1 10
0 0 0 0
"""