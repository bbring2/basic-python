# 문자열 인덱싱과 슬라이싱
# 인덱싱은 가리키는 것 슬라이싱은 자르는 것
# 자바랑 동일함 첫자리는 0부터 시작

# string indexing
a = "Life is too short, You need Python"
lion = a[0]+a[1]+a[9]+a[23]
print(lion)

# how to use indexing?
print(a[-1]+a[-2])

# string slicing
# it means a[0] <= slicing < a[6]
slicing = a[0:6]
print(slicing)

# print entire String
print(a[:])

# how to use slicing
ex = "20220311Sunny"
date = ex[:8]
weather = ex[8:]
print("date: " + date)
print("weather: " + weather)