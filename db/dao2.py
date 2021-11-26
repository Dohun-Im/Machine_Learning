import pymysql

# def create(id, pw, name, tel):(클래스로 할때)
def create(vo): #(리스트로 할때)
    #1. conn
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='1234',
                           db='cloth',
                           charset='utf8')
    print('1. db연결 성공', conn)

    #2. cursur
    cur = conn.cursor()
    print('2. db연결 스트림을 접근할 수 있는 객체 획득 성공', cur)
    #3. sql문 작성후 쿼리 날림. 사용 용도에 맞게
    #클래스로 할때
    # sql =  "insert into member values ('" + id + "', '" + pw + "', '" +  name + "', '" + tel + "')"
    #리스트로 할때
    # sql = "insert into member values ('" + vo[0] + "', '" + vo[1] + "', '" + vo[2] + "', '" + vo[3] + "')"
    sql = "insert into diary (writeday, title, content) values ( %s, %s, %s)"
    result = cur.execute(sql, vo) #%s에 vo리스트 안의 값을 넣기
    print('3. sql문을 만들어서 mysql로 보낸 후 결과값>>', result)

    conn.commit() #확정하는것
    conn.close() #연결 종료

def update(vo):
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='1234',
                           db='cloth',
                           charset='utf8')
    print('1. db연결 성공', conn)

    # 2. cursur
    cur = conn.cursor()
    print('2. db연결 스트림을 접근할 수 있는 객체 획득 성공', cur)

    sql = "update diary set title = %s, content = %s where id = %s"
    result = cur.execute(sql, vo)  # %s에 vo리스트 안의 값을 넣기
    print('3. sql문을 만들어서 mysql로 보낸 후 결과값>>', result)

    conn.commit()
    conn.close()

def delete(vo):
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='1234',
                           db='cloth',
                           charset='utf8')
    print('1. db연결 성공', conn)

    # 2. cursur
    cur = conn.cursor()
    print('2. db연결 스트림을 접근할 수 있는 객체 획득 성공', cur)

    sql = "delete from diary where id = %s"
    result = cur.execute(sql, vo)  # %s에 vo리스트 안의 값을 넣기
    print('3. sql문을 만들어서 mysql로 보낸 후 결과값>>', result)

    conn.commit()
    conn.close()

def read(id):
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='1234',
                           db='cloth',
                           charset='utf8')
    print('1. db연결 성공', conn)

    # 2. cursur
    cur = conn.cursor()
    print('2. db연결 스트림을 접근할 수 있는 객체 획득 성공', cur)

    sql = "select * from diary where id = %s"
    result = cur.execute(sql, id)  # %s에 vo리스트 안의 값을 넣기

    row = cur.fetchone() #읽어온 결과를 스트림에서 빼와서 보여줘야함
    print(row)
    print('3. sql문을 만들어서 mysql로 보낸 후 결과값>>', result)

    conn.commit()
    conn.close()

    return row

    ## 모듈은 각자의 역할에 충실하도록 만들어야됨. 역할을 섞어서 만들면 안된다!
    ## 응집도
    ## ex) dao.py에는 입력과 출력 역할을 넣으면 안된다~

def all():
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='1234',
                           db='cloth',
                           charset='utf8')
    print('1. db연결 성공', conn)

    # 2. cursur
    cur = conn.cursor()
    print('2. db연결 스트림을 접근할 수 있는 객체 획득 성공', cur)

    sql = "select * from diary"
    result = cur.execute(sql)  # %s에 vo리스트 안의 값을 넣기

    rows = cur.fetchall() #fetchmany 하면 전체중 가져올 사이즈 정할 수 있음
    #읽어온 결과를 스트림에서 빼와서 보여줘야함
    print(len(rows))
    print('3. sql문을 만들어서 mysql로 보낸 후 결과값>>', result)

    conn.commit()
    conn.close()

    return rows

#외부 호출 시 에는 create() 실행 안되도록하는 함수!!
#해당 모듈이 main이 되어서 실행될 때만, 실행해주는 부분!!
if __name__ == '__main__':
    create('','','','')
