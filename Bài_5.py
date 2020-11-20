'''- Tạo một List gồm cấc số thực (có thể tạo bằng tay hoặc ngẫu nhiên) (lưu ý: nằm ngoài vòng lặp)
- Thực hiện lặp truy xuất đến từng phần tử trong List và in giá trị của từng phần tử ra màn hình
- Thực hiện lặp truy xuất đến từng phần tử trong List và thực hiện tính logarith của từng phần tử và in giá trị đó ra màn hình'''
def bai5():   
    import math

    n=int(input("n="))
    lst=[]
    for i in range(n):
        lst.append(float(input("Chọn số đi bạn ^^ :")))
    for i in lst:
        print("Giá trị của lst[",i,"] và logarit của phần tử đó là:", math.log10(i))
k=int(input("Số lần lặp:"))
for i in range(k):
    bai5()
print("End.")
