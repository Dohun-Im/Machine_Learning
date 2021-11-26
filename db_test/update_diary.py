# 내가만든 db_test안의 dao 모듈을 import

import db.daoClass2  as dao2

id = input('id>> ')
title = input('title>> ')
content = input('content>> ')


vo = list()
vo.append(title)
vo.append(content)
vo.append(id)

dao2 = dao2.DAO2()
dao2.update(vo)

print('-----------')