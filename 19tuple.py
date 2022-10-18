# 튜플tuple
# 파이썬의 리스트와 유사한 자료구조 - 순서기억, 중복저장
# 선언방법은 값들을 ()안에 정의하고 사용
# 단, 튜플의 요소는 수정이나 삭제 불가 (생성은 가능)
# 주로, 읽기전용 데이터를 다룰때 사용 - 상수값 저장

# 튜플 선언
nums = (1, 5, 10, 15, 20)
print(nums)

# 튜플의 요소 읽기 : 객체명[인덱스]
print(nums[0], nums[3])

# 튜플의 요소 수정 : 객체명[인덱스] = 수정값
nums[0] = 999       # => 실행되지 않는다.

# 튜플의 요소 삭제 : del 객체명[인덱스]
del nums[1]          # => 실행되지 않는다.

# 만일, 튜플의 요소를 수정/삭제하려면
# 튜플을 리스트로 변환한 후 값을 수정/삭제하고
# 다시 리스트를 튜플로 변환하면 된다 : list(객체명)
    # # (별로 추천하는 방식은 아님.
    # # 튜플은 최대한 수정/삭제를 하지 않는 경우에 사용한다고 생각하면 된다.)
# 변환함수 : list(객체명), tuple(객체명)
nums = list(nums)       # 튜플 -> 리스트

nums[0] = 999
print(nums)

nums = tuple(nums)      # 리스트 -> 튜플
print(nums)

# ex) 년도를 입력하면 십간와 심이지를 이용해서
# 해당년도의 60갑자(간지) 출력
# 십간: 갑을병정무기경신임계
# 심이지: 자축인묘진사오미신유슬해

BASE = 1444
ten = ('갑', '을', '병', '정', '무', '기', '경', '신', '임', '계')
twelve = tuple('자축인묘진사오미신유술해'[:])
# twelve = ('자', '축', '인', '묘', '진', '사', '오', '미', '신', '유', '술', '해')
animal = tuple('쥐 소 호랑이 토끼 용 뱀 말 양 원숭이 닭 개 돼지'.split(' '))
# animal = ('쥐', '소', '호랑이', '토끼', '용', '뱀', '말', '양', '원숭이', '닭', '개', '돼지')

year = int(input("연도 입력 : "))
i1 = (year - BASE) % 10
i2 = (year - BASE) % 12
print(f'{year}년은 {ten[i1]+twelve[i2]}년({animal[i2]}의 해)입니다.')