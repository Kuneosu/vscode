# 랜덤으로 변호사 번호 / 이름 / 이메일 / 연락처 / 착수금 데이터를 생성한다.
# lawyers[i] / names[i] / emails[i] / numbers[i] / prices[i]

# 오라클 DB와 연결한다.
# 오라클 DB에서 LAW 데이터베이스에 접속한다.
# 변호사 테이블에 위에서 생성한 데이터를 삽입한다.
# pip install cx_Oracle 필요
import cx_Oracle

# Oracle DB 연결 정보 설정
dsn_tns = cx_Oracle.makedsn('호스트', '포트번호', service_name='서비스명')
username = '사용자명'
password = '비밀번호'

# Oracle DB 연결
connection = cx_Oracle.connect(username, password, dsn_tns)

# 연결된 Oracle DB와 작업 수행

cursor = connection.cursor()

# SQL 쿼리 실행
cursor.execute("SELECT * FROM 테이블명")

# 결과 가져오기
results = cursor.fetchall()

# 결과 출력
for row in results:
    print(row)

# 커서 닫기
cursor.close()

# ...

# Oracle DB 연결 종료
connection.close()


# 반복한다.