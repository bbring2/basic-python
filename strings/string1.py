print("hello world \t no")
print("Hello World")
print('Python is Fun')
print("""Life is too short, You need Python!""")
print('''Life is too short, You need Python!''')

# 문자열에 작은따옴표 포함시키기
food = "Python's favorite food is perl"
print(food)

# 문자열에 큰따옴표 포함시키기
statement = '"Python is very easy." he said.'
print(statement)

# 백슬래시 사용하기
food = 'Python\'s favorite food is pizza'
print(food)

# 백슬래시 사용하지 않기 위해 따옴표 3개 사용하기
multiline = '''
life is too short
you need python 
'''
print(multiline)
multiline = """
why does it work?
i dont understand
because i am java developer
"""
print(multiline)

# 문자열 곱하기
head = "Python"
tail = 'fun'
print(head*3 + ' ' + tail*2)

# multiString
print("=" * 50)
print("HELLO, I AM PYCHARM FOR PYTHON")
print("=" * 50)

# 문자열 길이 구하기 -> length함수를 나타내는 줄임말의 len
nice = "Life is too short"
print(len(nice))