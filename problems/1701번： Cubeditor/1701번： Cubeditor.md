# 1701번： Cubeditor - <img src="https://static.solved.ac/tier_small/13.svg" style="height:20px" />Gold III


| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 0.5 초 | 128 MB | 10344 | 3432 | 2622 | 34.564% |


## 문제


Cubelover는 프로그래밍 언어 Whitespace의 코딩을 도와주는 언어인 Cubelang을 만들었다. Cubelang을 이용해 코딩을 하다보니, 점점 이 언어에 맞는 새로운 에디터가 필요하게 되었다. 오랜 시간 고생한 끝에 새로운 에디터를 만들게 되었고, 그 에디터의 이름은 Cubeditor이다.

텍스트 에디터는 찾기 기능을 지원한다. 대부분의 에디터는 찾으려고 하는 문자열이 단 한 번만 나와도 찾는다. Cubelover는 이 기능은 Cubelang에 부적합하다고 생각했다. Cubelang에서 필요한 기능은 어떤 문자열 내에서 부분 문자열이 두 번 이상 나오는 문자열을 찾는 기능이다. 이때, 두 부분 문자열은 겹쳐도 된다.

예를 들어, abcdabc에서 abc는 두 번 나오기 때문에 검색이 가능하지만, abcd는 한 번 나오기 때문에 검색이 되지를 않는다.

이렇게 어떤 문자열에서 두 번 이상 나오는 부분 문자열은 매우 많을 수도 있다. 이러한 부분 문자열 중에서 가장 길이가 긴 것을 구하는 프로그램을 작성하시오.

예를 들어, abcabcabc에서 abc는 세 번 나오기 때문에 검색할 수 있다. 또, abcabc도 두 번 나오기 때문에 검색할 수 있다. 하지만, abcabca는 한 번 나오기 때문에 검색할 수 없다. 따라서, 두 번 이상 나오는 부분 문자열 중에서 가장 긴 것은 abcabc이기 때문에, 이 문자열이 답이 된다.




## 입력


첫째 줄에 문자열이 주어진다. 문자열의 길이는 최대 5,000이고, 문자열은 모두 소문자로만 이루어져 있다.




## 출력


입력에서 주어진 문자열의 두 번이상 나오는 부분문자열 중에서 가장 긴 길이를 출력한다.




## 제한




## 예제 입력 1


<pre>abcdabcabb
</pre>


## 예제 출력 1


<pre>3
</pre>




## 예제 입력 2


<pre>abcdefghijklmn
</pre>


## 예제 출력 2


<pre>0
</pre>




## 예제 입력 3


<pre>abcabcabc
</pre>


## 예제 출력 3


<pre>6
</pre>






## 출처


[ICPC](/category/1)> [Regionals](/category/7)> [Asia Pacific](/category/42)> [Korea](/category/211)> [Asia Regional - Seoul 2007](/category/detail/1065)B번
- 잘못된 데이터를 찾은 사람: [atomzeno](/user/atomzeno)
- 문제를 번역한 사람: [baekjoon](/user/baekjoon)
- 문제의 오타를 찾은 사람: [dsa2341](/user/dsa2341), [klimmek55](/user/klimmek55)




