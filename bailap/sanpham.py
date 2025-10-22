class sampham: 
    def __init__(self, tensp, giamgiasp, giasp):
        self.giasp = giasp
        self.tensp = tensp
        self.giamgiasp = giamgiasp
        
    def thuenhapkhau(self):
        return self.giasp * 0.1
    
    def nhap_thong_tin_sp(self):
        self.tensp = input("Nhập tên sản phẩm: ")
        self.giasp = float(input("Nhập giá sản phẩm: "))
        self.giamgiasp = float(input("Nhập giảm giá sản phẩm: "))
    def xuat_thong_tin_sp(self):
        print(f"Sản Phẩm {self.tensp} Giá: {self.giasp} Giảm giá: {self.giamgiasp} Thuế nhập khẩu: {self.thuenhapkhau()}")
#gt