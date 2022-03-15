# elif는 개수에 제한없이 사용이 가능함

# 주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 도보
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시")
elif card:
    print("지하철")
else:
    print("도보")

# if문 한 줄로 작성하기
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라!")

# 이렇게 줄일 수 있음
pocket = ['money', 'paper', 'cellphone']
if 'money' in pocket: pass
else: print("카드를 꺼내라라")

