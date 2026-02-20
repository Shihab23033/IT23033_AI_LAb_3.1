import copy
import heapq
N=3
class p8_board:
    def __init__(self,board,x,y,depth,parent=None,h=0):
        self.board=board
        self.x=x
        self.y=y 
        self.parent=parent
        self.h=h
        self.depth=depth
    
    def __lt__(self,other):
        return self.h<other.h

moves=[(0,1),(0,-1),(1,0),(-1,0)]
goal=[[1,2,3],[4,5,6],[7,8,0]]

def manhattan(board):
  dist = 0
  for i in range(N):
    for j in range(N):
      val = board[i][j]
      if val != 0:
        f=1
        for row in range(N):
          for col in range(N):
            if val==goal[row][col]:
              dist += abs(i - row) + abs(j - col)
              f=0
              break
          if f==0:
            break
  return dist

def is_goal(board):
    return goal==board

def is_valid(x,y):
    return 0<=x<3 and 0<=y<3

def best(start_board,x,y):
    pq=[]
    visited=set()
    h=manhattan(start_board)
    start_tuple=tuple(map(tuple,start_board))
    visited.add(start_tuple)
    start_node=p8_board(start_board,x,y,0,None,h)
    heapq.heappush(pq,start_node)

    while pq:
        current=heapq.heappop(pq)
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
                    h=manhattan(new_board)
                    heapq.heappush(pq,p8_board(new_board,new_x,new_y,current.depth+1,current,h))
    print("solution not found")

def prints(node):
    current=node
    path=[]
    while current!=None:
        path.append(current)
        current=current.parent
    path.reverse()
    for i,step in enumerate(path):
        print(f"step {i}")
        for j in step.board:
            print(j)
        print()



start=[[1,2,3],[4,0,5],[7,8,6]]
x,y=1,1
print("solving with best first search")
best(start,x,y)
