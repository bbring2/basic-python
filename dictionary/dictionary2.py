# 1. Key 리스트 만들기(keys)
ex1 = {'name': 'jenna', 'phone': '0119110117', 'birth': '1208', 'COB': 'South korea'}
print(ex1.keys())

# 2. Value 리스트 만들기(values)
print(ex1.values())

# 3. Key, Value 쌍으로 얻기(items)
print(ex1.items())

# 4. Key: Value 쌍 모두 지우기(clear)
print(ex1.clear())

# 5. Key로 Value 얻기(get)
ex2 = {'name': 'jenna', 'phone': '0119110117', 'birth': '1208'}
print(ex2.get('birth'))
print(ex2.get('COB')) # NONE 리턴
# print(ex2['COB']) 에러띄움
print(ex2.get('COB', 'Null')) # default 설정

# 6. 해당 Key가 딕셔너리 안에 있는지 조사하기(in)
print('name' in ex2)
print('COB' in ex2)