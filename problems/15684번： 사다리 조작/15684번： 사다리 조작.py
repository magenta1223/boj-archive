#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 15684                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/15684                         #+#        #+#      #+#     #
#     Solved: 2024-02-14 12:09:49 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N, M, H = map(int, input().split())
BOARD = [[False] * N for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    BOARD[a-1][b-1] = True
 
def check(h, board):
    for v in range(H):
        if board[v][h]:
            h += 1
        elif h > 0 and board[v][h-1]:
            h -= 1
    return h
 
def dfs(board, depth, x, y):
    global ANS
    if depth >= ANS:
        return
    if all(check(i, board) == i for i in range(N)):
        ANS = depth
        return
    if depth == 3 or y >= N - 1:
        return
    for a in range(x, H):
        for b in range(y, N - 1):
            if not board[a][b] and (b == 0 or not board[a][b - 1]) and (b == N - 2 or not board[a][b + 1]):
                board[a][b] = True
                dfs(board, depth + 1, a, b)
                board[a][b] = False
            y = 0  # 다음 줄부터는 처음부터 검사
 
ANS = 4
dfs(BOARD, 0, 0, 0)
print(ANS if ANS < 4 else -1)
 