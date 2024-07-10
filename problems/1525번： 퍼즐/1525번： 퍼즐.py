#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1525                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1525                          #+#        #+#      #+#     #
#     Solved: 2024-07-10 05:11:02 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #



# 정렬된 상태에 이르는 최소 횟수 
# 가능한 가짓수는 9! = 36만가지 

from math import factorial 
from collections import deque 

def arr2idx(arr):
    idx = 0 
    nums = list(range(9))
    for i in range(3):
        for j in range(3):
            _nidx = nums.index(arr[i][j])
            idx += fcts[i*3+j]*_nidx
            del nums[_nidx]
    return idx 
            
def idx2arr(idx):
    arr = [[0] * 3 for _ in range(3)]
    nums = list(range(9))
    for i in range(9):
        v, idx = divmod(idx, fcts[i])
        x,y = divmod(i, 3)
        arr[x][y] = nums[v]
        del nums[v]
    return arr 

D = [(-1,0), (0,1), (1,0), (0,-1)]
A = [list(map(int,input().split())) for _ in range(3)]
dp = [-1] * factorial(9)
fcts = [factorial(i) for i in range(8,-1,-1)]
dst = arr2idx([[1,2,3], [4,5,6], [7,8,0]])

for i in range(3):
    for j in range(3):
        if not A[i][j]:
            x,y = i,j 

arridx = arr2idx(A)
q = deque([(x, y, arridx, 0)])
dp[arridx] = 0 
done = False 

if dst == arridx:
    print(0)
    exit()

while q and not done:
    x, y, arr, d = q.popleft()
    for dx, dy in D:
        nx,ny = x+dx, y+dy 
        if 0<=nx<3 and 0<=ny<3:
            _arr = idx2arr(arr)
            _arr[nx][ny], _arr[x][y] = _arr[x][y], _arr[nx][ny]
            arridx = arr2idx(_arr)
            if dp[arridx] == -1:
                dp[arridx] = d+1 
                q.append((nx,ny,arridx,d+1))
                if arridx == dst:
                    done = True 
                    break 
print(dp[dst])


