# 함수 (Definition)

 ## 1) 파이썬 함수의 구조

 - def 함수명(입력받는 인수):  형식으로 사용하며, 자바처럼 {}로 감싸지 않고, 들여쓰기로 함수 영역을 구분한다.
 - 함수를 def로 선언, 함수명은 임의로 만들며, 입력받는 인수는 함수에 입력할 값이다. 
 - 함수명은 보통 소문자로 시작한다.(대문자로 시작하는 클래스와 구분)

 ```python
 # 함수의 형태 예시
 def hamsu(a, b, c):
  return a + b + c
  
 # 해석
 1) 'hamsu'라는 이름의 함수를 만든다.
 2) 함수 내에 a, b, c라는 값이 입력(=사용)된다.
 3) 함수의 실행 결과로 a+b+c의 값을 받는다.   
 ```

## 2) 여러가지 함수의 형태

- 일반적인 함수 : 입력값과 결과값 모두 있는 함수
  ```python
  # 함수 생성
  >>>def normal(a,b):
  ...   return a + b
  
  # 함수 사용
  >>>normal(17, 20):
  37
  ```

- 입력값이 없는 함수 : 입력값을 받는 부분에 값을 넣지 않은 함수
  ```python
  # 입력값이 없는 함수 생성
  >>>def hello():
  ...  return 'Hello World!'
  
  # 입력값이 없는 함수 사용
  >>>a = hello()
  >>>print(a)
  Hello World!
  ```

- 결과값이 없는 함수 : return 문이 없는 함수
  ```python
  # 결과값이 없는 함수 생성
  >>>def hello(a, b):
  ... print("%d, %d의 합은 %d입니다." % (a, b, a+b))
  
  # 결과값이 없는 함수 사용
  >>>a = hello(16, 17)
  >>>print(a)
  16, 17의 합은 33입니다.
  ```
- 입력값과 결과값 모두 없는 함수 : 입력값을 받는 부분에 넣어준 파라미터도 없고, return 구문도 없는 함수
- 입력값과 결과값이 모두 없는 함수는 변수에 입력할 수 없다.(변수에 값을 넣어야 하는데, 값을 가질 수 없기 때문이다.)
- 따라서, 함수만 실행시켜서 사용한다. (물론, 다른 함수들도 꼭 변수에 넣어야만 사용할 수 있는건 아니다.)
  ```python
  # 입력값과 결과값 없는 함수 생성
  >>>def noresult():
  ... print('No Result')
  
  # 입력값과 결과값 없는 함수 사용
  >>> noresult()
  No Result
  ```

## 3) 여러 개의 입력값을 받는 함수

   - 입력 변수명 앞에 *을 붙이면, 입력한 값들을 전부 모아서 튜플 형태로 만들어준다.
   ```python
   # 입력값의 갯수에 제한이 없는 함수 만들기
   # 'args'에는 원하는 변수명을 넣으면 된다.(정해진 타입을 넣어야 하는 자바와는 다르다!)
   >>>def plus_all(*args):
   ...  result = 0
   ...  for i in args:
   ...      result = result + i
   ...  return result

   # 실제 사용
   >>> value = plus_all(1,2,3,4,5)
   >>> print(value)
   15
   >>> value = plus_all(1,2,3,4,5,6,7,8,9,10)
   >>> print(value)
   55
   ```

## 4) args와 kwargs에 대한 추가 설명

  - 앞에서 살펴본 args뿐만 아니라 kwargs도 함께 쓰는 경우가 많다.
  - args앞에는 * 한 개를 붙여 사용하며, tuple이나 list 형태의 자료를 unpacking(괄호나 대괄호를 제거)하여 반환한다.
  - kwargs앞에는 * 두 개를 붙여 사용하며, dictionary 형태의 자료를 unpacking해주어 value 값을 반환해준다. 

   ```python
   #kwargs 예시 추가
   >>>profile_dict_many = {
        "name" : "홍길동",
        "age" : 25,
        "height": 175,
        "country": "대한민국"
      }
   >>>def myprofile_kwargs(**kwargs):
   ...  for key, value in kwargs.items():
   ...  print("{key} = {value}.format(key=key, value=value))
   myprofile_kwargs(**profile_dict_many) 
   ```

## 5) 함수의 결과값은 언제나 하나이다.

  - 함수에서 return문에 여러 개의 값을 쓰더라도, 결과값은 튜플값으로 묶어서 반환한다.
  ```python
  #return문 하나에 여러 개의 값을 쓴 함수
  >>>def sum_and_mul(a,b):
  ... return a+b, a*b
  >>>result = sum_and_mul(7, 12)
  >>>print(result)
  (19, 84)
  ```

  - 임의의 상황이 되었을 때, 함수를 빠져 나가고자 하면 return 함수를 단독으로 사용한다.
  ```python
  #return문으로 함수 종료.
  >>>def terminate_zero(value):
  ... if value == 0:
  ...   return
  ... print(value)
  ```

## 6) 함수 안에서 함수 밖의 변수를 변경하는 방법

 - return 함수를 이용하거나, global 명령어를 이용한다.
 - 단, global은 의존성을 갖기 떄문에 가급적 사용하지 않도록 한다.
  ```python
  #return 이용하기
  >>>value = 1
  >>>def valuedef(value):
  ...   value = value + 1
  ...   return value
  ...
  >>>value = valuedef + 1
  2

  #global 명령어 이용하기
  >>>value = 1
  >>>def valuedef():
  ...   global value
  ...   value = value + 1
  ...
  >>>valuedef()
  >>>print(value)
  2
  ```

# 7) 함수 사용시 주의 사항

 - 함수에서 초기값을 설정해 놓은 인수 뒤에 있는 인수는 사용할 수 없다.
 ```python
 #초기값 설정
 def profile(name, age, man=True):
    print("이름 : %s" % name )
    print("나이 : %d" % age )
    if man:
      print("성별 : 남자")
    else:
      print("성별 : 여자")
 #초기값 인수 위치 변경
 def profileswitch(name, man=True, age):
    print("이름 : %s" % name )
    print("나이 : %d" % age )
    if man:
      print("성별 : 남자")
    else:
      print("성별 : 여자")

  #profileswitch 함수 실행시 SyntaxError 발생
  ```
