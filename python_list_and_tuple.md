# 파이썬 문자열 자료형

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
    
    // 연속된 범위의 값 수정
    a = ['a', 'b', 'c', 'd', 'e']
    a[1:2] == 'b'
    a[1:2] = ['f', 'g', 'h']
    
    //이렇게 하면 리스트를 추가했다고 해도, 리스트가 하나의 요소값으로 들어가는 것이 아니다.
    결과 : a == ['a', 'f', 'g', 'h', 'c', 'd', 'e']
    
    //요소값으로 리스트 추가하기
    a[1] = ['a', 'b', 'c']
    결과 : a == ['a' , ['a', 'b', 'c'], 'c'
    
    // 리스트 내의 요소 지우기
    a = ['a', 'b', 'c', 'd', 'e']
    a[1:3] = []
    결과 : a == ['a', 'd', 'e']
    
    a = ['apple', 'melon', 'peach']
    del a[2]
    결과 : a == ['apple', 'melon']
    
    // del은 파이썬이 자체적으로 가지고 있는 삭제 함수이다.
    </code></pre>

- 리스트 관련 함수들

    1. append
     
        - 리스트의 맨 마지막에 요소값 추가
        - 어떤 자료형도 추가할 수 있다.

    <pre><code>
    a = ['car', 'train', 'ship']
    a.append('airplane')
    결과 : a == ['car', 'train', 'ship', 'airplane']
    </code></pre>

    2. sort

        - 리스트의 요소를 순서대로 정렬해준다.
    <pre><code>
        a = [6, 3, 4, 5]
        a.sort() // 오름차순 정렬
        결과 : a == [3, 4, 5, 6]
        
        a.sort(reverse=True) // 내림차순 정렬
        결과 : a == [6, 5, 4, 3]
    </code></pre>

    3. index

        - 리스트에 있는 요소값의 위치를 반환한다.
     
    <pre><code>
        a = ['python', 'java', 'c', 'javascript']
        a.index(3) == 'c' //index는 1부터 시작.    
    </code></pre>

    4. insert와 remove

        - insert : 리스트안에 원하는 위치에 특정 요소값을 넣는다.
        - remove : 리스트에서 첫 번쨰로 나오는 지정 요소값을 삭제한다.

    <pre><code>
        //insert
        a = [1, 2, 3, 1, 2, 3]
        a.insert(3, 99)
        결과 : a == [1, 2, 3, 99, 2, 3]
        
        //remove
        a = [1, 2, 3, 99, 2, 3, 'string']
        a.remove(3)
        결과 : a == [1, 2, 99, 2, 3, 'string']

        //a.remove(5)는 에러가 난다.
        //요소가 아닌 인덱스값을 넣었기 때문.
    </code></pre>

    5. pop

        - 리스트의 맨 마지막 요소값을 꺼낸다.(리스트에서 삭제함.)
        - 요소값으로 삭제할 수 없으며, 인덱스로만 삭제 가능하다.

    <pre><code>
        a = ['korea', 'usa', 'japan']
        a.pop(2)
        결과 : 'japan'
        a == ['korea', 'usa']
        
        //a.pop('usa')는 에러가 난다.
    </code></pre>

    6. count

        - 리스트에 포함된 지정 요소값 개수를 출력한다.

    <pre><code>
        
        a = [1, 9, 2, 4, 9, 6, 9, 8, 9, 2]
        a.count(9)
        결과 : 4

    </code></pre>

    7. extend
        - 원래의 리스트에 다른 리스트를 추가한다.

    <pre><code>
    
        a = [19, 22, 25]
        a.extend[6, 12, 18]
        결과 : a == [19, 22, 25, 6, 12, 18]
        
        //extend와 동일한 결과를 나타내는 수식
        a = [19, 22, 25]
        a += [6, 12, 18]
        결과 : a == [19, 22, 25, 6, 12, 18]

    </code></pre>

# 파이썬 투플(tuple) 자료형

## 1) 튜플의 특징

    1. 리스트와 유사하다.
    2. ()로 둘러싼다.
    3. 값을 바꿀 수 없다.

<pre><code>
    //튜플의 형태

    number = (1,2,3)
    comma = (3,)
    duplex = (1, 2, (35, 36))
    special = 99, 98, 100