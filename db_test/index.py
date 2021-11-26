from tkinter import *
import db.dao as dao

def create():
    vo = [id_text.get(), pw_text.get(), name_text.get(), tel_text.get()]

    dao.create(vo)
    print('-----------')

def delete():
    vo = [id_text.get()]

    dao.delete(vo)

def update():
    vo = [pw_text.get(), tel_text.get(),id_text.get()]

    dao.update(vo)
w = Tk()
# w.~~ 테두리 설정
w.geometry('700x1000')
w.config(bg='lightgray')

icon=PhotoImage(file='야통.png')
dogLabel=Label(w,image=icon) # w는 부모임. 주소값이 들어있다!, 라벨에다가 이미지를 넣어서 표시
dogLabel.pack()

id_label = Label(w,text='아이디입력',font=('맑은 고딕',20),bg='lightgray',fg='blue')
id_label.pack()

id_text=Entry(w,font=('맑은 고딕',20),bg='yellow',fg='red')
id_text.pack()

pw_label = Label(w,text='패스워드입력',font=('맑은 고딕',20),bg='lightgray',fg='blue')
pw_label.pack()

pw_text=Entry(w,font=('맑은 고딕',20),bg='yellow',fg='red')
pw_text.pack()

name_label = Label(w,text='이름입력',font=('맑은 고딕',20),bg='lightgray',fg='blue')
name_label.pack()

name_text=Entry(w,font=('맑은 고딕',20),bg='yellow',fg='red')
name_text.pack()

tel_label = Label(w,text='전화번호입력',font=('맑은 고딕',20),bg='lightgray',fg='blue')
tel_label.pack()

tel_text=Entry(w,font=('맑은 고딕',20),bg='yellow',fg='red')
tel_text.pack()

#command 에는 함수명 넣기.
button = Button(w,width=30,height=1,bg='green',font=('맑은 고딕',10),text='회원가입',command=create)
button.pack()

button2 = Button(w,width=30,height=1,bg='green',font=('맑은 고딕',10),text='회원탈퇴',command=delete)
button2.pack()

button3 = Button(w,width=30,height=1,bg='green',font=('맑은 고딕',10),text='회원수정',command=update)
button3.pack()
w.mainloop()