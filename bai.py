"""Viết chương trình nhập ba góc của một tam giác và kiểm tra xem tam giác đó có hợp lệ không"""
n_1 = int(input("Nhap goc 1 vao ban phim :"))
n_2 = int(input("Nhap gốc 2 :"))
n_3 = int(input("nhập gốc 3"))
sum = n_1 + n_2 + n_3
print(sum)
if sum != 180:
    print("ko phải tác giam")
else: print("phai tam giác")