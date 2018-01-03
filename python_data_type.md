## 1) 문자열

 - """ : 쌍따옴표 세개 안에 들어간 문자는 줄바꿈까지 반영되어 변수에 대입된다.
    <pre><code>
        multiline = """
        라팔아
        팔렸니
        아니오
        """
        
        print(multiline)
        
        라팔아
        팔렸니
        아니오 

    </code></pre>

- 문자열도 연산이 가능하다.
    <pre><code>
        bye = 'python'
        print(bye * 2)
        
        결과 : pythonpython
    </code></pre>

- 문자열 인덱싱과 슬라이싱
    <pre><code>
    index = '21세기는 정보화시대로서 코딩이 중요하게 여겨집니다.'
    
    index[0] == 2
    index[1] == 1
    index[-1] == .
    index[-2] == 다
    
    index[:10] == 21세기는 정보화시
    (세미콜론이 숫자 앞에 오면 해당글자까지만 잘라서 보여준다.) 
    
    index[7:] == 보화시대로서 코딩이 중요하게 여겨집니다.
    (세미콜론이 숫자 뒤에 오면 해당글자 다음부터 잘라서 보여준다.)
    </code></pre>

## 2) 리스트

- 리스트는 자바의 배열과 같음.
    <pre><code>
    number_list = [1, 3, 5, 7, 9]
    complex_list = [1, 'python', 'aaa', 'bbb']
    nested_list = [1, 3, 5, ['aa', 'bb', 'cc']]
    </code></pre>

- 인덱싱 방법도 자바와 유사함.
    <pre><code>
    number_list[0] == 1
    complex_list[2] == 'aaa'
    
    number_list[0] + number_list[3]
    결과 : 8
    </code></pre>

- 다중 리스트도 가능함.

    <pre><code>
    nested_list[3] == ['aa', 'bb', 'cc']
    nested_list[3][1] == 'bb'
    </code></pre>

- 리스트도 변수처럼 슬라이싱과 연산이 가능함.

    <pre><code>
    // 슬라이싱
    
    b = complex_list[:2]
    b == [1, 'python']
    
    // 연산
    odd = [1, 3, 5]
    even = [2, 4, 6]
    
    // 연산 더하기
    odd + even == [1, 3, 5, 2, 4, 6]

    // 리스트 반복
    odd * 3 == [1, 3, 5, 1, 3, 5, 1, 3, 5]
    </code></pre>

- 주의해야할 리스트 연산 오류

    <pre><code>
    a = [1, 2, 3]
    print(a[2] + Three)
    결과 : 3Three   ??
    </code></pre>

    > ai[2]의 값은 3이라는 정수이고, "Three"는 문자열이므로 서로 더할 수 없기 때문에 형 오류(TypeError)가 발생한다.

    > 만약, 3Three라는 결과를 얻고 싶다면 아래와 같이 str() 내장 함수를 이용해야한다.

    <pre><code>
    str(a[2] + "Three")
    </code></pre>

- 리스트 수정하기

    <pre><code>
    a = ['a', 'b', 'c', 'd', 'e']
    /* 리스트 내에 바꾸고자 하는 위치를 불러온 후,
    */   변경할 변수를 입력하면 된다.   
    a[3] = 'f'
    a == ['a', 'b', 'c', 'f', 'e']
    </code></pre>