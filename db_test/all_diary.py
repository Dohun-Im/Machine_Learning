# 내가만든 db_test안의 dao 모듈을 import

import db.daoClass2  as dao2

dao2 = dao2.DAO2()
rows = dao2.all()

for i in range(len(rows)):
    print(rows[i])


for row in rows:
    print('결과는 ' + str(row[0]) + " " + row[1] + " " + row[2] + " " + row[3])
