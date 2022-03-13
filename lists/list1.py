# 파이썬 리스트는 안에 아무런 데이터타입 상관없음 다 넣어도됨
a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = ['1', '2', 'Life', 'is']
e = [1, 2, ['Life', 'is']]
f = [4, 5, 6]

# 리스트 인덱싱
print(b[0]+b[2])
print(d[0]+d[1])
print(e[2])
print(e[2][0]+" "+e[2][1]+" "+c[2]+" "+c[3])

# 리스트 슬라이싱
print(b[0:2])
print(d[1:3])
print(c[:2])
print(e[1:])

# 리스트 연산하기
print(b+c)
print(b*3)

# 리스트 길이구하기
print(len(d))

# 리스트에서 값 수정하기
del b[1]
del e[:2]
print(b)
print(e)