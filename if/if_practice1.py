money = 2000
card = True
if money>=3000:
    print("택시")
else:
    print("걷기")

# 돈이 3000원 이상있거나 카드가 있다면 택시 그렇지 않으면 도보
if money>=3000 or card:
    print("택시")
else:
    print("도보")

print(1 in [2,3,4])
print((1,) not in (1,2,3))

# 주머니에 돈이 있다면 택시를 타고 없으면 걸어가기
pocket = ["money", "cellphone", "key"]
if("money" in pocket):
    print("택시")
else:
    print("도보")

# 조건문에서 아무일도 하지 않게 설정하기
if('money' in pocket):
    pass
else:
    print("카드를 꺼내세요.")
