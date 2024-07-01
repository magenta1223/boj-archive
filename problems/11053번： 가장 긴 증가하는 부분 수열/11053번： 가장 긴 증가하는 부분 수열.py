#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11053                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11053                         #+#        #+#      #+#     #
#     Solved: 2023-12-19 18:28:02 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def length_of_lis(seq):
    if not seq:
        return 0
 
    # dp[i]는 seq[i]를 마지막으로 하는 가장 긴 증가하는 부분 수열의 길이
    dp = [1] * len(seq)
 
    for i in range(1, len(seq)):
        for j in range(i):
            # j번째 이후에 i번째 값을 더할 수 있는지? 
            if seq[i] > seq[j]:
                # 더할 수 있으면 -> 기존 최대길이와 j번째에 i번째 값을 더한 길이를 비교, 큰 값으로 변경 
                dp[i] = max(dp[i], dp[j] + 1)
 
    return max(dp)
 
N=int(input())
l=list(map(int, input().split()))
print(length_of_lis(l))