#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 14889                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/14889                         #+#        #+#      #+#     #
#     Solved: 2023-12-18 19:09:01 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int, input().split())))
total = sum([ sum(row) for row in S])
peoples = [i for i in range(N)]
results = []
 
def dfs(start, depth):
    if depth == N // 2:
        link = [p for p in peoples if p not in start]
        A = sum([S[i][j] for j in start for i in start])
        B = sum([S[i][j] for j in link for i in link])        
        if abs(A - B) == 0:
            print(0)
            exit(0)
        results.append(abs(A - B))
    else:
        # for i in range(len(peoples)):
        for i in range(start[-1]+1, N):
            s=peoples[i]
            dfs(start + [s], depth+1)
dfs([0], 1)
 
print(min(results))