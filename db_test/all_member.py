# 내가만든 db_test안의 dao 모듈을 import

import db.dao as dao

# id = input('id>> ')
# pw = input('pw>> ')
# name = input('name>> ')
# tel = input('tel>> ')

# 값을 전달할 때 묶어서 보내는 역할의 클래스(data transfer object, DTO, value Object, VO)
# db_test.dao.create(id, pw, name, tel)


rows = dao.all()

for i in range(len(rows)):
    print(rows[i])


for row in rows:
    print('결과는 ' + row[0] + " " + row[1] + " " + row[2] + " " + row[3])
