# 파이썬으로 데이터 다루기 2 - insert
# 입력한 회원정보를 member 테이블에 저장
import sqlite3

#회원정보 입력받기
userid = input('아이디는?')
passwd = input('비밀번호는?')
name = input('이름은?')
email = input('이메일은?')

conn = sqlite3.connect('c:/Java/bigdata.db')
cur = conn.cursor()

# 아래 방식은 비추 - SQL injection 공격의 위험 존재!
# sql = 'insert into member values ('+userid+', '+passwd+', '+name+', '+email+')'

# sql = f'insert into member values ({userid},{passwd},{name},{email})'

# 매개변수 placeholder(?)
sql = f'insert into member values (?,?,?,?)'
params = (userid, passwd, name, email)
cur.execute(sql, params)
conn.commit()    # 테이블에 값 저장하기 위해 commit 호출
print(cur.rowcount, '행이 추가됨!!')

cur.close()
conn.close()

# 파이썬으로 데이터 다루기 3 - update
# 수정할 회원의 아이디를 입력받아 회원정보 수정
import sqlite3

userid = input('수정할 회원의 아이디를 입력하세요: ')
passwd = input('새로운 비밀번호를 입력하세요: ')
name = input('수정할 이름을 입력하세요: ')
email = input('수정할 이메일 입력: ')

conn = sqlite3.connect('c:/Java/bigdata.db')
cur = conn.cursor()

# named parameter placeholder를 이용해서 실제값 지정
sql = f'update member set passwd = :pwd, name = :name, email = :eml where userid = :uid'
params = {'pwd':passwd, 'name':name, 'eml':email, 'uid':userid}
cur.execute(sql, params)
conn.commit()
print(cur.rowcount, '수정됌')

cur.close()
conn.close()

# 파이썬으로 데이터 다루기 4 - delete
# 삭제할 회원의 아이디를 입력받아 회원정보 삭제
import sqlite3

userid = input('삭제할 아이디 입력')

conn = sqlite3.connect('c:/Java/bigdata.db')
cur = conn.cursor()

sql = f'delete from member where userid = :uid'
params = {'uid':userid}

cur.execute(sql, params)
conn.commit()
print(cur.rowcount, '행삭제')

cur.close()
conn.close()