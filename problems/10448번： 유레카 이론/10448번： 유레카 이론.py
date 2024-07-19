#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 10448                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/10448                         #+#        #+#      #+#     #
#     Solved: 2024-07-19 02:48:37 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


input = open(0).readline 

# K가 3개의 삼각수의 합으로 표현 가능한지 확인 
# K는 1000이하 
# 1. 삼각수를 찾고
# 2. 2개로 표현 가능한 삼각수 

triNums = []
i = 1
while i*(i+1)//2 <= 1000:
    triNums.append(i*(i+1)//2) 
    i += 1 
dp = [[False] * 1001 for _ in range(3)]
for tri in triNums:
    dp[0][tri] = True 

for r in range(2):
    for i in range(1000, 0, -1):
        for tri in triNums:
            if dp[r][i] and i+tri <= 1000:
                dp[r+1][i+tri] = True 

for _ in range(int(input())):
    print(1 if dp[2][int(input())] else 0)


