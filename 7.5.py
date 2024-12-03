print("TRẦN DANH HOÀNG")
print("MSSV:235752021610064")

def file_write_and_read(fname):
    # Mở tệp để ghi nội dung vào cuối tệp (append mode)
    with open(fname, "a") as myfile:
        myfile.write("chuc lam tot\n")
        myfile.write("happy\n")
    
    # Mở tệp để đọc và hiển thị nội dung
    with open(fname, "r") as txt:
        print(txt.read())  # Đọc toàn bộ nội dung của tệp và in ra

# Gọi hàm và sử dụng tệp 'abc.txt'
file_write_and_read(r'C:\Users\asus\Documents\0.1.py')
