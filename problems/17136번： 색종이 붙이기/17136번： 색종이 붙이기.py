#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 17136                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/17136                         #+#        #+#      #+#     #
#     Solved: 2024-04-01 15:01:20 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

A = [list(map(int, input().split())) for _ in range(10)] 
 
def cover(arr, i,j,s):
    for _i in range(i, i+s):
        for _j in range(j, j+s):
            arr[_i][_j] = 0
    return arr 
 
def recover(arr, i,j,s):
    for _i in range(i, i+s):
        for _j in range(j, j+s):
            # print(i,j)
            arr[_i][_j] = 1
    return arr 
 
def coverable(arr,i,j,s):
    for row in arr[i:i+s]:
        if sum(row[j:j+s]) != s:
            return False 
    return True 
 
C = {i : 0 for i in range(1,6)}
 
 
def dfs(arr, c, start_i, start_j):
    global ans
    # 모든 1을 덮었는지 확인
    covered = True
    for i in range(start_i, 10):
        for j in range(start_j if i == start_i else 0, 10):
            if arr[i][j] == 1:
                covered = False
                start_i, start_j = i, j
                break
        if not covered:
            break
    
    if covered:
        ans = min(ans, sum(c.values()))
        return
    
    if sum(c.values()) >= ans:
        return  # 가지치기
 
    for s in range(5, 0, -1):  # 가장 큰 조각부터 시도
        if i + s <= 10 and j + s <= 10 and c[s] < 5 and coverable(arr, i, j, s):
            cover(arr, i, j, s)
            c[s] += 1
            dfs(arr, c, start_i, start_j)  # 다음 탐색 시작
            recover(arr, i, j, s)
            c[s] -= 1
 
ans = 26
dfs(A,C,0,0)
print(ans if ans <= 25 else -1)