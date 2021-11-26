from tkinter import *
import db.daoClass2 as dao2



def create():

    vo = [title_text.get(), content_text.get() ]

    dao2 = dao2.DAO2()
    dao2.create(vo)

def delete():
    vo = [id_text.get()]

    dao2 = dao2.DAO2()
    dao2.delete(vo)

def update():
    vo = [title_text.get(), content_text.get(),id_text.get()]

    dao2 = dao2.DAO2()
    dao2.update(vo)
w = Tk()
# w.~~ 테두리 설정
w.geometry('700x1000')
w.config(bg='lightgray')

icon=PhotoImage(file='야통.png')
dogLabel=Label(w,image=icon) # w는 부모임. 주소값이 들어있다!, 라벨에다가 이미지를 넣어서 표시
dogLabel.pack()

id_label = Label(w,text='id 입력',font=('맑은 고딕',20),bg='lightgray',fg='blue')
id_label.pack()

id_text=Entry(w,font=('맑은 고딕',20),bg='yellow',fg='red')
id_text.pack()

title_label = Label(w,text='title 입력',font=('맑은 고딕',20),bg='lightgray',fg='blue')
title_label.pack()

title_text=Entry(w,font=('맑은 고딕',20),bg='yellow',fg='red')
title_text.pack()

content_label = Label(w,text='content 입력',font=('맑은 고딕',20),bg='lightgray',fg='blue')
content_label.pack()

content_text=Entry(w,font=('맑은 고딕',20),bg='yellow',fg='red')
content_text.pack()

#command 에는 함수명 넣기.
button = Button(w,width=30,height=1,bg='green',font=('맑은 고딕',10),text='개시물 작성',command=create)
button.pack()

button2 = Button(w,width=30,height=1,bg='green',font=('맑은 고딕',10),text='게시물 삭제',command=delete)
button2.pack()

button3 = Button(w,width=30,height=1,bg='green',font=('맑은 고딕',10),text='게시물 수정',command=update)
button3.pack()
w.mainloop()