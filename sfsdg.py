from pathlib import Path
import importlib.util

module_path = Path().resolve() / "lap4menu.py"  # đảm bảo file nằm cùng thư mục với notebook
assert module_path.exists(), f"Không tìm thấy file: {module_path}"

spec = importlib.util.spec_from_file_location("lap4menu", str(module_path))
lap4menu = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lap4menu)

# dùng hàm từ module
tinh_tien_nuoc = lap4menu.tinh_tien_nuoc
tinh_nguyen_lieu = lap4menu.tinh_nguyen_lieu
