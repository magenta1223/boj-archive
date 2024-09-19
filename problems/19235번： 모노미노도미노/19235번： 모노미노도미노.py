#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 19235                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/19235                         #+#        #+#      #+#     #
#     Solved: 2024-09-19 01:08:11 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


from collections import deque 
input = open(0).readline 
N = int(input())
G,B = [[0] * 4 for _ in range(6)], [[0] * 4 for _ in range(6)]
D = [(-1,0),(0,1),(1,0),(0,-1)]
tFlip = [0,1,3,2]

def can_fall(cells, board):
    for x, y, _ in cells:
        if x<5 and not board[x+1][y]:
            continue
        return False
    return True

def find_blocks(board, rowmax):
    visited = [[0] * 4 for _ in range(6)]
    cells = []
    for i in range(rowmax-1,-1,-1):
        for j in range(4):
            if not board[i][j] or visited[i][j]:
                continue 
            block_id = board[i][j]
            q, _cells = deque([(i,j)]), [(i,j,block_id)]
            visited[i][j] = 1 
            while q:
                x,y=q.popleft()
                for dx,dy in D:
                    nx,ny = x+dx,y+dy 
                    if 0<=nx<6 and 0<=ny<4 and block_id == board[nx][ny] and not visited[nx][ny]:
                        q.append((nx,ny))
                        _cells.append((nx,ny,block_id))
                        visited[nx][ny] = 1
            for x,y,_ in _cells:
                board[x][y] = 0 
            cells.append(_cells)
    return cells 

def getScore(board):
    score, rowmax = 0, 0 
    for i in range(6):
        if all(board[i]):
            board[i] = [0] * 4
            rowmax = i
            score += 1 
    return score, rowmax 


def fall(board,t,y,block_id):
    if t==1:
        cells = [(1,y,block_id)]
    elif t==2:
        cells = [(1,y,block_id), (1,y+1,block_id)]
    else:
        cells = [(0,y,block_id), (1,y,block_id)] 
    score = 0 
    while can_fall(cells, board):
        cells = [(x+1,y,_id) for x,y,_id in cells]
    for x,y,_id in cells:
        board[x][y] = _id 

    while True:
        _score, rowmax = getScore(board)
        if not _score:
            break 
        score += _score 
        for cells in find_blocks(board, rowmax):
            while can_fall(cells, board):
                cells = [(x+1,y,_id) for x,y,_id in cells]
            for x,y,_id in cells:
                board[x][y] = _id 

    # 밀어내기 
    while sum(board[1]):
        board = [[0] * 4] + board[:-1]

    return score, board 

ans = 0 
debug = False  
for i in range(N):
    t,x,y = map(int,input().split())

    score_green,G = fall(G,t,y,i+1)
    score_blue,B = fall(B,tFlip[t],x,i+1)
    

    ans += score_green + score_blue 

    
    if debug:
        print('ROUND', i+1)
        print("GREEN")
        print(*G, sep = '\n')
        print("Blue")
        print(*B, sep='\n')
        print()

print(ans)
print(sum([4-row.count(0) for row in G]) + sum([4-row.count(0) for row in B]))



"""
6
2 0 1
2 1 1
3 2 3
3 2 1
3 0 0
1 0 1


"""