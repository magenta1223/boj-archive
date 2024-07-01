#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1036                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1036                          #+#        #+#      #+#     #
#     Solved: 2024-05-27 11:19:49 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from string import ascii_uppercase
D = {str(i) : i for i in range(10)}
for i in range(len(ascii_uppercase)):
    D[ascii_uppercase[i]] = i+10 
rD = {v:k for k, v in D.items()}
 
N = int(input())
W = [input() for _ in range(N)]
K = int(input())
 
all_letters = set()
for w in W:
    all_letters.update(set(w))
 
def sum_36(words):
    # 길이 조정 
    maxlen = max([len(w) for w in words])
    words = [w.zfill(maxlen) for w in words]
    res, prev = "", 0
    # 뒷자리부터 더하기 
    for i in range(1, maxlen+1):
        s,r= divmod(sum([D[w[-i]] for w in words]) + prev, 36)        
        res = rD[r] + res 
        prev = s 
    # 남은거 
    while prev:
        s,r = divmod(prev, 36)
        res = rD[r]+res
        prev = s  
    return res 
 
def subtract(w1,w2):
    # w1 > w2 
    maxlen = max(len(w1), len(w2))
    w1, w2 = w1.zfill(maxlen), w2.zfill(maxlen)
    res, prev, w = 0,0,1
    for i in range(1, maxlen+1):
        # 빼기 
        s,r = divmod(D[w1[-i]] - D[w2[-i]] + prev, 36)
        res += w*r
        prev = s 
        w *= 36
    return res
 
S = sum_36(W)
diffs = []
for letter in all_letters:
    # 대체 
    z_replaced_W = [w.replace(letter, "Z") for w in W]
    s = sum_36(z_replaced_W)
    diffs.append((subtract(s,S), letter))
diffs.sort(key = lambda x: x[0], reverse= True)
 
replace_letter = []
for i in range(len(diffs[:K])):
    replace_letter.append(diffs[i][1])
 
for letter in replace_letter:
    W = [w.replace(letter, "Z") for w in W]
print(sum_36(W))