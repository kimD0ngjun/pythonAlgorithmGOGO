import sys
from collections import defaultdict

# 입력 단계
N, M, inventory_blocks = map(int, input().split())
grid = []
height_count = defaultdict(int)

for _ in range(N):
    row = list(map(int, input().split()))
    grid.append(row)

    left = 0
    right = M - 1

    while left <= right:

        if left < right:
            height_count[row[left]] += 1
            height_count[row[right]] += 1
        else:
            height_count[row[left]] += 1

        left += 1
        right -= 1

height_list = sorted(list(height_count.keys()))

# print(height_count)
# print(height_list)

# 최소 시간과 최대 높이 초기화
"""
이전 문제에서 썼던 투 포인터를
반대로 동시에 높여가고 깎아 내려가는 과정을
동시에 담아서 중간의 만나는 지점 계산하기?
"""
min_seconds = sys.maxsize
high_height = 0

for height_level in range(257):
    # """
    # 제너레이터 표현식은 메모리를 효율적으로 사용하며, 특히 큰 데이터셋을 다룰 때 유리합니다.
    # 명시적인 반복문은 더 읽기 쉬운 코드를 작성할 수 있도록 도와주며, 복잡한 논리나 디버깅이 필요한 경우에 유리할 수 있습니다.
    #
    # max() 함수를 제너레이터 표현식에서 if문 대용으로 사용할 수 있음
    # """
    # # 제너레이터 표현식 기반
    # # 사용해야 되는 블록
    # # height_level 기준보다 낮으면 쌓아줘야 함
    # used_blocks = sum(max(0, height_level - height) for row in grid for height in row)
    # # 파헤쳐지는 블록
    # # height_level 기준보다 높으면 제거해야 함
    # dug_blocks = sum(max(0, height - height_level) for row in grid for height in row)
    used_blocks = 0
    dug_blocks = 0

    for height, count in height_count.items():
        if height < height_level:
            used_blocks += (height_level - height) * count
        elif height > height_level:
            dug_blocks += (height - height_level) * count

    # 사용해야 되는 블록 기준으로 시간 합산하기
    # 인벤토리 블록과 깎아 얻은 블록이 사용된 블록보다 많아야 사용이 가능하다는 것이므로
    # 사용해야 되는 블록이 더 많으면 그건 평탄화 작업이 불가능하다는 거
    if used_blocks <= dug_blocks + inventory_blocks:
        """
        블록 쌓는 데에 1초
        블록 파는 데에 2초
        """
        total_seconds = dug_blocks * 2 + used_blocks

        # total_seconds 계산값으로 최소 시간 업데이트 + 높이 지정
        # 높이 레벨마다 최소 시간을 계속 계산해서 동기화
        # 같은 시간이면 더 높은 애를 고르기 위한 반복문 분기 추가
        if total_seconds <= min_seconds:
            min_seconds = total_seconds
            high_height = height_level

print(min_seconds, high_height)