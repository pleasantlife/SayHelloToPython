Say Hello to Python
===================

# 1. 파이썬은?

 - 1990년 암스테르담의 귀도 반 로섬이 개발
 - '몬티 파이썬의 날아다니는 서커스'에서 따왔다고 함.
 - 인터프리터 언어(한 줄씩 소스 코드를 해석해서 그때그때 실행해 결과를 바로 확인할 수 있는 언어)


# 2. 파이썬의 장점

 - 직관적이다.
 - 문법이 쉬워 빠르게 배울 수 있다.
 - 다른언어(이를 테면 C)로 만든 프로그램을 포함시킬 수 있다.
 - 간결한 코드를 작성하게 해준다.

# 3. 파이썬의 특징

 - 변수에 타입을 지정할 필요가 없다.
 - 세미콜론(;)대신 엔터를 쓰고, 중괄호 대신 들여쓰기로 단계를 구분한다.

# 4. 파이썬 변수

 - 변수는 특별히 타입을 입력하지 않는다.
    <pre><code>
    a = 16 (정수형)
    b = 2.57 (실수형)
    c = "파이썬" (String)
    d = 0o177 (8진수 : 숫자 0 + 알파벳 소문자 o 또는 대문자 O로 시작.)
    e = 0xABC (16진수 : 숫자 0 + 알파벳 소문자 x로 시작.)
    </code></pre>

 - 연산 또한 다른언어들과 특별히 다르지 않다.
    <pre><code>
    a = 2
    b = 4
    
    a * b
    결과 : 8
    
    a ** b
    결과 : 16 (2의 4제곱)

    7 / 4
    결과 : 1.75
    
    7 // 4
    결과 : 1 (소수점은 버림)

    </code></pre>

# 5. 파이썬 자료형 

## 1) 자료형 종류별 정리

[리스트 자료형과 튜플 자료형](https://github.com/pleasantlife/SayHelloToPython/blob/master/python_list_and_tuple.md)

[딕셔너리 자료형](https://github.com/pleasantlife/SayHelloToPython/blob/master/python_dictionary.md)

[집합 자료형](https://github.com/pleasantlife/SayHelloToPython/blob/master/python_set_type.md)    

## 2) 자료형의 Boolean

 - Boolean은 'True(참)' 또는 'False(거짓)'으로 판단할 수 있는 유형을 뜻한다.

 - 파이썬에는 자료형에서도 'True(참)'와 'False(거짓)'을 구분할 수 있다.
 - '속이 차있으면 True', '속이 비어있으면 False' 이라고 생각해두면 구분하기 쉬워진다.

  <pre>
  # 값 별 True / False 판별하기
  "python" : True
  ""       : False
  [1,2,3]  : True
  []       : False
  ()       : False
  {}       : False
  1        : True
  0        : False
  None     : False
  </pre>

 - 코드 예시

 <pre>
 # True와 False의 활용
 
 >>> a = [1,2,3,4]
 >>> while a:
 ...    a.pop()
 ...
 4
 3
 2
 1
 
 # 설명 : while문을 분기시 a 내부에 요소가 있으면 True가 되기 때문에, pop()이 실행된 후 다시 while문으로 돌아간다. 이 과정을 a 내부에 요소가 없을때까지 반복하게 되고, 요소가 없을 때 while문을 빠져나온다.  

 </pre>

 ## 3) 변수에 대하여

  - 파이썬의 변수는 값을 저장하기도 하지만, 객체를 가리키는 것이기도 하다.
  - 객체를 가리키는 목적으로 사용된 변수는 객체 그 자체를 저장하는 것이 아니라, 객체가 저장된 메모리의 위치를 담고 있는 레퍼런스가 된다.
  - 같은 객체를 여러 개의 변수가 가리킬 수 있으며, 한 개의 객체를 몇 개의 변수가 가리키고 있는지를 나타낸 것이 '레퍼런스 카운트'이다.

  <pre><code>
  # 서로 같은 객체를 가리키는지 확인
  >>> a = 3
  >>> b - 3
  >>> a is b
  True

  # 레퍼런스 카운트 확인
  >>> import sys
  >>> sys.getrefcount(3)
  33
  # - 파이썬에서 내부적으로 이미 3이라는 객체를 사용했기 때문에, 33이 나오게 된다.
  (이보다 더 나올수도, 덜 나올 수도 있다.)

  </code></pre>

 - 변수 생성하기

  <pre><code>
  # 튜플로 변수 생성하기
  >>> a, b = ('hello', 'world')
  >>> (a, b) = 'hello', 'world'

  # 리스트로 변수 생성하기
  >>> [a, b] = ['hello', 'world']
  
  # 여러개의 변수에 같은 값 대입하기

  >>> a = b = 'Hello World!'
  </code></pre>

- 메모리에 생성된 변수 없애기
 
  - 메모리에 생성된 변수를 굳이 삭제해야 하나?
    -  객체를 가리키는 변수가 하나라도 있으면, 그 객체는 사라지지 않는다.
    -  그럴 경우, 객체가 메모리에 계속 남아있어 성능저하나 메모리부족을 야기할 수 있다.
    -  따라서, 쓰지않는 객체를 사라지게 해야하고 이를 위해 변수를 삭제해야한다.

  <pre><code>
  # 변수 없애기
  >>> a = 3
  >>> b = 3
  >>> del(a)
  </code></pre>

- 변수로 리스트 복사하기

  - [:] 이용 : 리스트 전체를 가리키는 [:]을 이용하여 복사한다.

  <pre><code>
  >>> a = ['spring', 'summer', 'fall', 'winter']
  >>> b = a[:]
  >>> a[0] = 'bom'
  >>> a
  ['bom', 'summer', 'fall', 'winter']
  >>> b
  ['spring', 'summer', 'fall', 'winter']
  </code></pre>

  - copy 모듈 이용

  <pre><code>
  >>> from copy import copy
  >>> b = copy(a)
  </code></pre>

  - 유의사항 : 두 변수는 같은 값을 가지고 있지만, 서로 동일한 객체는 아니다.

  <pre><code>
  >>> b is a
  False
  </code></pre> 

# 6. 함수 (Definition)

  - [함수 부분 정리](https://github.com/pleasantlife/SayHelloToPython/blob/master/python_definition.md)

 



