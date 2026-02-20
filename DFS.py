import copy
class  p8_board:
    def __init__(self,board,x,y,depth,parent=None):
        self.board=board
        self.x=x 
        self.y=y 
        self.depth=depth
        self.parent=parent

moves=[(0,1),(0,-1),(1,0),(-1,0)]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]] 
def is_goal(board):
    return goal==board
def is_valid(x,y):
    return 0<=x<3 and 0<=y<3

def dfs_solve(start_board,x,y):
    stack=[]
    start_tuple=tuple(map(tuple,start_board))
    visited=set()
    stack.append(p8_board(start_board,x,y,0))
    visited.add(start_tuple)
    while stack:
        current=stack.pop()
        if is_goal(current.board):
            print("solution found")
            prints(current)
            return
        for x,y in moves:
            new_x=current.x+x
            new_y=current.y+y
            if(is_valid(new_x,new_y)):
                new_board=copy.deepcopy(current.board)
                new_board[current.x][current.y],new_board[new_x][new_y]=\
                new_board[new_x][new_y],new_board[current.x][current.y]
                board_tuple=tuple(map(tuple,new_board))
                if board_tuple not in visited:
                    visited.add(board_tuple)
                    stack.append(p8_board(new_board,new_x,new_y,current.depth+1,current))
    print("No solution found")

def prints(node):
    path=[]
    current=node
    while current is not None:
        path.append(current)
        current=current.parent
    path.reverse()
    for i,steps in enumerate(path):
        print(f"Step {i}")
        for r in steps.board:
            print(r)
        print()

start=[[1,2,3],[4,0,5],[7,8,6]]
x,y=1,1
print("solving with dfs")
dfs_solve(start,x,y)
