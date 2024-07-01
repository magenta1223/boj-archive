#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1062                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1062                          #+#        #+#      #+#     #
#     Solved: 2024-04-01 16:48:24 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from string import ascii_lowercase
 
def word2bitmask(w):
    bitmask = 0
    for char in set(w):
        bitmask |= (1 << ascii_lowercase.index(char))
    return bitmask 
 
N, K = map(int, input().split())
words = [word2bitmask(input().strip()) for _ in range(N)]
ans = 0
K -= 5
def dfs(idx, k, learned):
    global ans
    if k == K:
        ans = max(ans, sum([1 for w in words if w & learned == w]))
        return
    for i in range(idx, 26):
        if not learned & (1<<i):
            dfs(i+1, k+1, learned | (1<<i))
 
dfs(0, 0, word2bitmask("acint"))
print(ans)