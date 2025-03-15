while True:
    try:
        namefile = input("enter your file name ")
        if not namefile.strip():  # Kiểm tra nếu người dùng nhập rỗng
            print("Error: File name cannot be empty!")
            continue  # Quay lại vòng lặp để nhập lại
        with open(namefile, "r") as file:  # Thử mở file
            print("File content:\n", file.read())  # In nội dung file     
        break  # Nếu thành công, thoát vòng lặp
    
    except FileNotFoundError:  # Nếu file không tồn tại
        print("Error: File not found! Please try again.")
    retry = input("do you want to try again? (y/n)").strip().lower()  #try againt went not find file
    if retry != 'y':
        print(" exting program , Goodbye!")
        break

