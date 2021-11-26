# 내가만든 db_test안의 dao 모듈을 import

import db.daoClass2 as dao2

title = input('title>> ')
content = input('content>> ')

# list로 할때
vo = list()


vo.append(title)
vo.append(content)

dao2 = dao2.DAO2()
dao2.create(vo)

