# 16287번： Parcel - <img src="https://static.solved.ac/tier_small/16.svg" style="height:20px" />Platinum V


| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 512 MB | 7064 | 1513 | 1087 | 21.854% |


## 문제


국제대학소포센터(ICPC: International Collegiate Parcel Center)는 전세계 대학생들을 대상으로 소포 무료 배송 이벤트를 진행하고 있다. 무료 배송 조건은 보낼 소포가 물품 4개로 구성되어야 하며 이들 물품의 무게 합이 정확히 정해진 정수 무게 그램이어야 한다는 것이다.
부산대학교에 있는 찬수는 영국 왕립대학에 있는 수환에게 보낼 물품이 매우 많이 있는데, 각 물품의 무게(모두 정수 그램)는 모두 다르다. 이 이벤트는 한시적으로 진행되는 이벤트이기 때문에 찬수는 자신이 보낼 물품 중에서 이 조건을 만족하는 물품 4개가 있는지 가능하면 빨리 알아내고 싶다. 다시 말해서 서로 다른 (≥ 4)개의 정수로 이루어진 집합 에서 4개의 원소만 꺼내어 만든 부분집합 (|| = 4)가 ∑∈
= 조건을 만족하는지 판단하려고 한다. 
주어진 와 에 대해서, 위 조건을 만족하는 부분집합 가 존재하면 YES를, 아니면 NO를 출력하는 프로그램을 작성하시오.



## 입력


입력은 표준입력을 사용한다. 입력의 첫 줄에는 무게 (10 ≤ ≤ 799,994)와 의 원소 개수 (4 ≤ ≤ 5,000)이 공백으로 분리되어 주어진다. 다음 줄에는 의 원소인 개의 정수 
∈ (1 ≤ ≤ )가 공백으로 분리되어 주어진다. 각 원소 
는 1이상 200,000이하이다(1 ≤ 
≤ 200,000).



## 출력


출력은 표준출력을 사용한다. 문제의 조건에 따라 <code>YES</code>나 <code>NO</code>를 한 줄에 출력한다.



## 제한




## 예제 입력 1


<pre>10 6
5 10 7 3 2 1
</pre>


## 예제 출력 1


<pre>NO
</pre>




## 예제 입력 2


<pre>21 7
10 1 4 6 2 8 5
</pre>


## 예제 출력 2


<pre>YES
</pre>






## 출처


[ICPC](/category/1)> [Regionals](/category/7)> [Asia Pacific](/category/42)> [Korea](/category/211)> [Nationwide Internet Competition](/category/256)> [Seoul Nationalwide Internet Competition 2018](/category/detail/1935)F번
- 데이터를 추가한 사람: [kipa00](/user/kipa00), [urd05](/user/urd05), [yukariko](/user/yukariko), [zych1751](/user/zych1751)
- 잘못된 데이터를 찾은 사람: [orihehe](/user/orihehe)




