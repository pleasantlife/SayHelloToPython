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

## 1) 자료형 종류별 링크

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
 
 



