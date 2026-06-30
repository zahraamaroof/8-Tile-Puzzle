import heapq

goal = ((1,2,3),
        (4,5,6),
        (7,8,0))

moves = [(-1,0),(1,0),(0,-1),(0,1)]


def manhattan(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x = (value-1)//3
                goal_y = (value-1)%3
                distance += abs(i-goal_x)+abs(j-goal_y)
    return distance


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j]==0:
                return i,j


def neighbors(state):
    x,y = find_blank(state)
    result=[]

    for dx,dy in moves:
        nx,ny=x+dx,y+dy
        if 0<=nx<3 and 0<=ny<3:
            temp=[list(row) for row in state]
            temp[x][y],temp[nx][ny]=temp[nx][ny],temp[x][y]
            result.append(tuple(tuple(row) for row in temp))

    return result


def greedy(start):
    pq=[]
    heapq.heappush(pq,(manhattan(start),start))

    visited=set()

    while pq:
        h,state=heapq.heappop(pq)

        if state==goal:
            print("Goal Reached!")
            return

        if state in visited:
            continue

        visited.add(state)

        print(state)

        for nxt in neighbors(state):
            if nxt not in visited:
                heapq.heappush(pq,(manhattan(nxt),nxt))

    print("No Solution")


start=((1,2,3),
       (4,0,6),
       (7,5,8))

greedy(start)