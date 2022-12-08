import re

def kiemtra(p):
    if len(p)<6 or len(p)>12:
        kq=1
    else:
        if not re.search("[a-z]",p):
            kq=2
        elif not re.search ("[0-9]",p):
            kq=3
        elif not re.search ("[A-Z]",p):
            kq=4
        elif not re.search ("[$#@]",p):
            kq=5
        else:
            kq=0
    return kq

print("Mật khẩu hợp lệ là mật khẩu có độ dài từ 6 đến 12 kí tự, có chữ số, chữ thường, chữ hoa và kí tự đặc biệt")
t=1
while t==1:
    p = input("Nhập mật khẩu để kiểm tra tính hợp lệ: ")
    kq= kiemtra(p)
    if kq == 1:
        print("Độ dài không hợp lệ, nhập lại")
    elif kq == 2:
        print("Mật khẩu không có chữ thường")
    elif kq == 3:
        print("Mật khẩu không có chữ số")
    elif kq == 4:
        print("Mật khẩu không có chữ hoa")
    elif kq == 5:
        print("Mật khẩu không có kí tự đặc biệt")
    else:
        print("Mật khẩu đã hợp lệ: ",p)
        t=2