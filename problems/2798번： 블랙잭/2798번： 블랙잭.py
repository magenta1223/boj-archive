#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2798                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2798                          #+#        #+#      #+#     #
#     Solved: 2023-10-26 16:03:43 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
best_error = 100000 * N
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i!=j!=k!=i:
                blackjack=numbers[i] + numbers[j] + numbers[k]
                error = abs(M-blackjack)
                if error < best_error and blackjack <= M:
                    best_error = error
                    val = blackjack
print(val)