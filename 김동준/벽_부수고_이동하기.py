from collections import deque
import copy


# 풀이 최적화를 위한 함수 생성
def pathfinder(maze):
    # 코드에서의 좌표 개념 : (상하, 좌우)
    # 이중 리스트에서의 상하좌우이므로 상하는 겉 리스트의 인덱스, 좌우는 내부 리스트의 인덱스
    # 백트랙킹에 벽 뚫기가 추가돼서 벽 탐지 로직에 건너편 역시 탐색해야 함

    dx = [1, -1, 0, 0]  # 상하
    dy = [0, 0, -1, 1]  # 좌우

    # 벽 + 왔던 길 : 0, 길 : 1
    # 튜플 : (x, y, distance, 경로)
    # 경로 공유가 안 되도록 지도도 슬라이싱으로 복사해서 새로운 지도 할당시키기
    queue = deque()
    queue.append((0, 0, 1, maze))

    while queue:
        x, y, distance, prev_maze = queue.popleft()

        # 새로운 경로 할당
        new_maze = copy.deepcopy(prev_maze)

        # 팝 지점 방문 처리
        new_maze[x][y] = 1
        # 팝 지점의 사방 좌표 확인용
        four_points = []
        # 추가 탐색 필요 여부 변수
        need_search = True

        # 팝했을 때 종점(N, M)에 도착했다면
        if x == len(maze) - 1 and y == len(maze[0]) - 1:
            return distance

        # 네 방향
        for i in range(4):

            next_x = x + dx[i]
            next_y = y + dy[i]

            four_points.append((next_x, next_y))

            # 백트랙킹 조건
            # 맵 이탈
            if not (0 <= next_x < len(maze) and 0 <= next_y < len(maze[0])):
                continue

            # 전제조건: 사방이 벽(1)이어야 함
            if new_maze[next_x][next_y] == 1:
                continue

            # 방문 처리
            if new_maze[next_x][next_y] == 0:
                # 방문했으면 다시 벽 처리
                new_maze[next_x][next_y] = 1
                # 큐에 append 되면서 길이 변화
                queue.append((next_x, next_y, distance + 1, new_maze))
                # 추가 탐색 불필요
                need_search = False

        # 처음 탐색한 네 방향 전부 벽일때(즉 네 방향 전부 탐색이 완료됐고),
        # 건너편 추가 탐색점이 1인지를 보는 로직이 추가로 필요
        if need_search:

            for point in four_points:
                point_x, point_y = point

                # 백트랙킹 조건
                # 맵 이탈
                if not (0 <= point_x < len(maze) and 0 <= point_y < len(maze[0])):
                    continue

                for i in range(4):

                    point_next_x = point_x + dx[i]
                    point_next_y = point_y + dy[i]

                    # 백트랙킹 조건
                    # 맵 이탈
                    if not (0 <= point_next_x < len(maze) and 0 <= point_next_y < len(maze[0])):
                        continue

                    # 추가 탐색지점조차 벽이라면 더이상 탐색 x
                    if new_maze[point_next_x][point_next_y] == 1:
                        continue

                    # 추가 탐색지점이 길(0)이라면
                    if new_maze[point_next_x][point_next_y] == 0:
                        # 방문했으면 다시 벽 처리
                        new_maze[point_next_x][point_next_y] = 1

                        # 길이는 2배
                        queue.append((point_next_x, point_next_y, distance + 2, new_maze))

    # 큐가 비워질 때까지 종점의 좌표를 팝하지 못하면 그건 길이 막혔다는 뜻
    return -1


# 입력 단계
N, M = map(int, input().split())

maze = []

for _ in range(N):
    maze.append(list(map(int, input())))

# print("N:" + str(N))
# print("M:" + str(M))
# print(maze)

# 정답 출력
print(pathfinder(maze))



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