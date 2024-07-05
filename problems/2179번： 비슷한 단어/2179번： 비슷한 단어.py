#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2179                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2179                          #+#        #+#      #+#     #
#     Solved: 2024-07-03 12:57:27 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
W = [(input().strip(), i) for i in range(N)]
 
def find(a, b):
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            return i
    return min(len(a), len(b))
 
# 단어 리스트를 사전 순으로 정렬
WW = sorted(W, key=lambda x: x[0])
 
maxlen = 0
ans = (-1, -1)
lengths = [0] * N 
 
for i in range(N - 1):
    wordA, idxA = WW[i]
    wordB, idxB = WW[i + 1]
    res = find(wordA, wordB)
    if res > maxlen:
        maxlen = res 
    lengths[idxA] = max(lengths[idxA], res)
    lengths[idxB] = max(lengths[idxB], res)
 
 
findFirst = False
for i in range(N):
    # 최장 접두사를 찾으면 됨.
    if not findFirst:
        if lengths[i] == maxlen:
            firstWord = W[i][0]
            print(firstWord)
            findFirst = True 
    else:
        if lengths[i] == maxlen and W[i][0][:maxlen] ==firstWord[:maxlen]:
            print(W[i][0])
            break 