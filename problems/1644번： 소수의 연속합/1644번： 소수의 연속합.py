#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1644                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1644                          #+#        #+#      #+#     #
#     Solved: 2024-02-05 14:16:48 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 1644 : 소수의 연속 합
N=int(input().strip())
def prime(N):
    visited = [False for _ in range(N+1)]
    prime_numbers = set()
    for i in range(2, N+1):
        if not visited[i]:
            prime_numbers.add(i)
            for j in range(N//i+1):
                visited[i * j] = True
    return sorted(list(prime_numbers))
prime_numbers = prime(N)
a,b,s,ans = 0,0,0,0
while a < len(prime_numbers):
    if s < N:
        if b == len(prime_numbers):
            break
        else:
            s += prime_numbers[b]
            b += 1
    elif s > N:
        s -= prime_numbers[a]
        a += 1
    else:
        ans += 1
        if b == len(prime_numbers):
            break
        else:
            s += prime_numbers[b]
            b += 1
print(ans)