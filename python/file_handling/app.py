
chon = input("Hãy chọn chế độ: 1. ghi đè/ 2. thêm vào file")
print(chon)
if chon==1:
    with open('demo.txt', 'w') as file:
        dulieu = input("Hãy nhập dữ liệu:")
        file.write(dulieu)
if chon==2:
    with open('demo.txt', 'a') as file:
        dulieu = input("Hãy nhập dữ liệu:")
        file.write(dulieu)



