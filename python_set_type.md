# 파이썬 집합 자료형

## 1. 집합 자료형의 특징

 - 중복을 허용하지 않는다.
 - 정해진 순서가 없다. => 인덱싱으로 값을 얻을 수 없다.
 - set자료형에 저장된 값을 순서로 접근하고자 한다면, 리스트나 튜플로 변환해야 한다.

    <pre><code>
    # 집합 자료형 만들기
    >>>num_set = set([1,2,3])
    >>>num_set
    {1,2,3}
    
    # 중복 제거
    >>>alphabet_set = set('alphabet')
    >>>alphabet_set
    # 정해진 순서 없이 값이 들어가게 된다.
    {'a','e','l','h','p','b','t'}
    
    # 리스트로 변환 하기
    >>num_set = set([1,2,3])
    >>num_list = list(num_set)
    >>num_list
    [1,2,3]
    >>num_list[1]
    2
    
    # 튜플로 변환 하기
    >>num_set = set([1,2,3])
    >>num_tuple = tuple(num_set)
    >>num_tuple
    (1,2,3)
    >>num_tuple[2]
    3
    </code></pre>

## 2. 집합 자료형 활용하기

 - 교집합 구하기 : & 또는 intersection() 이용
 
 <pre><code>
 >>>s1 = set([1,2,3,4,5,6])
 >>>s2 = set([4,5,6,7,8,9])
 >>>s1 & s2
 {4,5,6}
 >>>s1.intersection(s2)
 {4,5,6}
 >>>s2.intersection(s1)
 {4,5,6}
 </code></pre>
 
 - 합집합 구하기 : | 또는 union() 이용
 - 중복된 값은 한 개씩만 표현된다.
 
 <pre><code>
 >>>s1 = set([1,2,3,4,5,6])
 >>>s2 = set([4,5,6,7,8,9])
 >>>s1 | s2
 {1,2,3,4,5,6,7,8,9}
 >>>s1.union(s2)
 {1,2,3,4,5,6,7,8,9}
 >>>s2.union(s1)
 {1,2,3,4,5,6,7,8,9}
 </code></pre>

- 차집합 구하기 : - 또는 difference() 이용
 
 <pre><code>
 >>>s1 = set([1,2,3,4,5,6])
 >>>s2 = set([4,5,6,7,8,9])
 >>>s1-s2
 {1,2,3}
 >>>s2-s1
 {8,9,7}
 >>>s1.difference(s2)
 {1, 2, 3}
 >>>s2.difference(s1)
 {8, 9, 7}
 </code></pre>

## 3. 집합 자료형 관련 함수

 - add : 값 1개를 추가한다.

 <pre><code>
 >>> s1 = set([1, 2, 3])
 >>> s1.add(4)
 >>> s1
 {1, 2, 3, 4}
 </code></pre>

 - update : 값 여러개를 추가한다.
 <pre><code>
 >>> s1 = set([1, 2, 3])
 >>> s1.update([4, 5, 6])
 >>> s1
 {1, 2, 3, 4, 5, 6}
 </code></pre>

 - remove : 특정값을 제거한다.    
 
 <pre><code>
 >>> s1 = set([1, 2, 3])
 >>> s1.remove(2)
 >>> s1
 {1, 3}
 </code></pre>