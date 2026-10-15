import os
import json
from mechanisms.base import BaseMechanism

MAX_FILE_LINES = 90

class MitosisMechanism(BaseMechanism):
    name = "mitosis"
    priority = 5

    def check_and_divide(self, file_path, context):
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Chỉ phân bào khi file quá dài và không phải là file con cháu
        if len(lines) > MAX_FILE_LINES and not file_path.endswith(("_worker.py", "_shield.py")):
            base_name = os.path.basename(file_path)[:-3]
            dir_name = os.path.join(os.path.dirname(file_path), f"{base_name}_organ")

            print(f"⚡ [PHÂN BÀO THÔNG MINH] Tệp '{base_name}.py' ({len(lines)} dòng) bắt đầu phân bào...")
            os.makedirs(dir_name, exist_ok=True)

            # SINH FILE CON 1: WORKER (Đảm nhận nhiệm vụ chính)
            worker_code = f'''# [CON TRƯỞNG: WORKER CỦA {base_name.upper()}]
from mechanisms.base import BaseMechanism

class {base_name.capitalize()}Worker(BaseMechanism):
    name = "{base_name}_worker"
    priority = 25

    def execute(self, context):
        print("⚙️ [{base_name.upper()}_WORKER] Đang chấp hành nhiệm vụ phân bào chuyên biệt...")
'''
            # SINH FILE CON 2: SHIELD (Đảm nhận kiểm định & phòng thủ)
            shield_code = f'''# [CON THỨ: SHIELD BẢO VỆ CỦA {base_name.upper()}]
from mechanisms.base import BaseMechanism

class {base_name.capitalize()}Shield(BaseMechanism):
    name = "{base_name}_shield"
    priority = 26

    def execute(self, context):
        print("🛡️ [{base_name.upper()}_SHIELD] Đang kích hoạt màng lọc bảo vệ tế bào con...")
'''
            # Ghi file con hợp cú pháp 100%
            with open(os.path.join(dir_name, f"{base_name}_worker.py"), "w", encoding="utf-8") as f:
                f.write(worker_code)
            with open(os.path.join(dir_name, f"{base_name}_shield.py"), "w", encoding="utf-8") as f:
                f.write(shield_code)

            # Đổi tên file mẹ thành file di tích để lưu niệm
            os.rename(file_path, file_path + ".ancestral_relic")
            print(f"👑 [PHÂN BÀO THÀNH CÔNG] Thư mục '{base_name}_organ' đã sinh 2 tế bào con hợp chuẩn!")

    def execute(self, context):
        mech_dir = "mechanisms"
        if not os.path.exists(mech_dir): return
        for root, _, files in os.walk(mech_dir):
            for file in files:
                if file.endswith(".py") and not file.startswith("__") and file != "base.py" and file != "mitosis.py":
                    try:
                        self.check_and_divide(os.path.join(root, file), context)
                    except Exception as e:
                        print(f"⚠️ [MITOSIS NOTICE]: {e}")
