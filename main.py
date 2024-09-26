from tkinter import *
from datetime import *

def update_time():
    now = datetime.now()
    current = now.strftime("%Y-%m-%d %H시%M분%S초")
    ctime.config(text=current)
    window.after(1000, update_time)

window = Tk()
window.title('스트리밍 수익 수수료 계산기')
window.geometry('1280x720')

#프레임
frame1 = Frame(window, width=200, height=900, bg='gray')
frame1.pack_propagate(False)
frame1.pack(side='left', fill='y')

frame2 = Frame(window, width=200, height=900, bg='lightgray')
frame2.pack_propagate(False)
frame2.pack(side='left', fill='y')

frame3 = Frame(window, width=1200, height=900, bg='white')
frame3.pack(fill='y')

#메인메뉴 프레임
basic_menu = Label(frame1, text='메인메뉴, 사진/로고', bg='gray')
basic_menu.pack(pady=50)

#메인메뉴 버튼
button1 = Button(frame1, text='□ CHZZK', bg='gray', width=20)
button1.pack(pady=10)

button2 = Button(frame1, text='□ AFREECA TV', bg='gray', width=20)
button2.pack(pady=10)

button2 = Button(frame1, text='□ SPOON', bg='gray', width=20)
button2.pack(pady=10)

button2 = Button(frame1, text='□ 메모', bg='gray', width=20)
button2.pack(pady=10)


#서브메뉴 프레임
sub_menu = Label(frame2, text='서브 메뉴', bg='lightgray')
sub_menu.pack(pady=20)

#서브메뉴 버튼
sub_button1 = Button(frame2, text='test1')
sub_button1.pack(pady=10)

sub_button2 = Button(frame2, text='test2')
sub_button2.pack(pady=10)

#기능화면
feature_label = Label(frame3, text='기능 화면', bg='white')
feature_label.pack(pady=20)


ctime = Label(frame1, text="", bg='gray')
ctime.pack(side='bottom', pady=10)
update_time()

window.mainloop()