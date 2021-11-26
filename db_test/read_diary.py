# 내가만든 db_test안의 dao 모듈을 import

import db.daoClass2  as dao2

id = input('id>> ')

dao2 = dao2.DAO2()
row = dao2.read(id)

print('-----------')
print('결과는' + str(row[0]) + " "+row[1]+ " "+row[2]+" "+row[3])