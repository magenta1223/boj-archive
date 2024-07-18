# 20913번： Mixtape Management - <img src="https://static.solved.ac/tier_small/11.svg" style="height:20px" />Gold V


| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 (추가 시간 없음) | 512 MB | 122 | 84 | 61 | 63.542% |


## 문제


Mary has created a mixtape with her favourite reggae tracks. The mixtape consists of a list of MP3 files on her computer that she wants to share with her friends Wendy and Larry. However she knows that her friends have different musical tastes and will therefore also have different preferences for the order in which the tracks are played.

Mary knows that Wendy is a Windows user and Larry is a Linux user and realised that she can use this to her advantage. This is because Windows and Linux use different methods to sort files within a directory in case their names contain numerical data. In Windows, numbers in file names are read as actual numbers, causing the files to be sorted by increasing values of these numbers. In Linux, there is no special handling for numbers, so file names are sorted lexicographically. See Figure M.1 for an example of file sorting on the two operating systems.

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 (추가 시간 없음) | 512 MB | 122 | 84 | 61 | 63.542% |
Figure M.1: Illustration of the first sample case. Note that the file extensions <code>.mp3</code>do not influence the ordering and are purely for illustration.
After deciding on the order in which she wants Wendy and Larry to listen to the tracks, Mary has already sorted the files according to Larry's taste. Now she wants to rename the files such that the filenames are distinct positive integers without leading zeroes, they are sorted in increasing lexicographic order, and when sorting them by value the new order will match Wendy's taste. For this purpose, she has come up with a permutation $p_1,\dots,p_n$ that describes how to rearrange Larry's list into Wendy's list: for every $i$, the $i$th number in lexicographic order needs to be the $p_i$th smallest by value. Help Mary find a suitable sequence of filenames.




## 입력


The input consists of:

- One line with an integer $n$ ($1\le n\le 100$), the number of tracks.

- One line with $n$ distinct integers $p_1,\dots,p_n$ ($1\le p_i\le n$ for each $i$), the given permutation.





## 출력


Output $n$ distinct integers in lexicographically increasing order, your sequence of filenames. All numbers must be positive integers less than $10^{1000}$ and may not contain leading zeroes. Any valid sequence of filenames will be accepted.




## 제한




## 예제 입력 1


<pre>7
4 2 6 1 5 7 3
</pre>


## 예제 출력 1


<pre>337 34 3401 7 780 7803 79
</pre>




## 예제 입력 2


<pre>4
4 1 3 2
</pre>


## 예제 출력 2


<pre>234 6 87 9
</pre>






## 출처




[ICPC](/category/1)> [Regionals](/category/7)> [Europe](/category/10)> [Northwestern European Regional Contest](/category/15)> [German Collegiate Programming Contest](/category/47)> [GCPC 2020](/category/detail/2427)M번
- 문제를 만든 사람: Paul Wild





