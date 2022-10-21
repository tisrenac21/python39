# 마리아디비로 데이터 다루기 1 - select
# pymysql 모듈을 먼저 설치 : pip install pymysql
import pymysql

url = 'localhost'
dbid = 'root'
dbpw = '1234'
dbname = 'bigdata'

conn = pymysql.connect(host=url, user=dbid, password=dbpw, database=dbname, charset='utf8')

cur = conn.cursor()
sql = 'select memberId, password, memberName, email from member'
cur.execute(sql)

result = ''
rows = cur.fetchall()    # 커서에서 데이터 한 건을 읽어온 후
for row in rows:
    # 읽어온 결과에서 각 컬럼값을 변수에 저장하고 출력
    result += f'{row[0]} {row[1]} {row[2]} {row[3]}\n'

cur.close()
conn.close()
print(result)


# 마리아디비로 데이터 다루기 - insert
import pymysql

url = 'localhost'
dbid = 'root'
dbpw = '1234'
dbname = 'bigdata'

userid = input('아이디는?')
passwd = input('비밀번호는?')
name = input('이름은?')
email = input('이메일은?')

conn = pymysql.connect(host=url, user=dbid, password=dbpw, database=dbname, charset='utf8')
cur = conn.cursor()

# 아래 방식은 비추 - SQL injection 공격의 위험 존재!
# sql = 'insert into member values ('+userid+', '+passwd+', '+name+', '+email+')'

# sql = f'insert into member values ({userid},{passwd},{name},{email})'

# 매개변수 placeholder(?)
sql = f'insert into member(memberId, password, memberName, email) values (%s,%s,%s,%s)'
params = (userid, passwd, name, email)
cur.execute(sql, params)
conn.commit()    # 테이블에 값 저장하기 위해 commit 호출
print(cur.rowcount, '행이 추가됨!!')

cur.close()
conn.close()