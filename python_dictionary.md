# 파이썬 딕셔너리 자료형

## 1. 파이썬에서 '딕셔너리'란?

 - 서로 대응대는 관계를 나타낼 수 있는 자료형
 - 사전의 '단어' : 단어에 대한 '정의' 의 관계와 유사
 - '딕셔너리'에서 '단어'는 Key, '정의'는 Value로 보면 된다.
 - 다른 언어에서는 연관 배열(Associative array) 또는 해시(Hash)라고 한다.

## 2. '딕셔너리'의 특징

 - 순차적으로 요소값을 구하는 것이 아니라 특정한 Key를 통해 Value를 얻는다.
 - 딕셔너리의 형태

    <pre><code>
    # 기본적인 형태 : {Key1:Value1, Key2:Value2, Key3,Value3}
    dictionary = {'name':'kim', 'age':'17', 'address':'Seoul'}
    
    # Value에는 리스트가 들어가기도 한다.
    dic_list = {'broadcast':['sbs', 'kbs', 'mbc']}
    </code></pre>

## 3. 딕셔너리 수정

 - 딕셔너리 쌍 추가

    <pre><code>
    dic = {'korea' : 'seoul'}
    dic['taiwan'] = 'taipei'
    dic['usa'] = ['washington', 'newyork', 'LA']
    결과 : dic = {'korea' : 'seoul', 'taiwan':'taipei', 'usa' : ['washington', 'newyork', 'LA']}
    </code></pre>

 -  딕셔너리 삭제      
    <pre><code>
    del dic['taiwan']
    결과 : dic={'korea':'seoul', 'usa':['washington', 'newyork', 'LA']}

## 4. '딕셔너리' 사용법

 - Value 얻기 

    <pre><code>
    # 딕셔너리명[키] 형태로 얻기
    age = {'kim' : 30, 'lee' : 17}
    Value 얻기 : age[kim]
    결과 : 30
    age[lee]
    결과 : 30



