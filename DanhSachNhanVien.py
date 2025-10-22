import os

class DanhSachNhanVien:
    def __init__(self, filename="nhanvien.txt"):
        self.filename = filename
        self.nhan_vien_list = []
        if os.path.exists(self.filename):
            self.load_from_file()

    def nhap_va_luu(self):
        so_nv = int(input("Nhập số lượng nhân viên: "))
        for i in range(so_nv):
            print(f"\nNhập thông tin nhân viên thứ {i+1}:")
            ma_nv = input("Mã nhân viên: ").strip()
            ten_nv = input("Họ tên: ").strip()
            tuoi = input("Tuổi: ").strip()
            phong_ban = input("Phòng ban: ").strip()
            luong = input("Lương: ").strip()

            nhan_vien = {
                "Mã NV": ma_nv,
                "Họ tên": ten_nv,
                "Tuổi": tuoi,
                "Phòng ban": phong_ban,
                "Lương": luong
            }
            self.nhan_vien_list.append(nhan_vien)

        self.save_to_file()
        print("\nĐã lưu thông tin nhân viên vào file 'nhanvien.txt' thành công!")

    def save_to_file(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            f.write("Danh sách nhân viên:\n")
            f.write("---------------------------------------------\n")
            for nv in self.nhan_vien_list:
                f.write(f"{nv['Mã NV']} | {nv['Họ tên']} | {nv['Tuổi']} | {nv['Phòng ban']} | {nv['Lương']}\n")

    def load_from_file(self):
        self.nhan_vien_list = []
        with open(self.filename, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Bỏ 2 dòng đầu (header + separator)
        start = 0
        if len(lines) >= 1 and "Danh sách" in lines[0]:
            start = 2  # giả sử dòng thứ 2 là đường kẻ
        for line in lines[start:]:
            line = line.strip()
            if not line:
                continue
            # tách theo dấu '|' và strip từng phần
            parts = [p.strip() for p in line.split("|")]
            # đảm bảo có đủ trường
            if len(parts) >= 5:
                nv = {
                    "Mã NV": parts[0],
                    "Họ tên": parts[1],
                    "Tuổi": parts[2],
                    "Phòng ban": parts[3],
                    "Lương": parts[4]
                }
                self.nhan_vien_list.append(nv)
            else:
                pass
#------------------------------------------------------------------------------------------
    def tim_theo_ma(self):
        print("Danh sách mã NV hiện có:", [nv["Mã NV"] for nv in self.nhan_vien_list])
        ma_tim = input("Nhập mã nhân viên cần tìm: ").strip()
        found = False

        for nv in self.nhan_vien_list:
            if nv["Mã NV"].strip() == ma_tim:
                print("\nThông tin nhân viên tìm được:")
                print(f"Mã NV: {nv['Mã NV']}")
                print(f"Họ tên: {nv['Họ tên']}")
                print(f"Tuổi: {nv['Tuổi']}")
                print(f"Phòng ban: {nv['Phòng ban']}")
                print(f"Lương: {nv['Lương']}")
                found = True
                break
        if not found:
            print("Không tìm thấy nhân viên với mã đã nhập.")
#------------------------------------------------------------------------------------------
    def xoa_theo_ma(self):
        print("Danh sách mã NV hiện có:", [nv["Mã NV"] for nv in self.nhan_vien_list])
        ma_xoa = input("Nhập mã nhân viên cần xóa: ").strip()
        initial_count = len(self.nhan_vien_list)
        self.nhan_vien_list = [nv for nv in self.nhan_vien_list if nv["Mã NV"].strip() != ma_xoa]

        if len(self.nhan_vien_list) < initial_count:
            self.save_to_file()
            print(f"Đã xóa nhân viên với mã {ma_xoa} và cập nhật file.")
        else:
            print("Không tìm thấy nhân viên với mã đã nhập.")
#------------------------------------------------------------------------------------------

    def cap_nhat_thong_tin(self):
        print("Danh sách mã NV hiện có:", [nv["Mã NV"] for nv in self.nhan_vien_list])
        ma_cap_nhat = input("Nhập mã nhân viên cần cập nhật: ").strip()
        found = False

        for nv in self.nhan_vien_list:
            if nv["Mã NV"].strip() == ma_cap_nhat:
                print("\nNhập thông tin mới (để trống nếu không muốn thay đổi):")
                ten_moi = input(f"Họ tên ({nv['Họ tên']}): ").strip()
                tuoi_moi = input(f"Tuổi ({nv['Tuổi']}): ").strip()
                phong_ban_moi = input(f"Phòng ban ({nv['Phòng ban']}): ").strip()
                luong_moi = input(f"Lương ({nv['Lương']}): ").strip()

                if ten_moi:
                    nv['Họ tên'] = ten_moi
                if tuoi_moi:
                    nv['Tuổi'] = tuoi_moi
                if phong_ban_moi:
                    nv['Phòng ban'] = phong_ban_moi
                if luong_moi:
                    nv['Lương'] = luong_moi

                self.save_to_file()
                print("Đã cập nhật thông tin nhân viên và lưu vào file.")
                found = True
                break
        if not found:
            print("Không tìm thấy nhân viên với mã đã nhập.")

    def cap_nhat_theo_ma(self):
        self.cap_nhat_thong_tin()
    def hien_thi_danh_sach(self):
        if not self.nhan_vien_list:
            print("Danh sách nhân viên trống.")
            return

#------------------------------------------------------------------------------------------



    def tim_theo_khoang_luong(self):
        try:
            luong_min = float(input("Nhập mức lương thấp nhất: ").strip())
            luong_max = float(input("Nhập mức lương cao nhất: ").strip())
        except ValueError:
            print("Vui lòng nhập số hợp lệ cho lương.")
            return

        found_nvs = []
        for nv in self.nhan_vien_list:
            try:
                luong_nv = float(nv["Lương"].replace(",", "").strip())
                if luong_min <= luong_nv <= luong_max:
                    found_nvs.append(nv)
            except ValueError:
                continue

        if found_nvs:
            print(f"\nNhân viên có lương trong khoảng {luong_min} đến {luong_max}:")
            for nv in found_nvs:
                print(f"Mã NV: {nv['Mã NV']}, Họ tên: {nv['Họ tên']}, Lương: {nv['Lương']}")
        else:
            print("Không tìm thấy nhân viên trong khoảng lương đã nhập.")

#------------------------------------------------------------------------------------------
    def sap_xep_theo_ho_ten(self):
        self.nhan_vien_list.sort(key=lambda nv: nv["Họ tên"].lower())
        self.save_to_file()
        print("Đã sắp xếp nhân viên theo họ và tên và cập nhật file.")     

#------------------------------------------------------------------------------------------
    def sap_xep_theo_thu_nhap(self):
        def get_luong(nv):
            try:
                return float(nv["Lương"].replace(",", "").strip())
            except ValueError:
                return 0.0

        self.nhan_vien_list.sort(key=get_luong, reverse=True)
        self.save_to_file()
        print("Đã sắp xếp nhân viên theo thu nhập và cập nhật file.")
#------------------------------------------------------------------------------------------
    def xuat_5_nhan_vien_luong_cao_nhat(self):
        def get_luong(nv):
            try:
                return float(nv["Lương"].replace(",", "").strip())
            except ValueError:
                return 0.0

        sorted_nvs = sorted(self.nhan_vien_list, key=get_luong, reverse=True)
        top_5_nvs = sorted_nvs[:5]

        print("\n5 nhân viên có thu nhập cao nhất:")
        for nv in top_5_nvs:
            print(f"Mã NV: {nv['Mã NV']}, Họ tên: {nv['Họ tên']}, Lương: {nv['Lương']}")
           