#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1943                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1943                          #+#        #+#      #+#     #
#     Solved: 2024-06-10 12:59:41 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

ans = []
 
for _ in range(3):
    N = int(input())
    COINS = dict()
    S = 0
    for _ in range(N):
        a, b = list(map(int, input().split()))
        COINS[a] = b
        S += a * b
 
    # 총합이 홀수라면 두 그룹으로 나눌 수 없음
    if S % 2:
        ans.append(0)
        continue
 
    target = S // 2
    dp = [0] * (target + 1)
    dp[0] = 1  # 0원을 만드는 방법은 한 가지 (아무것도 선택하지 않는 경우)
 
    for coin, count in COINS.items():
        if count * coin >= target:
            # 이 동전만으로도 목표를 초과할 수 있다면
            for j in range(coin, target + 1):
                if dp[j - coin]:
                    dp[j] = 1
        else:
            # 해당 동전으로 목표를 초과할 수 없을 때
            for j in range(target, -1, -1):
                if dp[j]:
                    for k in range(1, count + 1):
                        if j + k * coin <= target:
                            dp[j + k * coin] = 1
 
    ans.append(dp[target])
 
# 결과 출력
print(*ans, sep='\n')