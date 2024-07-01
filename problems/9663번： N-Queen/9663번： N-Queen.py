#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 9663                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/9663                          #+#        #+#      #+#     #
#     Solved: 2023-11-28 15:00:30 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline
 
def check(x):
    for i in range(x):
        if rows[x] == rows[i] or abs(rows[x] - rows[i]) == x - i:
            return False
    return True
 
def dfs(x):
    global cnt
 
    if x == n:
        cnt += 1
        return
 
    for i in range(n):
        if visited[i]: 
            continue
 
        rows[x] = i
        if check(x):
            visited[i] = True
            dfs(x+1)
            visited[i] = False
 
n = int(input())
rows = [0] * n
visited = [False] * n
cnt = 0
 
dfs(0)
print(cnt)