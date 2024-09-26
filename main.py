from tkinter import *
from tkinter import ttk
from datetime import *

def update_time():
    now = datetime.now()
    current = now.strftime("%Y-%m-%d %H시%M분%S초")
    ctime.config(text=current)
    window.after(1000, update_time)

def sub_chzzk():
    for button in frame2.winfo_children():
        button.destroy()
    Label(frame2, text='치지직 수익 수수료 계산', bg='lightgray', font=('Arial',12)).pack(pady=20)

    job_var = StringVar(value="개인")  # 기본값 설정
    Radiobutton(frame2, bg='lightgray', text="개인", variable=job_var, value="개인").pack(pady=5)
    Radiobutton(frame2, bg='lightgray', text="사업자", variable=job_var, value="사업자").pack(pady=5)
    grade_combobox = ttk.Combobox(frame2, width=15, values=["루키", "프로", "파트너"])
    grade_combobox.pack(pady=10)
    Button(frame2, text='초기화').pack(pady=10)


def sub_afreeca():
    for button in frame2.winfo_children():
        button.destroy()
    Label(frame2, text='아프리카TV 수익 수수료 계산', bg='lightgray', font=('Arial',12)).pack(pady=20)

    job_var = StringVar(value="개인")  # 기본값 설정
    Radiobutton(frame2, bg='lightgray', text="개인", variable=job_var, value="개인").pack(pady=5)
    Radiobutton(frame2, bg='lightgray', text="사업자", variable=job_var, value="사업자").pack(pady=5)
    grade_combobox = ttk.Combobox(frame2, width=15, values=["일반BJ", "베스트BJ", "파트너BJ"])
    grade_combobox.pack(pady=10)
    Button(frame2, text='초기화').pack(pady=10)


def sub_spoon():
    for button in frame2.winfo_children():
        button.destroy()
    Label(frame2, text='스푼라디오 수익 수수료 계산', bg='lightgray', font=('Arial',12)).pack(pady=20)

    grade_combobox = ttk.Combobox(frame2, width=15, values=["일반", "초이스", "STAR초이스", "TOP초이스"])
    grade_combobox.pack(pady=10)
    Button(frame2, text='초기화').pack(pady=10)

window = Tk()
window.title('스트리밍 수익 수수료 계산기')
window.geometry('900x720')

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
button1 = Button(frame1, text='□ CHZZK', bg='gray', width=20, command=sub_chzzk)
button1.pack(pady=10)

button2 = Button(frame1, text='□ AFREECA TV', bg='gray', width=20, command=sub_afreeca)
button2.pack(pady=10)

button2 = Button(frame1, text='□ SPOON', bg='gray', width=20, command=sub_spoon)
button2.pack(pady=10)

button2 = Button(frame1, text='□ 메모', bg='gray', width=20)
button2.pack(pady=10)


#서브메뉴 프레임
sub_menu = Label(frame2, text='서브 메뉴', bg='lightgray')
sub_menu.pack(pady=20)


#기능화면
feature_label = Label(frame3, text='기능 화면', bg='white')
feature_label.pack(pady=20)


ctime = Label(frame1, text="", bg='gray')
ctime.pack(side='bottom', pady=10)
update_time()

window.mainloop()