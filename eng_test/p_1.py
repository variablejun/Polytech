a = {'일본','중국','한국'}
a.add('베트남')
a.add('중국') # 중국은 이미 있기 때문에 추가 안됨
a.remove('일본') # 일본을 지우고
a.update({'홍콩','한국','태국'}) # 이미 있는 한국을 제외한 나머지 것들 추가
print(a)
#{'중국', '한국', '홍콩', '태국', '베트남'} 순서무의미