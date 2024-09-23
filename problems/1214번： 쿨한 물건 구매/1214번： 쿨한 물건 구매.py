#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1214                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1214                          #+#        #+#      #+#     #
#     Solved: 2024-09-23 06:20:57 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# D원을 내기위해 P원, Q원 지폐로만 지불
# 최소로 내야하는 금액은? 
# 17, 7, 13 
# 이 경우 20원이 최소 


# 시작은 D, 끝은 10**9 
# D원 이상, X원 이하로 만드는게 가능한지 확인
# P,Q 중 작은 액수로 D원 이상이 되게 만든다.
# 루프
    # 이게 X보다 작은가? -> break 
    # 현재 금액에 P,Q 중 큰 액수를 더하고, D원 미만이 되기 전까지 작은 액수를 빼준다. 
# 이러면 X원 이하가 가능한지 확인하려면 너무 오래걸림. 
# 최대 10억번 안에 끝남 

D,P,Q = map(int, input().split())
A,B = sorted([P,Q])


if D%A:
    X = (D//A + 1)*A
    # 1. 이 이하로 만드는게 가능? 
    cntA, cntB = D//A+1, 0 
else:
    X = D 
    cntA, cntB = D//A, 0

ans = X 
ansCnt = cntA, cntB

while cntA>=0:
    X += B 
    diffA = (X-D)//A
    cntA -= diffA
    cntB += 1 
    X -= diffA * A 

    if cntA < 0:
        break 
    if X<ans:
        ans = X
        ansCnt = cntA, cntB

print(ans)
print(ansCnt)
print(A*ansCnt[0] + B*ansCnt[1])


"""
1000000000 3 7 
"""