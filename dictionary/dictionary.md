### Dictionary란?
- 대응관계를 나타낼 수 있는 자료형
- 연관 배열(Associative array) 또는 해시(Hash)라고 함
- Key와 Value를 한 쌍으로 갖는 자료형

### How to make Dictionary?
```python
{Key1:Value1, Key2:Value2, Key3:Value3, ...}
```
- Key와 Value의 쌍 여러 개가 {}로 둘러쌓여 있다. 
- 각각의 요소는 Key : Value 형태로 이루어져 있고, 쉼표로 구분함
- Value에는 다양한 데이터타입이 들어갈 수 있다
- Key는 고유한 값이므로 중복되는 Key 값을 설정해놓으면 하나를 제외한 나머지것들이 모두 무시됨
- 동일한 Key가 2개 존재할 경우 앞에 쌍이 무시됨
- Key에 리스트는 들어갈 수 없음 (왜? 리스트는 항상 값이 바뀔수 있기 때문)
- 