#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2239                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2239                          #+#        #+#      #+#     #
#     Solved: 2024-04-05 14:55:31 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

A = [list(map(int,list(input().strip()))) for _ in range(9)]
FULL = set([i for i in range(1,10)])
BLOCKS = {
    (0,0) : 0, (0,1) : 1, (0,2) : 2,
    (1,0) : 3, (1,1) : 4, (1,2) : 5,
    (2,0) : 6, (2,1) : 7, (2,2) : 8,
}
 
rows =  [set(row) - set([0]) for row in A]
cols = [set(row) - set([0]) for row in zip(*A)]
blocks = [set() for _ in range(9)] 
zeros = []
for i in range(9):
    for j in range(9):
        if A[i][j]:
            blocks[BLOCKS[(i//3, j//3)]].add(A[i][j])
        else:
            zeros.append((i,j))
 
def dfs(idx, arr, rows, cols, blocks):
    if idx == len(zeros):
        print(*["".join(map(str, row)) for row in arr], sep='\n')
        exit(0)
 
 
    i,j = zeros[idx]
    block_idx = BLOCKS[(i//3, j//3)]
    available = FULL - rows[i] - cols[j] - blocks[block_idx]
    for k in available:
        arr[i][j] = k 
        rows[i].add(k)
        cols[j].add(k)
        blocks[block_idx].add(k)
        
        dfs(idx+1, arr, rows, cols, blocks)
        arr[i][j] = 0 
        rows[i].remove(k)
        cols[j].remove(k)
        blocks[block_idx].remove(k)
 
dfs(0, A, rows, cols, blocks)