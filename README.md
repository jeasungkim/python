# python
## 자료형
#### 숫자형
* 정수 : 123,-20, 0  
* 실수 : 123.45, -4321.5, 6.08e9  
* 8잔수 : 0o456, 0o123  
* 16진수 : 0xFF, 0x0D, 0x0A

#### 변수
* 문자 또는 밑줄로 시작(beta,_kim)
* 대소문자를 구분한다.(sum, Sum SUM)
* 영문자, 숫자, 밑줄(A~z,0~9,_)
* 파이썬 키워드는 사용 불가
* a = 10
b = 20
c = a + b
print(c)

a = 10
b = 2
c = a/b #나눗셈
d = a-b
e = a*b
f = a//b # 몪
g = a%b #나머지
h = a**b #제곱
print(c,d,e,f,g,h)
# 시험 나옴

#### 문자열
1. 큰 따옴표 : "Hello World! it\'s"
2. 작은 따옴표 : '대한민국'
3. 큰따옴표 3 : """hello!"""
4. 작은 따옴표 3 :'''Life is too short. You need pyhton.'''

myName = "jeasung Kim" # 중간에 대문자 낙타표기법 (카멜)
my_name = "김재성" # 언더바 스네이크표기법
_my_name = "korea"
MYNAME = "God is love" # 앞에대문자 파스칼표기법
my2name = "12345"
# 2myname = "123"  my-name = "231" my name = "231" 안됨 시험출제
myStr = '123' #글자 stf
myNum = 123 # int

print(myStr, myNum)
print(type(myStr))
print(type(myNum))

x,y,z = "포도", "딸기", "수박"
print(x)
print(y)
print(z)

a = b = c = "오렌지"
print(a)
print(b)
print(c)

fruits = ["포도", "딸기", "수박"]
x,y,z = fruits
print(x)
print(y)
print(z)

x = "Life"
y = "is"
z = "beautiful"
print(x,y,z) # ,는 띄어쓰기
print(x+y+z)

a = 1
b = 2
c = 3
print(a,b,c)
print(a+b+c)

#### 데이터 유형 
+ 텍스트
+ 숫자
+ 불(bool)

a = 100
b = 200
good = a + b
print(a, '+', b, '=', good)
