# 문자 개수 세기
ex1 = "confirmation"
count_result = ex1.count('o')
print(count_result)

# 가장 먼저 사용된 위치 알려주기
ex2 = "Python is really easy."
find_s = ex2.find('s')
find_x = ex2.find('x')
print(find_s)
print(find_x)

# 위치 알려주기
ex3 = "Life is too short."
index_o = ex3.index('o')
print(index_o)

# find와 index의 차이점은 find는 찾는 char가 없을때 -1 반환, index는 에러띄움

# 문자열 삽입
join_comma = ", ".join('abcd')
join_tuple = ",".join(['a, b, c, d'])
print(join_comma)
print(join_tuple)

# 소문자 대문자
lower_case = "banana".upper()
upper_case = "NEW YORK".lower()
print(upper_case + ' ' + lower_case)

# 공백 지우기
left_blank = " hello.".lstrip()
print(left_blank)
right_blank = "no way. ".rstrip()
print(right_blank)
both_blank = " Hola! ".strip()
print(both_blank)

# 문자열 바꾸기
change_string = "Life is too short."
result_after_change = change_string.replace("Life", "Your leg")
print(result_after_change)

# 문자열 나누기
split_ex1 = "My life is so beautiful."
result_split = split_ex1.split()
print(result_split)
split_ex2 = "1:2:3:4:5:6:7:8:9:0"
print(split_ex2.split(':'))

