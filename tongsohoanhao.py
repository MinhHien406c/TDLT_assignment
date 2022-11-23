p = 0
s = 0
i = 0
e = 1
a = int(input("so dau day: "))
b = int(input("so cuoi day: "))
for i in range(a,b+1):
    while e <= a-1:
        if a % e == 0:
            s= s + e
        e = e + 1
    if s == a:
        print(f"{a} la so hoan hao ")
        p = p + a
    else:
        print(f"{a} khong la so hoan hao")
    e = 1
    s = 0
    a = a + 1
print("tong la:", p)