# 딕셔너리 쌍 추가 및 삭제하기
dictionary1 = {1: 'a'}
dictionary1[2] = 'b'
print(dictionary1)
dictionary1['name'] = 'heejeong'
print(dictionary1)
dictionary1[3] = [1, 2, 3]
print(dictionary1)

# 딕셔너리 요소 삭제하기
# key가 1인 key:value 쌍을 삭제
del dictionary1[1]
print(dictionary1)

sports = {'김연아' : '피겨', '류현진' : '야구', '손흥민' : '축구', '한선수' : '배구'}
# 키값 사용해서 벨류값 얻기
print(sports['류현진'])
