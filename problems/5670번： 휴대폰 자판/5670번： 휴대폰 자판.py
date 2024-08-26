#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 5670                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/5670                          #+#        #+#      #+#     #
#     Solved: 2024-08-26 01:12:41 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #



from collections import defaultdict 
from collections import deque 

input = open(0).readline 

def solution(n, words):
    trie = defaultdict(set)
    for word in words:
        subword = ""
        for char in word:
            nsubword = subword+char 
            trie[subword].add(nsubword)
            subword = nsubword  
        trie[word].add(None)

    for k in trie.keys():
        trie[k] = list(trie[k])
        
    q = deque([])

    while trie['']:
        w = trie[''].pop()
        q.append(('',w))

    while q:
        parent, subword = q.popleft()
        if len(trie[subword])==1:
            if trie[subword][0] is not None:
                subwordB = trie[subword].pop()
                del trie[subword]
                q.append((parent, subwordB))
            else:
                trie[parent].append(subword)
        else:
            trie[parent].append(subword)
            k = subword if subword in trie else parent 
            add = []
            while trie[subword]:
                subwordB = trie[subword].pop()
                if subwordB is not None:
                    q.append((k ,subwordB))
                else:
                    add.append((k,None))
            for k,v in add:
                trie[k].append(v)
    
    q = deque([('',0)])
    s = 0
    while q:
        subword, t = q.popleft()
        for nextsubword in trie[subword]:
            if nextsubword is None:
                s += t 
            else:
                q.append((nextsubword, t+1))
    return s/n

while True:
    N = input().strip()
    if not N:
        break 
    N = int(N)
    W = [input().strip() for _ in range(N)]
    print(f"{solution(N,W):.2f}")

