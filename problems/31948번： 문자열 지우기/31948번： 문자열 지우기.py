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

S = input().strip()
dp = dict()

def dfs(s:str):
    if not s:
        # user가 패배 
        return 0 # user가 할게 없으므로 상대가 승리 

    if s in dp:
        return dp[s]
    
    n = len(s)
    # 가능한 액션 한가지를 취함 
    start, end = s[0], s[-1]
    res = 0 
    if start != "?":
        for i in range(n):
            if start == s[i]:
                res = max(res, 1-dfs(s[i+1:]))
            else:
                break 

    if end != "?":
        for i in range(n-1,-1,-1):
            if end == s[i]:
                res = max(res, 1- dfs(s[:i]))
            else:
                break 
    
    # 물음표 바꾸기 
    idx = s.find("?")
    if idx != -1:
        res = max(res, 1- dfs(s[:idx] + "0" + s[idx+1:]))
        res = max(res, 1- dfs(s[:idx] + "1" + s[idx+1:]))

    # idx = s.find("?", idx+1)
    # if idx != -1:
    #     res = max(res, 1- dfs(s[:idx] + "0" + s[idx+1:]))
    #     res = max(res, 1- dfs(s[:idx] + "1" + s[idx+1:]))

    dp[s] = res 
    return dp[s]
print(dfs(S))