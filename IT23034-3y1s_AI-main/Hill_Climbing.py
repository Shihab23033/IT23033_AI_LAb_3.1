import copy

N = 3

class p8_board:
    def __init__(self, board, x, y, depth=0, parent=None):
        self.board = board
        self.x = x
        self.y = y
        self.depth = depth
        self.parent = parent

row_moves = [0, 0, -1, 1]
col_moves = [-1, 1, 0, 0]

def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N

def is_goal(board):
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return goal == board

def heuristic(board):
    h = 0
    for i in range(3):
        for j in range(3):
            val = board[i][j]
            if val != 0:
                gx = (val - 1) // 3
                gy = (val - 1) % 3
                h += abs(i - gx) + abs(j - gy)
    return h

def hill_climbing(start_board, x, y):
    current = p8_board(start_board, x, y)
    current_h = heuristic(current.board)
    step = 0

    while True:
        if is_goal(current.board):
            prints(current)
            return

        neighbors = []

        for i in range(4):
            new_x = current.x + row_moves[i]
            new_y = current.y + col_moves[i]

            if is_valid(new_x, new_y):
                new_board = copy.deepcopy(current.board)
                new_board[current.x][current.y], new_board[new_x][new_y] = \
                    new_board[new_x][new_y], new_board[current.x][current.y]

                h = heuristic(new_board)
                neighbors.append((h, new_board, new_x, new_y))

        best = neighbors[0]
        for item in neighbors:
            if item[0] < best[0]:
                best = item

        best_h = best[0]
        best_board = best[1]
        bx = best[2]
        by = best[3]

        if best_h >= current_h:
            print("Stuck at plateau!")
            return

        current = p8_board(best_board, bx, by, current.depth + 1, current)
        current_h = best_h
        step += 1

def prints(node):
    path = []
    current = node
    while current is not None:
        path.append(current)
        current = current.parent
    path.reverse()
    for i, step in enumerate(path):
        print(f"Step {i}")
        for r in step.board:
            print(r)
        print()
    print("Goal reached!")

start = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
x, y = 1, 1
print("Solving with Hill Climbing...")
hill_climbing(start, x, y)
