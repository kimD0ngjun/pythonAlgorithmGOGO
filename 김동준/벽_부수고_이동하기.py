from collections import deque


# 풀이 최적화를 위한 함수 생성
def pathfinder(maze):
    # 코드에서의 좌표 개념 : (상하, 좌우)
    # 이중 리스트에서의 상하좌우이므로 상하는 겉 리스트의 인덱스, 좌우는 내부 리스트의 인덱스
    # 백트랙킹에 벽 뚫기가 추가돼서 벽 탐지 로직에 건너편 역시 탐색해야 함

    dx = [1, -1, 0, 0]  # 상하
    dy = [0, 0, -1, 1]  # 좌우

    # 벽 + 왔던 길 : 0, 길 : 1
    # 튜플 : (x, y, distance)
    queue = deque()
    queue.append((0, 0, 1))

    while queue:
        x, y, distance = queue.popleft()

        # 팝된 상태에서 추가된 경로 방향 확인 여부
        prev_length = len(queue)

        # 팝했을 때 종점(N, M)에 도착했다면
        if x == len(maze) - 1 and y == len(maze[0]) - 1:
            return distance

        # 네 방향
        for i in range(4):

            next_x = x + dx[i]
            next_y = y + dy[i]

            # 백트랙킹 조건
            # 맵 이탈
            if not (0 <= next_x < len(maze) and 0 <= next_y < len(maze[0])):
                continue

            # 전제조건: 사방이 벽(1)이어야 함
            if maze[next_x][next_y] == 1:
                continue

            # 방문 처리
            if maze[next_x][next_y] == 0:
                # 방문했으면 다시 벽 처리
                maze[next_x][next_y] = 1

                # 큐에 append 되면서 길이 변화
                queue.append((next_x, next_y, distance + 1))

        post_length = len(queue)

        # 처음 탐색한 네 방향 전부 벽일때,
        # 즉, 큐에 append 된 게 없을 때. 즉, prev_length가 변함이 없을 때
        # 건너편이 1인지를 보는 로직이 추가로 필요
        if prev_length == post_length:

            next_dx = [2, -2, 0, 0]  # 상하
            next_dy = [0, 0, -2, 2]  # 좌우

            for i in range(4):
                double_next_x = x + next_dx[i]
                double_next_y = y + next_dy[i]

                # 맵 이탈
                if not (0 <= double_next_x < len(maze) and 0 <= double_next_y < len(maze[0])):
                    continue

                # 건너도 벽
                if maze[double_next_x][double_next_y] == 1:
                    continue

                if maze[double_next_x][double_next_y] == 0:
                    maze[double_next_x][double_next_y] = 1
                    queue.append((double_next_x, double_next_y, distance + 2))

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

"""