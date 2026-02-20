import copy
from collections import deque

class p8_board:
    def __init__(self,board,x,y,depth,parent=None):
        self.board=board
        self.x=x 
        self.y=y 
        self.depth=depth
        self.parent=parent

moves=[(0,1),(0,-1),(1,0),(-1,0)]

def is_valid(x,y):
    return 0<=x<3 and 0<=y<3

def is_goal(board):
    goal=[[1,2,3],[4,5,6],[7,8,0]]
    return goal==board

def bfs_solve(start_board,x,y):
    queue=deque()
    visited=set()
    queue.append(p8_board(start_board,x,y,0))
    start_tuple=tuple(map(tuple,start_board))
    visited.add(start_tuple)
    
    while queue:
        current=queue.popleft()
        if is_goal(current.board):
            print("solution found")
            prints(current)
            return
        for x,y in moves:
            new_x=current.x+x
            new_y=current.y+y
            if is_valid(new_x,new_y):
                new_board=copy.deepcopy(current.board)
                new_board[current.x][current.y],new_board[new_x][new_y]=\
                new_board[new_x][new_y],new_board[current.x][current.y]
                board_tuple=tuple(map(tuple,new_board))
                if board_tuple not in visited:
                    
                    visited.add(board_tuple)
                    queue.append(p8_board(new_board,new_x,new_y,current.depth+1,current))
    print("solution not found")

def prints(board):
    path=[]
    current=board
    while current is not None:
        path.append(current)
        current=current.parent
    path.reverse()

    for i,steps in enumerate(path):
        print(f"step {i}")
        for j in steps.board:
            print(j)
        print()


start=[[1,2,3],[4,0,5],[7,8,6]]
x,y=1,1
print("solving with bfs")
bfs_solve(start,x,y)
