
# --------- BÀI 1: Tính tiền nước ----------
GIA_BAN_NUOC = (7500, 8800, 12000, 24000)

def tinh_tien_nuoc(san_luong: int) -> int:
    """Tính tiền nước theo bậc thang. Trả về số tiền (đồng)."""
    if san_luong < 0:
        raise ValueError("Sản lượng nước không được âm.")
    if san_luong <= 10:
        return san_luong * GIA_BAN_NUOC[0]
    if san_luong <= 20:
        return 10 * GIA_BAN_NUOC[0] + (san_luong - 10) * GIA_BAN_NUOC[1]
    if san_luong <= 30:
        return (10 * GIA_BAN_NUOC[0] +
                10 * GIA_BAN_NUOC[1] +
                (san_luong - 20) * GIA_BAN_NUOC[2])
    return (10 * GIA_BAN_NUOC[0] +
            10 * GIA_BAN_NUOC[1] +
            10 * GIA_BAN_NUOC[2] +
            (san_luong - 30) * GIA_BAN_NUOC[3])


# --------- BÀI 2: Tính nguyên liệu làm bánh ----------
BANH_DAU_XANH = (0.04, 0.07)   # (đường, đậu)
BANH_THAP_CAM = (0.06, 0.00)
BANH_DEO      = (0.05, 0.02)

def tinh_nguyen_lieu(so_dau_xanh: int, so_thap_cam: int, so_deo: int) -> dict:
    """Tính tổng đường, đậu (kg) cần cho một hộp bánh."""
    for v in (so_dau_xanh, so_thap_cam, so_deo):
        if v < 0:
            raise ValueError("Số lượng bánh không được âm.")
    duong = (so_dau_xanh * BANH_DAU_XANH[0] +
             so_thap_cam * BANH_THAP_CAM[0] +
             so_deo * BANH_DEO[0])
    dau = (so_dau_xanh * BANH_DAU_XANH[1] +
           so_thap_cam * BANH_THAP_CAM[1] +
           so_deo * BANH_DEO[1])
    return {"đậu": duong, "đường": dau}
