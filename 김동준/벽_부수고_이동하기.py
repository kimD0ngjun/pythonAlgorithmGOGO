from collections import deque
import copy


class Solution:
    # 풀이 최적화를 위한 함수 생성
    def pathfinder(self):
        # 코드에서의 좌표 개념 : (상하, 좌우)
        # 이중 리스트에서의 상하좌우이므로 상하는 겉 리스트의 인덱스, 좌우는 내부 리스트의 인덱스
        # 백트랙킹에 벽 뚫기가 추가돼서 벽 탐지 로직에 건너편 역시 탐색해야 함

        dx = [1, -1, 0, 0]  # 상하
        dy = [0, 0, -1, 1]  # 좌우

        # 벽 + 왔던 길 : 0, 길 : 1
        # 튜플 : (x, y, broken(벽 부쉈는지 여부))
        # 경로 공유가 안 되도록 지도도 슬라이싱으로 복사해서 새로운 지도 할당시키기
        queue = deque()
        queue.append((0, 0, 0))

        while queue:
            x, y, broken = queue.popleft()

            # 팝했을 때 종점(N, M)에 도착했다면
            if x == len(maze) - 1 and y == len(maze[0]) - 1:
                return visited[x][y][broken]

            # 네 방향
            for i in range(4):

                next_x = x + dx[i]
                next_y = y + dy[i]

                # 백트랙킹 조건
                # 맵 이탈
                if not (0 <= next_x < len(maze) and 0 <= next_y < len(maze[0])):
                    continue

                """
                1. 다음 이동지점이 벽 and 벽인데 아직 벽 안 부숨
                2. 다음 이동지점이 벽 x and 아직 방문 안됨
                
                그냥 문제 조건이 벽 한 번만 부술 수 있다... 였음; 개빡
                """

                # 1번
                if maze[next_x][next_y] == 1 and broken == 0:
                    visited[next_x][next_y][1] = visited[x][y][0] + 1
                    queue.append((next_x, next_y, 1))

                # 2번
                # 현재까지의 경로에서 벽을 부순 상태 혹은 안 부순 상태 그대로 유지하면서 이동
                if maze[next_x][next_y] == 0 and visited[next_x][next_y][broken] == 0:
                    visited[next_x][next_y][broken] = visited[x][y][broken] + 1
                    queue.append((next_x, next_y, broken))

        # 큐가 비워질 때까지 종점의 좌표를 팝하지 못하면 그건 길이 막혔다는 뜻
        return -1


# 입력 단계
N, M = map(int, input().split())

maze = []

for _ in range(N):
    maze.append(list(map(int, input())))

# 3차원 리스트
# 가장 내부의 리스트는 벽 부순 경로 계산과 벽 안 부순 경로 계산 따로따로
# 튜플을 쓰지 않은건 업데이트가 필요하기 때문
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

# 정답 출력
s = Solution()
print(s.pathfinder())



"""
예제 입출력은 전부 성공되나 터지는 이유?

01
10

이런 케이스에서 벽을 부순 다음 통과 처리가 되어야 하나?
즉, 벽을 부수면 상식적으로 출발점과 도착점이 이어지니까 맞다고 봐야 되는데
지금 내 풀이에서는 저런 케이스도 통과 안 되고 -1 반환시키게 했으니 틀렸다고 뜨는 거 같은데?
아닌가

01
10
10

이런 케이스도 통과여야 되는데 불통과처리돼서 오답 처리인 것 같은데

수정한 풀이 문제 확인
경로 공유로 인한 벽뚫기 케이스 혼동 발생

"""