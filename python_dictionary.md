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
    </code></pre>

## 4. '딕셔너리' 사용법

 - Value 얻기 

    <pre><code>
    age = {'kim' : 30, 'lee' : 17}
    Value 얻기 : age[kim]
    결과 : 30
    age[lee]
    결과 : 17
    </code></pre>

## 5. 주의사항

 - Key값이 중복되면 하나를 제외한 나머지는 무시된다.(무시되지 않는 것과 무시되는 것이 어떤 것인지 알 수 없다.)
 - Value에는 리스트가 들어갈 수 있지만, Key에는 리스트가 들어갈 수 없다. (리스트는 그 값이 변할 수 있기 때문이다.)

## 6. 딕셔너리 관련 함수

 - Key 리스트 만들기 (keys)
 - keys()는 딕셔너리의 Key만을 모아서 dict_keys라는 객체를 리턴한다.

    <pre><code>
    capital = {'korea':'seoul', 'usa':'washington', 'japan':'tokyo', 'russia':'moscow'}
    capital.keys()
    dict_keys(['korea', 'usa', 'japan'])
    
    # dict_keys 객체는 리스트와 형태의 차이가 없으나 append, insert, pop, remove, sort 함수 등 리스트 고유의 함수를 사용할 수는 없다.
    
    # 리스트 형태로 변환하려면 list()를 이용한다.

    list(captital.keys())
     </code></pre>

- Value 리스트 만들기 (values)

    <pre><code>
    capital = {'korea':'seoul', 'usa':'washington', 'japan':'tokyo', 'russia':'moscow'}
    dict_values(['seoul','washington','tokyo','moscow'])
    
    # dict_values는 dict_key와 성격이 같다.
    </code></pre>

 - Key, Value 쌍 얻기 (items)   
    - 튜플로 묶은 값을 얻을 수 있다.

    <pre><code>
    capital = {'korea':'seoul', 'usa':'washington', 'japan':'tokyo', 'russia':'moscow'}
    captial.items()
    dict_items([('korea', 'seoul'), ('usa', 'washington'), ('japan', 'tokyo'), ('russia','moscow')])
    </code></pre>
- 딕셔너리 내의 Key:Value 쌍 모두 지우기 (clear)

    <pre><code>
    capital = {'korea':'seoul', 'usa':'washington', 'japan':'tokyo', 'russia':'moscow'}
    capital.clear()
    capital = {}
    
    # 빈 딕셔너리는 {}로 표현한다.
    </code></pre>

 - Key로 Value 얻기 (get)

    <pre><code>
    capital = {'korea':'seoul', 'usa':'washington', 'japan':'tokyo', 'russia':'moscow'}
    capital.get('korea')
    
    #결과
    'seoul'

    #존재하지 않는 Key를 가져오려고 할 때
    
    #Key 오류를 발생시킨다.
    captital.get('canada')

    #None을 리턴한다.
    capital['canada']

    default를 리턴한다.
    
    captial.get('canada', 'idonnaknow')
    결과 : 'idonnaknow'

    </code></pre>

- 해당 Key가 딕셔너리 안에 있는지 확인할 때 (in)

    <pre><code>
    capital = {'korea':'seoul', 'usa':'washington', 'japan':'tokyo', 'russia':'moscow'}
    
    'korea' in capital == True
    'swiss' in capital == False
    </code></pre>