import sys

N, M, inventory_blocks = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 최소 시간과 최대 높이 초기화
"""
이전 문제에서 썼던 투 포인터를
반대로 동시에 높여가고 깎아 내려가는 과정을
동시에 담아서 중간의 만나는 지점 계산하기?
"""
min_seconds = sys.maxsize
high_height = 0
height_level = 0

while True:
    """
    제너레이터 표현식은 메모리를 효율적으로 사용하며, 특히 큰 데이터셋을 다룰 때 유리합니다. 
    명시적인 반복문은 더 읽기 쉬운 코드를 작성할 수 있도록 도와주며, 복잡한 논리나 디버깅이 필요한 경우에 유리할 수 있습니다.
    
    max() 함수를 제너레이터 표현식에서 if문 대용으로 사용할 수 있음 
    """
    # 제너레이터 표현식 기반
    # 사용해야 되는 블록
    # height_level 기준보다 낮으면 쌓아줘야 함
    used_blocks = sum(max(0, height_level - height) for row in grid for height in row)
    # 남아있는 블록
    # height_level 기준보다 높으면 제거해야 함
    remaining_blocks = sum(max(0, height - height_level) for row in grid for height in row)

    # 사용해야 되는 블록 기준으로 시간 합산하기
    if used_blocks <= remaining_blocks + inventory_blocks:
        """
        블록 쌓는 데에 1초
        블록 파는 데에 2초
        """
        total_seconds = remaining_blocks * 2 + used_blocks

        # total_seconds 계산값으로 최소 시간 업데이트 + 높이 지정
        if total_seconds <= min_seconds:
            min_seconds = total_seconds
            high_height = height_level

    height_level += 1

    # 문제 제시 범위 높이가 256이하 0 또는 자연수
    if height_level > 256:
        break

print(min_seconds, high_height)