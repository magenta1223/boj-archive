#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 3111                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/3111                          #+#        #+#      #+#     #
#     Solved: 2024-09-04 07:38:34 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #



input = open(0).readline 
A, T = input().strip(), input().strip()
M,N = len(A), len(T)
RA = list(A[::-1])
A  = list(A)
s, e = 0, N-1
fwd_q, bwd_q = [], []
while s<=e:
    while s<=e: 
        fwd_q.append(T[s])
        s += 1 
        if fwd_q[-M:] == A:
            del fwd_q[-M:]
            break 
    while s<=e:
        bwd_q.append(T[e])
        e -= 1 
        if bwd_q[-M:] == RA:
            del bwd_q[-M:]
            break
# 붙어서 생기는걸 확인 
while bwd_q:
    if fwd_q[-M:] == A:
        del fwd_q[-M:]
    fwd_q.append(bwd_q.pop())
while fwd_q[-M:] == A:
    del fwd_q[-M:]

print("".join(fwd_q))





"""
ababa
abaababababababaaba

ababa
abaababababababaaba
ababababa


baba


dsnrpakbgwjyeajuqpwckqttywvkjylwpkphzwbkftficxrhhvisgcvypopmbkmcjtvjwsacababcababaacababaababaaacababaabababacabaabaabacabbahzlphszwvgkuyetxrrxwcghngzhagjhvcpfhnbhmpqskyrxveuriwxvgipenymvphdkbvg
dsnrpakbgwjyeajuqpwckqttywvkjylwpkphzwbkftficxrhhvisgcvypopmbkmcjtvjwsacababcababaacababaababaaacababaabababacabaabaabacabbahzlphszwvgkuyetxrrxwcghngzhagjhvcpfhnbhmpqskyrxveuriwxvgipenymvphdkbvg

"""