# Hello World 출력하기

print("Hello World!")

# 변수에 Hello World 넣어 출력하기

hello = "Hello World!!"
print(hello)


# 숫자형 변수

a = 2
b = 4
print(a*b)
print(a**b)

# 문자형 변수

multiline = """
라팔아
팔렸니
아니오
"""

print(multiline)

# 출력결과 :
#    라팔아
#    팔렸니
#    아니오


# 문자형 변수 연산

plus = '더하기'
divide = '나누기'

print(plus + divide) //결과 : 더하기나누기
print(divide * 3) //결과 : 나누기나누기나누기

# 문자열 인덱싱

index = '21세기는 정보화시대로서 코딩이 중요하게 여겨집니다.'

print(index[3])
print(index[-1])
print(index[-5])
print(index[:10])
print(index[7:])
print(index[0])

# 리스트

number_list = [1, 3, 5, 7, 9]
complex_list = [1, 'python', 'aaa', 'bbb']
nested_list = [1, 3, 5, ['aa', 'bb', 'cc']]

print(number_list[0])
print(complex_list[2])
    
print(number_list[0] + number_list[3])