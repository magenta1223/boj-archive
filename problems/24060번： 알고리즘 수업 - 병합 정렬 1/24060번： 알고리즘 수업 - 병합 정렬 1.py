#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 24060                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/24060                         #+#        #+#      #+#     #
#     Solved: 2023-11-24 16:36:12 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def mergeSort(A,p,r):
    if p<r:
        q=int((p+r)/2)
        A=mergeSort(A,p,q)
        A=mergeSort(A,q+1,r)
        return merge(A,p,q,r)
    else:
        return A
    
def merge(A,p,q,r):
    global c, hist 
    tmp = []
    i=p
    j=q+1
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i+=1 
        else:
            tmp.append(A[j]) 
            j+=1 
    while i<=q:
        tmp.append(A[i])
        i+=1 
    while j<=r:
        tmp.append(A[j])
        j+=1
    
    for i in range(len(tmp)):
        c+=1
        A[p+i] = tmp[i]
        hist.append(tmp[i])
    return A 
 
def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        return merge(A, p, q, r)
    else:
        return A
c=0
hist=[]
N,K=map(int,input().split())
A=list(map(int,input().split()))
mergeSort(A, 0, len(A)-1)
print(hist[K-1] if len(hist) >= K else -1)