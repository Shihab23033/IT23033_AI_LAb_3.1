import copy
import heapq

N = 3

class p8_board:
    def __init__(self, board, x, y, depth, parent=None, cost=0):
        self.board = board
        self.x = x
        self.y = y
        self.depth = depth
        self.parent = parent
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

row_moves = [0, 0, -1, 1]
col_moves = [-1, 1, 0, 0]

def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N

def is_goal(board):
    return board == [[1,2,3],[4,5,6],[7,8,0]]

def heuristic(board):
    h = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                gx = (board[i][j] - 1) // N
                gy = (board[i][j] - 1) % N
                h += abs(i - gx) + abs(j - gy)
    return h

def aostar(start_board, x, y):
    pq = []
    visited = set()

    h = heuristic(start_board)
    start = p8_board(start_board, x, y, 0, None, h)
    heapq.heappush(pq, start)

    while pq:
        current = heapq.heappop(pq)
        if is_goal(current.board):
            prints(current)
            return

        visited.add(tuple(map(tuple, current.board)))
        children = []
        for i in range(4):
            nx = current.x + row_moves[i]
            ny = current.y + col_moves[i]
            if is_valid(nx, ny):
                new_board = copy.deepcopy(current.board)
                new_board[current.x][current.y], new_board[nx][ny] = \
                    new_board[nx][ny], new_board[current.x][current.y]
                bt = tuple(map(tuple, new_board))
                if bt not in visited:
                    cost = current.depth + 1 + heuristic(new_board)
                    children.append(p8_board(new_board, nx, ny, current.depth + 1, current, cost))
        if children:
            best_child = children[0]
            for child in children:
                if child.cost < best_child.cost:
                    best_child = child
            heapq.heappush(pq, best_child)
    print("NO solution found")

def prints(node):
    path = []
    while node:
        path.append(node)
        node = node.parent
    path.reverse()
    for i, step in enumerate(path):
        print(f"Step {i}")
        for r in step.board:
            print(r)
        print()
start = [[1,2,3],[4,0,5],[7,8,6]]
x, y = 1, 1
print("Solving with AO* Search...")
aostar(start, x, y)
