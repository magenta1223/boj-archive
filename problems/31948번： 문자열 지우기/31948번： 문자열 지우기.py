#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 31948                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/31948                         #+#        #+#      #+#     #
#     Solved: 2024-07-11 04:31:56 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# 0,1,? 로 구성됨
# 할 수 있는 행동은 
# 가장 앞/뒤에서부터 연속된 숫자를 1개 이상 지우기
# 문자열의 ?하나를 0 or 1로 바꾸기 


# A와 B가 번갈아서 수행
# 더 이상 할 수 있는 행동이 없으면 패배
# A가 이기면 1 아니면 0 

# 길이는 1500 이하, ?는 2개 이하 


import sys 
sys.setrecursionlimit(2000)

# recursion이 딸려서 뭔가 이상한 값을 뱉는 것 같은데 .. 


input = open(0).readline

S = input().strip()
N = len(S)


qmIndices = [i for i in range(len(S)) if S[i] == "?"]
nQm = len(qmIndices)
# left, right, qmState 
dp = [[[-1] * (3**nQm)  for _ in range(N+1)]  for _ in range(N+1)]


def dfs(l:int, r:int, qms:int):
    global S 

    if dp[l][r][qms] != -1:
        return dp[l][r][qms]
    

    if l == r:
        dp[l][r][qms] = 0 
        return 0 # 문자열 없음 = 패배  
    
    # 가능한 액션 한가지를 취함 
    start, end = S[l], S[r-1]
    res = 0 

    if start != "?":
        for i in range(l,r):
            if start == S[i]:
                res = max(res, 1-dfs(i+1, r, qms))
            else:
                break 

    if end != "?":
        for i in range(r-1,l-1,-1):
            if end == S[i]:
                res = max(res, 1- dfs(l, i, qms))
            else:
                break 
        
    qms_l = [*divmod(qms, 3)][-nQm:]
    for i in range(nQm):
        # qms: 0~3**nQm-1 
        if qms_l[i] != 0:
            continue  

        idx = qmIndices[i]
        S = S[:idx] + "0" + S[idx+1:]
        res = max(res, 1-dfs(l,r, qms+i*3+1))
        
        S = S[:idx] + "1" + S[idx+1:]
        res = max(res, 1-dfs(l,r, qms+i*3+2))
        
        S = S[:idx] + "?" + S[idx+1:] # 초기화 

    dp[l][r][qms] = res 
    return dp[l][r][qms]

print(dfs(0,N,0))

