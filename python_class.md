# 클래스 (Class)

## 1. 클래스를 사용하는 이유
 - 많은 프로그래밍 언어들이 '클래스'라는 개념을 통해, 객체지향을 구현하고 있다.
 - 한 프로그래밍에서 같은 일을 하지만, 결과가 다른 여러개의 존재가 필요하다면? 함수를 여러번 만들어야 할까?
 - '클래스' 하나를 만들어 그 안에 할일을 지정하고, '객체'를 생산하면 같은 일을 하되 결과를 다르게 만들 수 있다.
 - 파이썬에서도 '클래스'가 존재하여, 객체를 만들어낼 수 있다.

## 2. 파이썬 클래스 만들고 사용하기

 - 'class <클래스명>:'의 형태로 만든다.
 - 클래스명은 보통 영문 대문자로 시작하며, 클래스 안의 내용은 들여쓰기로 구분한다.
 - 아무 명령이 없는 클래스를 미리 만들어둔다면, 선언문 아래에 'pass'를 쓰자.
 - 클래스 안에는 클래스나 함수, 변수가 들어갈 수 있다.
 <pre><code>
 #클래스 만들기

 >>> class Account:
 ...    counts = 0
 ...    
 ...    def __init__(self, name):
 ...        self.name = name
 ...        Account.counts += 1
 ...
 >>>

 #클래스 사용하기

 >>> sam = Account("sam")
 >>> sam.name
 'sam'
 >>> sam.counts
 1
 >>> mac = Account("mac")
 >>> mac.name
 'mac'
 >>> mac.counts
 2
 >>> kei = Account("kei")
 >>> kei.name
 'kei'
 >>> kei.counts
 3

 </code></pre>
