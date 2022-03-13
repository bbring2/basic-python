# 리스트 관련 함수
a = [1, 2, 3, 4, 5]
b = ['o', 'q', 'z', 'a', 'i', 'b', 'c', 'd']
c = [7, 4, 1, 9, 5]

# 1. 리스트에 요소 추가하기 : append
a.append(6)
a.append([7,8])
print(a)

# 2. 리스트 정렬하기 : sort
c.sort()
b.sort()
print(c)
print(b)

# 3. 리스트 뒤집기 : reverse
b.reverse()
print(b)

# 4. 위치 반환하기 : index -> 해당 위치를 알려줌
print(a.index(4))

# 5. 리스트 요소 삽입 : insert
a.insert(0, 100) # 0위치에 100을 삽입
print(a)
b.insert(1, 'ww')
print(b)

# 6. 리스트 요소 제거 : remove -> 리스트에서 첫번째로 나오는 x값을 삭제하는 함수
e = [1,2,3,1,2,3]
e.remove(1)
e.remove(1)
print(e)

# 7. 리스트 요소 끄집어 내기 : pop -> 리스트 맨 마지막 요소를 돌려주고 그 요소 삭제하는 함수
f = [1, 2, 3, 4]
f.pop()
print(f)
# 특정요소를 설정시, 특정번째 요소를 돌려주고 그 요소는 삭제함.
print(f.pop(0))
print(f)

# 8. 리스트에 포함된 요소 x의 개수 세기 : count -> 리스트 안에 x가 몇개 있는지 조사하기
g = [1, 1, 2, 3, 4, 4, 5, 5, 1, 1, 2, 2, 3]
print(g.count(1))

# 9. 리스트 확장 : extend -> x에는 리스트만 올 수 있고, 원래의 특정 리스트에 x 리스트를 더하게 됨
h = [1, 2, 3, 4, 5]
i = [8, 9, 10]
extended_list = h.extend([6, 7])
print(h)
h.extend(i)
print(h)

# a.extend([4,5]) == a+=[4,5]