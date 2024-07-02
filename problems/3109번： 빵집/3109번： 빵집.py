#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 3109                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/3109                          #+#        #+#      #+#     #
#     Solved: 2024-07-02 08:58:56 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# 그리디? 
# 가능한한 위로 붙여서 진행하면 될듯

# dfs+greedy 
# 1. route별로 출발
# 2. 최대 길이는 C의 길이
# 3. 최대한 위로 붙여본다
# 4. 가다가 안되면 -> 위로 실패신호 전달. 전부 취소
# 5. 가다가 되면-> 성공신호 전달. 전부 반영? 

input = open(0).readline

R,C = map(int,input().split())
A = [list(input().strip()) for _ in range(R)]

def dfs(r, c):
    global ans 
    if c == C-1:
        ans += 1
        return True 
    
    if visited[r][c] == -1:
        return False 

    for nr in [r-1, r, r+1]:
        if not 0<= nr < R or visited[nr][c+1] or A[nr][c+1] == "x":
            continue 
        if dfs(nr, c+1):
            visited[nr][c+1] = 1 
            return True
        else:
            visited[nr][c+1] = -1 
    return False 
    
visited = [[0] *C for _ in range(R)]

ans = 0

for i in range(R):
    visited[i][0] = 1 
    dfs(i,0)
print(ans)



print(*visited, sep = '\n')
    
print(ans)

"""
"""