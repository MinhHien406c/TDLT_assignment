import tkinter as tk
import re

root= tk.Tk()

root.geometry("800x400")
root.title("Phần mềm xác nhận tính hợp lệ của mật khẩu")

def kiemtrangam(mk):
    if len(mk)<6 or len(mk)>12:
        kq=1
    else:
        if not re.search("[a-z]",mk):
            kq=2
        elif not re.search ("[0-9]",mk):
            kq=3
        elif not re.search ("[A-Z]",mk):
            kq=4
        elif not re.search ("[$#@]",mk):
            kq=5
        else:
            kq=0
    return kq

def kiemtra():
    mk=textbox.get()
    kq=kiemtrangam(mk)
    if kq==1:
        textbox.delete(0, tk.END)
        thbao=tk.Label(text="Độ dài không hợp lệ, nhập lại",font = ("Arial",8)).pack()
    elif kq==2:
        textbox.delete(0, tk.END)
        thbao=tk.Label(text="Mật khẩu không có chữ thường, nhập lại",font = ("Arial",8)).pack()
    elif kq==3:
        textbox.delete(0,tk.END)
        thbao=tk.Label(text="Mật khẩu không có chữ số, nhập lại", font = ("Arial",8)).pack()
    elif kq==4:
        textbox.delete(0,tk.END)
        thbao=tk.Label(text="Mật khẩu không có chữ hoa, nhập lại", font = ("Arial",8)).pack()
    elif kq==5:
        textbox.delete(0,tk.END)
        thbao=tk.Label(text="Mật khẩu không có kí tự đặc biệt, nhập lại", font = ("Arial",8)).pack()
    elif kq==0:
        thbao=tk.Label(text="Mật khẩu đã hợp lệ " + mk, font = ("Arial",8)).pack()

label = tk.Label(root, text = "Xác thực tính hợp lệ", font = ("Arial", 18))
label.pack(padx=20, pady=20)

label_title=tk.Label(root, text = "Mật khẩu hợp lệ là mật khẩu có độ dài từ 6 đến 12 kí tự, có chữ số, chữ thường, chữ hoa và kí tự đặc biệt", font=("Arial",10))
label_title.pack()

label_1 = tk.Label(root, text = "Mời nhập mật khẩu", font = ("Arial",10))
label_1.pack(padx=5,pady=10)

textbox= tk.Entry(root, width=50, font=("Arial", 16))
textbox.pack(padx=20,pady=10)

button= tk.Button(root, text="Kiểm tra", font=("Arial", 18), command=kiemtra)
button.pack(padx=10,pady=10)

label_2 = tk.Label(root, text="Thông báo", font = ("Arial", 15))
label_2.pack(padx=10,pady=10)

root.mainloop()