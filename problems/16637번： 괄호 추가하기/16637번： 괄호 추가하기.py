#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 16637                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/16637                         #+#        #+#      #+#     #
#     Solved: 2024-06-11 14:34:31 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def dfs(idx, res):
    global ans 
    if idx >= N+1:
        ans = max(ans, res)
        return 
    # 앞에서부터 순서대로 계산임. 
    
    # 괄호를 추가
    # 괄호 추가 가능?
    if idx+3 <= N:
        # 괄호 추가 
        next_res = eval( f"{res}{S[idx-1]}{eval(S[idx:idx+3])}")
        dfs(idx+4, next_res)
 
    next_res = eval( f"{res}{S[idx-1:idx+1]}")
    dfs(idx+2, next_res)
 
N=int(input())
S = "0+"+input()
N+=2
ans = -float("inf")
dfs(2, 0)
print(ans)