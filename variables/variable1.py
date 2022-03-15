a = 1
b = "python"
c = [1, 2, 3]
d = 1
e = [1, 2 ,3]
print(c is e)

# 변수가 가리키는 메모리 주소는 id()메서드 사용
print(id(a))
print(id(c))
print(a is d)

# 리스트 복사
a = [1,2,3]
b = a
print(id(a))
print(id(b))

a is b
a[1] = 4
print(a)
print(b)

# [:] 사용하기 -> 리스트 전체를 가리키는 것
a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a)
print(b)

# copy 모듈 사용하기
from copy import copy
a = [1, 2, 3]
b = copy(a) # b = a[:]

# 변수 만드는 다른 방법
a, b = ('python', 'life')
(a, b) = 'python', 'life'
[a, b] = ['python', 'life']
a = b = 'python'