s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

# 1. 교집합
print(s1&s2)
print(s1.intersection(s2)) # == s2.intersection(s1)

# 2. 합집합
print(s1|s2)
print(s1.union(s2)) # s2.union(s1)

# 3. 차집합
print(s1-s2)
print(s1.difference(s2))
print(s2-s1)
print(s2.difference(s1))

# 4. 값 1개 추가하기
s3 = set([1, 2, 3])
s3.add(4)
print(s3)

# 5. 값 여러개 추가하기
s3.update([5, 6])
print(s3)

# 6. 특정 값 제거하기
s3.remove(5)
print(s3)